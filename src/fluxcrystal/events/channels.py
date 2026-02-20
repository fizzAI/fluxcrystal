"""
Channel-related gateway events.
"""

from __future__ import annotations

from typing import Any

from fluxcrystal.events.base import Event
from fluxcrystal.models.channels import Channel


class ChannelCreateEvent(Event):
    """Fired when a new channel is created."""

    __slots__ = ("channel",)

    def __init__(self, app: Any, data: dict[str, Any]) -> None:
        super().__init__(app)
        self.channel: Channel = Channel(data)

    @classmethod
    def event_name(cls) -> str:
        return "CHANNEL_CREATE"

    def __repr__(self) -> str:
        return f"<ChannelCreateEvent channel={self.channel!r}>"


class ChannelUpdateEvent(Event):
    """Fired when a channel is updated."""

    __slots__ = ("channel",)

    def __init__(self, app: Any, data: dict[str, Any]) -> None:
        super().__init__(app)
        self.channel: Channel = Channel(data)

    @classmethod
    def event_name(cls) -> str:
        return "CHANNEL_UPDATE"

    def __repr__(self) -> str:
        return f"<ChannelUpdateEvent channel={self.channel!r}>"


class ChannelDeleteEvent(Event):
    """Fired when a channel is deleted."""

    __slots__ = ("channel",)

    def __init__(self, app: Any, data: dict[str, Any]) -> None:
        super().__init__(app)
        self.channel: Channel = Channel(data)

    @classmethod
    def event_name(cls) -> str:
        return "CHANNEL_DELETE"

    def __repr__(self) -> str:
        return f"<ChannelDeleteEvent channel={self.channel!r}>"


class TypingStartEvent(Event):
    """Fired when a user starts typing in a channel."""

    __slots__ = ("channel_id", "guild_id", "user_id", "timestamp")

    def __init__(self, app: Any, data: dict[str, Any]) -> None:
        super().__init__(app)
        self.channel_id: str = data["channel_id"]
        self.guild_id: str | None = data.get("guild_id")
        self.user_id: str = data["user_id"]
        self.timestamp: int = data.get("timestamp", 0)

    @classmethod
    def event_name(cls) -> str:
        return "TYPING_START"

    def __repr__(self) -> str:
        return (
            f"<TypingStartEvent channel_id={self.channel_id!r} "
            f"user_id={self.user_id!r}>"
        )
