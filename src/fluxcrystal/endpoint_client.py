from __future__ import annotations

import asyncio
import json
import logging
from typing import Any

import httpx

from fluxcrystal.errors import RateLimitedError, try_raise_error
from fluxcrystal.models.channels import Channel
from fluxcrystal.models.guilds import Guild, GuildMember
from fluxcrystal.models.messages import Message, MessageReference, RichEmbed
from fluxcrystal.models.upload import AttachmentUpload
from fluxcrystal.models.users import User

log = logging.getLogger("fluxcrystal.rest")

# Max automatic retries on 429 before giving up.
_MAX_RATE_LIMIT_RETRIES = 5


class RESTClient:
    """
    HTTP client for Fluxer's REST API.
    """

    _client: httpx.AsyncClient
    _token: str | None

    def __init__(
        self,
        base_url: str = "https://api.fluxer.app/v1",
        token: str | None = None,
    ) -> None:
        self._client = httpx.AsyncClient(
            base_url=base_url,
            timeout=httpx.Timeout(30.0),
        )
        self._token = token

    async def __aenter__(self) -> RESTClient:
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self._client.__aexit__(*args)

    async def close(self) -> None:
        """Shut down the HTTP client."""
        await self._client.aclose()

    def _auth_headers(self) -> dict[str, str]:
        if self._token is None:
            return {}
        return {"Authorization": f"Bot {self._token}"}

    async def _request(
        self,
        method: str,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        files: dict[str, Any] | None = None,
    ) -> Any:
        """
        Send a request, automatically retrying on 429 (rate-limit) responses.
        """
        for attempt in range(_MAX_RATE_LIMIT_RETRIES):
            response = await self._client.request(
                method,
                path,
                headers=self._auth_headers(),
                json=json,
                files=files,
                params=params,
            )

            # Empty body (e.g. 204 No Content)
            if response.status_code == 204:
                return {}

            body: dict[str, Any] = response.json()

            # We only need to worry about rate limit statuses since try_raise_error gets the rest
            if response.status_code == 429:
                retry_after: float = float(
                    body.get("retry_after", 1.0)
                )
                if attempt < _MAX_RATE_LIMIT_RETRIES - 1:
                    log.warning(
                        "Rate limited on %s %s – retrying in %.2fs (attempt %d/%d)",
                        method, path, retry_after, attempt + 1, _MAX_RATE_LIMIT_RETRIES,
                    )
                    await asyncio.sleep(retry_after)
                    continue
                # Exhausted retries – raise.
                raise RateLimitedError(
                    body.get("message", "Rate limited"),
                    retry_after=retry_after,
                )

            return try_raise_error(body, response.status_code)

        # Should be unreachable.
        return {}

    async def _get(
        self, path: str, *, params: dict[str, Any] | None = None
    ) -> Any:
        return await self._request("GET", path, params=params)

    async def _post(
        self, path: str, body: dict[str, Any] | None = None, files: dict[str, tuple[bytes, str]] | None = None
    ) -> Any:
        if files is None:
            return await self._request("POST", path, json=body or {})
        else:
            real_files: dict[str, tuple[str | None, bytes, str]] = {
                "payload_json": (None, json.dumps(body).encode("utf-8"), "application/json")
            }
            for i, (name, file_info) in enumerate(files.items()):
                content_bytes, content_type = file_info
                real_files[f"files[{i}]"] = (name, content_bytes, content_type)

            return await self._request("POST", path, files=real_files)

    async def _patch(self, path: str, body: dict[str, Any]) -> Any:
        return await self._request("PATCH", path, json=body)

    async def _delete(self, path: str) -> None:
        await self._request("DELETE", path)

    async def _put(
        self, path: str, body: dict[str, Any] | None = None
    ) -> Any:
        return await self._request("PUT", path, json=body or {})

    # ------------------------------------------------------------------
    # Gateway
    # ------------------------------------------------------------------

    async def get_gateway_url(self) -> str:
        """Grab the WebSocket gateway URL from the API."""
        data = await self._get("/gateway/bot")
        return str(data["url"])

    # ------------------------------------------------------------------
    # Messages
    # ------------------------------------------------------------------

    async def create_message(
        self,
        channel_id: str,
        *,
        content: str | None = None,
        message_reference: MessageReference | None = None,
        tts: bool = False,
        nonce: str | None = None,
        attachments: list[AttachmentUpload] | None = None,
        embeds: list[RichEmbed] | None = None,
    ) -> Message:
        """
        Send a message to a channel. To reply or forward messages, please see the details on referencing messages.
        """
        body: dict[str, Any] = {"content": content}
        
        if message_reference is not None:
            body["message_reference"] = message_reference
        if tts:
            body["tts"] = True
        if nonce is not None:
            body["nonce"] = nonce
        
        # Handle embeds
        if embeds is not None:
            body["embeds"] = [embed._copy_state() for embed in embeds]
        
        # Handle attachments
        files: dict[str, tuple[bytes, str]] | None = None
        if attachments:
            files = {}
            attachment_meta: list[dict[str, Any]] = []
            
            for i, attachment in enumerate(attachments):
                content_bytes = (
                    attachment.content.encode("utf-8")
                    if isinstance(attachment.content, str)
                    else attachment.content
                )
                filename = attachment.filename or f"file_{i}"
                
                # Use content_type if provided, otherwise default to octet-stream
                content_type = attachment.content_type or "application/octet-stream"
                files[filename] = (content_bytes, content_type)
                
                # Attachment metadata needs 'id' matching the files[N] index
                meta: dict[str, Any] = {
                    "id": i,
                    "filename": filename,
                }
                if attachment.description is not None:
                    meta["description"] = attachment.description
                attachment_meta.append(meta)
            
            body["attachments"] = attachment_meta
        
        data = await self._post(f"/channels/{channel_id}/messages", body, files=files)
        return Message(data)

    async def fetch_message(self, channel_id: str, message_id: str) -> Message:
        """Get a single message."""
        data = await self._get(f"/channels/{channel_id}/messages/{message_id}")
        return Message(data)

    async def fetch_messages(
        self,
        channel_id: str,
        *,
        limit: int = 50,
        before: str | None = None,
        after: str | None = None,
        around: str | None = None,
    ) -> list[Message]:
        """
        Fetch up to *limit* messages from a channel.

        ``GET /channels/{channel_id}/messages``
        """
        params: dict[str, Any] = {"limit": limit}
        if before:
            params["before"] = before
        if after:
            params["after"] = after
        if around:
            params["around"] = around
        data = await self._get(f"/channels/{channel_id}/messages", params=params)
        # The endpoint returns a list, not a dict
        if isinstance(data, list):
            return [Message(m) for m in data]
        return []

    async def edit_message(
        self,
        channel_id: str,
        message_id: str,
        *,
        content: str | None = None,
        embeds: list[RichEmbed] | None = None,
    ) -> Message:
        """Edit one of the bot's own messages."""
        body: dict[str, Any] = {}
        if content is not None:
            body["content"] = content
        if embeds is not None:
            body["embeds"] = [embed._copy_state() for embed in embeds]
        data = await self._patch(f"/channels/{channel_id}/messages/{message_id}", body)
        return Message(data)

    async def delete_message(self, channel_id: str, message_id: str) -> None:
        """Nuke a message."""
        await self._delete(f"/channels/{channel_id}/messages/{message_id}")

    async def send_typing(self, channel_id: str) -> None:
        """Show the "user is typing..." indicator in a channel."""
        await self._post(f"/channels/{channel_id}/typing")

    async def add_reaction(
        self, channel_id: str, message_id: str, emoji: str
    ) -> None:
        """
        Add a reaction to a message.
        `emoji` is a url-safe emoji string, e.g. ``"🔥"`` or ``"name:id"`` for custom emoji.
        """
        import urllib.parse
        encoded = urllib.parse.quote(emoji, safe="")
        await self._put(
            f"/channels/{channel_id}/messages/{message_id}/reactions/{encoded}/@me"
        )

    async def remove_reaction(
        self, channel_id: str, message_id: str, emoji: str
    ) -> None:
        """
        Remove the bot's reaction from a message.
        `emoji` is a url-safe emoji string, e.g. ``"🔥"`` or ``"name:id"`` for custom emoji.
        """
        import urllib.parse
        encoded = urllib.parse.quote(emoji, safe="")
        await self._delete(
            f"/channels/{channel_id}/messages/{message_id}/reactions/{encoded}/@me"
        )

    # ------------------------------------------------------------------
    # Channels
    # ------------------------------------------------------------------

    async def fetch_channel(self, channel_id: str) -> Channel:
        """Get a channel by its ID."""
        data = await self._get(f"/channels/{channel_id}")
        return Channel(data)

    async def fetch_guild_channels(self, guild_id: str) -> list[Channel]:
        """Get all channels in a guild."""
        data = await self._get(f"/guilds/{guild_id}/channels")
        if isinstance(data, list):
            return [Channel(c) for c in data]
        return []

    # ------------------------------------------------------------------
    # Guilds
    # ------------------------------------------------------------------

    async def fetch_guild(self, guild_id: str) -> Guild:
        """Get a guild by its ID."""
        data = await self._get(f"/guilds/{guild_id}")
        return Guild(data)

    async def fetch_guild_member(
        self, guild_id: str, user_id: str
    ) -> GuildMember:
        """Get a specific member of a guild."""
        data = await self._get(f"/guilds/{guild_id}/members/{user_id}")
        return GuildMember(data)

    async def kick_member(self, guild_id: str, user_id: str) -> None:
        """Kick a user from a guild."""
        await self._delete(f"/guilds/{guild_id}/members/{user_id}")

    async def ban_member(
        self,
        guild_id: str,
        user_id: str,
        *,
        delete_message_days: int = 0,
        reason: str | None = None,
    ) -> None:
        """Ban a user from a guild."""
        body: dict[str, Any] = {"delete_message_days": delete_message_days}
        if reason is not None:
            body["reason"] = reason
        await self._put(f"/guilds/{guild_id}/bans/{user_id}", body)

    async def unban_member(self, guild_id: str, user_id: str) -> None:
        """Lift a ban on a user."""
        await self._delete(f"/guilds/{guild_id}/bans/{user_id}")

    async def add_member_role(
        self, guild_id: str, user_id: str, role_id: str
    ) -> None:
        """Give a role to a guild member."""
        await self._put(
            f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}"
        )

    async def remove_member_role(
        self, guild_id: str, user_id: str, role_id: str
    ) -> None:
        """Take a role away from a guild member."""
        await self._delete(
            f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}"
        )

    # ------------------------------------------------------------------
    # Users
    # ------------------------------------------------------------------

    async def fetch_my_user(self) -> User:
        """Get the bot's own user object."""
        data = await self._get("/users/@me")
        return User(data)

    async def fetch_user(self, user_id: str) -> User:
        """Get a user by their ID."""
        data = await self._get(f"/users/{user_id}")
        return User(data)
