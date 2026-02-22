# pyright: reportImportCycles=false
# ^ the above is fine b/c we only import for typechecking

from __future__ import annotations

import inspect
import logging
from collections import defaultdict
from collections.abc import Callable, Coroutine
from typing import TYPE_CHECKING, Any, TypeVar, get_type_hints, overload

import anyio

from fluxcrystal.cache import Cache
from fluxcrystal.endpoint_client import RESTClient
from fluxcrystal.endpoints import _REST_ENDPOINT
from fluxcrystal.events.base import Event
from fluxcrystal.events.channels import (
    ChannelCreateEvent,
    ChannelDeleteEvent,
    ChannelUpdateEvent,
    TypingStartEvent,
)
from fluxcrystal.events.gateway import ReadyEvent
from fluxcrystal.events.guilds import (
    GuildBanAddEvent,
    GuildBanRemoveEvent,
    GuildCreateEvent,
    GuildDeleteEvent,
    GuildMemberAddEvent,
    GuildMemberRemoveEvent,
    GuildMemberUpdateEvent,
    GuildUpdateEvent,
)
from fluxcrystal.events.messages import (
    MessageCreateEvent,
    MessageDeleteEvent,
    MessageUpdateEvent,
)

if TYPE_CHECKING:
    from fluxcrystal.gateway import GatewayConnection  # noqa: F401

log = logging.getLogger("fluxcrystal.bot")

EventT = TypeVar("EventT", bound=Event)
F = TypeVar("F", bound=Callable[..., Coroutine[Any, Any, None]])

# Callback type alias
ListenerT = Callable[..., Coroutine[Any, Any, None]]

# Gateway dispatch event name → event class factory.
# Built automatically from event_name() classmethods so adding a new event
# only requires adding it to the list below.
_EVENT_REGISTRY: dict[str, type[Event]] = {}


def _register_event(cls: type[Event]) -> None:
    """Register an event class in the global registry by its ``event_name()``."""
    try:
        name = cls.event_name()
        _EVENT_REGISTRY[name] = cls
    except Exception:
        pass


for _cls in (
    ReadyEvent,
    MessageCreateEvent,
    MessageUpdateEvent,
    MessageDeleteEvent,
    GuildCreateEvent,
    GuildUpdateEvent,
    GuildDeleteEvent,
    GuildMemberAddEvent,
    GuildMemberRemoveEvent,
    GuildMemberUpdateEvent,
    GuildBanAddEvent,
    GuildBanRemoveEvent,
    ChannelCreateEvent,
    ChannelUpdateEvent,
    ChannelDeleteEvent,
    TypingStartEvent,
):
    _register_event(_cls)


class GatewayBot:
    """
    The main bot class. Connects to Fluxer's gateway and fires off events
    to whatever listeners you've registered.

    Args:
        token: Your bot token from the Fluxer developer portal.
        base_url: Override this if you're running against a self-hosted Fluxer instance.
    """

    # REST client (messages, guilds, etc)
    rest: RESTClient

    #: In-memory cache of info from gateway events
    cache: Cache

    def __init__(
        self,
        token: str,
        *,
        base_url: str = _REST_ENDPOINT,
    ) -> None:
        self._token = token
        self.rest = RESTClient(base_url=base_url, token=token)
        self.cache = Cache()
        # event_class → list of async callbacks
        self._listeners: defaultdict[type[Event], list[ListenerT]] = defaultdict(list)
        # Cancel scope for programmatic stop
        self._cancel_scope: anyio.CancelScope | None = None

    def subscribe(
        self,
        event_type: type[EventT],
        callback: Callable[[EventT], Coroutine[Any, Any, None]],
    ) -> None:
        """Register a callback to fire when `event_type` events come in."""
        self._listeners[event_type].append(callback)

    def unsubscribe(
        self,
        event_type: type[EventT],
        callback: Callable[[EventT], Coroutine[Any, Any, None]],
    ) -> None:
        """Stop a previously-registered callback from firing."""
        try:
            self._listeners[event_type].remove(callback)
        except ValueError:
            pass

    @overload
    def listen(
        self,
        event_type: type[EventT],
    ) -> Callable[[Callable[[EventT], Coroutine[Any, Any, None]]], Callable[[EventT], Coroutine[Any, Any, None]]]:
        ...

    @overload
    def listen(
        self,
    ) -> Callable[[Callable[[EventT], Coroutine[Any, Any, None]]], Callable[[EventT], Coroutine[Any, Any, None]]]:
        ...

    def listen(
        self,
        event_type: type[EventT] | None = None,
    ) -> Callable[..., Any]:
        """
        Decorator to register an async function as an event listener.

        Pass the event type directly or let fluxcrystal figure it out from
        your type hints:

        **Explicit**:

            @bot.listen(fluxcrystal.MessageCreateEvent)
            async def on_message(event: fluxcrystal.MessageCreateEvent) -> None:
                ...

        **Inferred** (needs a type annotation):

            @bot.listen()
            async def on_message(event: fluxcrystal.MessageCreateEvent) -> None:
                ...
        """

        def decorator(
            func: Callable[[EventT], Coroutine[Any, Any, None]],
        ) -> Callable[[EventT], Coroutine[Any, Any, None]]:
            resolved: type[EventT] | None = event_type  # type: ignore[assignment]

            if resolved is None:
                # Infer from the function's first parameter annotation.
                try:
                    hints = get_type_hints(func)
                    params = list(inspect.signature(func).parameters)
                    if params:
                        resolved = hints.get(params[0])  # type: ignore[assignment]
                except Exception:
                    resolved = None

                if resolved is None:
                    raise TypeError(
                        f"Cannot infer event type for {func.__qualname__!r}. "
                        "Either annotate the first parameter or pass the event "
                        "type explicitly: @bot.listen(SomeEvent)."
                    )

            self.subscribe(resolved, func)
            return func

        return decorator

    # ------------------------------------------------------------------
    # Dispatch
    # ------------------------------------------------------------------

    async def dispatch(self, event: Event) -> None:
        """
        Fire an event at all registered listeners.

        Mostly used internally, but you can call it yourself to synthesize
        events (useful for testing).
        """
        event_type = type(event)
        for listener in list(self._listeners.get(event_type, [])):
            try:
                await listener(event)
            except Exception:
                log.exception(
                    "Unhandled exception in listener %r for %r",
                    listener,
                    event_type.__name__,
                )

    # ------------------------------------------------------------------
    # Internal gateway hook
    # ------------------------------------------------------------------

    async def _on_raw_dispatch(
        self, event_name: str, data: dict[str, Any]
    ) -> None:
        """Called by the gateway when a DISPATCH event comes in."""
        # Update cache before dispatching to listeners.
        self.cache._update(event_name, data)

        event_cls = _EVENT_REGISTRY.get(event_name)
        if event_cls is None:
            return  # No listener registered for this event type

        try:
            event: Event = event_cls(self, data)
        except Exception:
            log.exception(
                "Failed to construct event %r from gateway data", event_name
            )
            return

        await self.dispatch(event)

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def stop(self) -> None:
        """Tell the bot to shut down cleanly."""
        if self._cancel_scope is not None:
            self._cancel_scope.cancel()

    async def start(self) -> None:
        """
        Connect to the gateway and start processing events.

        This blocks until the bot stops or something explodes.
        Most people should use `run` instead.
        """
        from fluxcrystal.gateway import GatewayConnection  # local import breaks cycle

        async with self.rest:  # properly manage the HTTP client lifecycle
            ws_url = await self.rest.get_gateway_url()
            log.info("Connecting to gateway: %s", ws_url)
            connection = GatewayConnection(bot=self, token=self._token)

            with anyio.CancelScope() as self._cancel_scope:
                await connection.start(ws_url)

    def run(self) -> None:
        """
        Start the bot and block until it exits.

        Handles Ctrl-C gracefully. Call `stop` from async code for
        a clean shutdown.
        """
        try:
            anyio.run(self.start)
        except (KeyboardInterrupt, SystemExit):
            pass
