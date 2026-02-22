# pyright: reportImportCycles=false
# ^ the above is fine b/c we only import for typechecking

from __future__ import annotations

import json
import logging
import sys
from typing import TYPE_CHECKING, Any, cast

import anyio
import httpx
import httpx_ws

if TYPE_CHECKING:
    from fluxcrystal.bot import GatewayBot

log = logging.getLogger("fluxcrystal.gateway")

# Constants (hopefully)
OP_DISPATCH = 0
OP_HEARTBEAT = 1
OP_IDENTIFY = 2
OP_RESUME = 6
OP_RECONNECT = 7
OP_INVALID_SESSION = 9
OP_HELLO = 10
OP_HEARTBEAT_ACK = 11

GATEWAY_VERSION = 1

_FATAL_CLOSE_CODES: frozenset[int] = frozenset(
    {
        4004,  # AUTHENTICATION_FAILED
        4010,  # INVALID_SHARD
        4011,  # SHARDING_REQUIRED
        4012,  # INVALID_API_VERSION
    }
)


class _WantReconnect(Exception):
    """Internal: raised to break out of the lifecycle and reconnect."""

    def __init__(self, *, clear_session: bool = False) -> None:
        self.clear_session = clear_session
        super().__init__()


class _FatalGatewayError(Exception):
    """Raised for close codes that mean we must not reconnect."""


class GatewayConnection:
    """
    Manages a single WebSocket connection to the Fluxer gateway.
    """

    def __init__(self, bot: GatewayBot, token: str, heartbeat_interval: float | None = None) -> None:
        self._bot = bot
        self._token = token

        # State that lives across reconnects
        self._session_id: str | None = None
        self._seq: int | None = None
        self._heartbeat_interval: float = heartbeat_interval  # updated by HELLO  # pyright: ignore[reportAttributeAccessIssue]
        self._ack_received: bool = True

        # Written by HELLO handler, read by heartbeat loop
        self._hello_received: anyio.Event = anyio.Event()

    async def start(self, ws_url: str) -> None:
        """
        Connect and begin processing events.  Reconnects automatically on
        resumable disconnects; raises on fatal ones.
        """
        # Append version and encoding to the gateway URL
        if "?" not in ws_url:
            ws_url = f"{ws_url}?v={GATEWAY_VERSION}&encoding=json"

        while True:
            self._hello_received = anyio.Event()
            self._ack_received = True
            try:
                await self._run(ws_url)
            except _FatalGatewayError:
                raise
            except _WantReconnect as exc:
                if exc.clear_session:
                    self._session_id = None
                    self._seq = None
                log.info("Reconnecting to gateway…")
                await anyio.sleep(2.0)
            except Exception as exc:  # noqa: BLE001
                log.warning(
                    "Gateway error (%s: %s), reconnecting…", type(exc).__name__, exc
                )
                await anyio.sleep(2.0)

    async def _run(self, ws_url: str) -> None:
        """Open a WebSocket and run the full connection lifecycle."""
        async with httpx.AsyncClient() as http_client:
            async with httpx_ws.aconnect_ws(ws_url, http_client) as ws:
                await self._lifecycle(ws)

    async def _lifecycle(self, ws: httpx_ws.AsyncWebSocketSession) -> None:
        """Coordinate the read loop and heartbeat loop over one connection."""
        try:
            async with anyio.create_task_group() as tg:
                tg.start_soon(self._read_loop, ws, tg.cancel_scope)
                tg.start_soon(self._heartbeat_loop, ws, tg.cancel_scope)
        except* _FatalGatewayError as eg:
            raise eg.exceptions[0] from None
        except* _WantReconnect as eg:
            raise eg.exceptions[0] from None

    async def _heartbeat_loop(
        self,
        ws: httpx_ws.AsyncWebSocketSession,
        cancel_scope: anyio.CancelScope,
    ) -> None:
        """Periodically send HEARTBEAT; detect zombie connections."""
        # Wait for HELLO to set the interval (up to 30 s)
        with anyio.move_on_after(30.0):
            await self._hello_received.wait()

        while True:
            await anyio.sleep(self._heartbeat_interval)
            if not self._ack_received:
                log.warning("Heartbeat not acknowledged – forcing reconnect")
                cancel_scope.cancel()
                return
            self._ack_received = False
            await self._send(ws, {"op": OP_HEARTBEAT, "d": self._seq})
            log.debug("Sent HEARTBEAT (seq=%s)", self._seq)

    async def _read_loop(
        self,
        ws: httpx_ws.AsyncWebSocketSession,
        cancel_scope: anyio.CancelScope,
    ) -> None:
        """Receive and dispatch every message from the gateway."""
        while True:
            try:
                raw = await ws.receive_text()
            except httpx_ws.WebSocketDisconnect as exc:
                code = exc.code
                if code is not None and code in _FATAL_CLOSE_CODES:
                    raise _FatalGatewayError(
                        f"Gateway closed with fatal code {code}"
                    ) from exc
                log.debug("WS closed with code %s, reconnecting", code)
                raise _WantReconnect() from exc
            payload: dict[str, Any] = json.loads(raw)
            await self._handle(ws, payload, cancel_scope)

    async def _handle(
        self,
        ws: httpx_ws.AsyncWebSocketSession,
        payload: dict[str, Any],
        cancel_scope: anyio.CancelScope,
    ) -> None:
        op: int = payload["op"]
        data: Any = payload.get("d")

        if op == OP_HELLO:
            interval_ms: int = data["heartbeat_interval"]
            if not self._heartbeat_interval:
                self._heartbeat_interval = interval_ms / 1000.0
                log.debug("HELLO received, heartbeat_interval=%s ms", interval_ms)
            self._hello_received.set()
            if self._session_id and self._seq is not None:
                await self._send_resume(ws)
            else:
                await self._send_identify(ws)

        elif op == OP_DISPATCH:
            seq: int | None = payload.get("s")
            if seq is not None:
                self._seq = seq
            event_name: str = payload.get("t") or ""
            await self._dispatch_event(event_name, data or {})

        elif op == OP_HEARTBEAT:
            # Server requests an immediate heartbeat
            await self._send(ws, {"op": OP_HEARTBEAT, "d": self._seq})

        elif op == OP_HEARTBEAT_ACK:
            self._ack_received = True
            log.debug("HEARTBEAT_ACK received")

        elif op == OP_RECONNECT:
            log.info("Gateway requested RECONNECT")
            raise _WantReconnect()

        elif op == OP_INVALID_SESSION:
            resumable: bool = bool(data)
            log.warning("INVALID_SESSION (resumable=%s)", resumable)
            raise _WantReconnect(clear_session=not resumable)

    async def _send(
        self, ws: httpx_ws.AsyncWebSocketSession, payload: dict[str, Any]
    ) -> None:
        await ws.send_text(json.dumps(payload))

    async def _send_identify(self, ws: httpx_ws.AsyncWebSocketSession) -> None:
        payload = {
            "op": OP_IDENTIFY,
            "d": {
                "token": self._token,
                "properties": {
                    "os": sys.platform,
                    "browser": "fluxcrystal",
                    "device": "fluxcrystal",
                },
            },
        }
        await self._send(ws, payload)
        log.debug("Sent IDENTIFY")

    async def _send_resume(self, ws: httpx_ws.AsyncWebSocketSession) -> None:
        payload = {
            "op": OP_RESUME,
            "d": {
                "token": self._token,
                "session_id": self._session_id,
                "seq": self._seq,
            },
        }
        await self._send(ws, payload)
        log.debug(
            "Sent RESUME (session_id=%s, seq=%s)", self._session_id, self._seq
        )

    async def _dispatch_event(
        self, event_name: str, data: dict[str, Any]
    ) -> None:
        """
        Convert a raw gateway dispatch into a typed event and hand it to
        the bot for listener dispatch.
        """
        if event_name == "READY":
            self._session_id = data.get("session_id")
            log.info(
                "Gateway READY (session_id=%s, user=%s#%s)",
                self._session_id,
                data.get("user", {}).get("username"),
                data.get("user", {}).get("discriminator"),
            )

        await cast(Any, self._bot)._on_raw_dispatch(event_name, data)
