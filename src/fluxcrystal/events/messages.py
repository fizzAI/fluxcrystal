"""
Message-related gateway events.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from fluxcrystal.events.base import Event
from fluxcrystal.models.messages import Message
from fluxcrystal.models.users import User

if TYPE_CHECKING:
    pass


class MessageCreateEvent(Event):
    """Fired when a new message is created in any channel the bot can see."""

    __slots__ = ("message",)

    def __init__(self, app: Any, data: dict[str, Any]) -> None:
        super().__init__(app)
        self.message: Message = Message(data)

    @classmethod
    def event_name(cls) -> str:
        return "MESSAGE_CREATE"

    # ── Convenience pass-throughs ────────────────────────────────────────

    @property
    def channel_id(self) -> str:
        """The ID of the channel the message was sent in."""
        return self.message.channel_id

    @property
    def guild_id(self) -> str | None:
        """The ID of the guild, if this was a guild message."""
        return self.message.guild_id

    @property
    def author(self) -> User:
        """The user who sent the message."""
        return self.message.author

    @property
    def content(self) -> str:
        """The text content of the message."""
        return self.message.content

    @property
    def is_human(self) -> bool:
        """True if this was sent by a real person, not a bot or webhook."""
        return not self.message.author.bot and not self.message.is_webhook

    @property
    def is_bot(self) -> bool:
        """True if this was sent by a bot account."""
        return self.message.author.bot

    def __repr__(self) -> str:
        return f"<MessageCreateEvent message={self.message!r}>"


class MessageUpdateEvent(Event):
    """Fired when a message is edited."""

    __slots__ = ("message",)

    def __init__(self, app: Any, data: dict[str, Any]) -> None:
        super().__init__(app)
        self.message: Message = Message(data)

    @classmethod
    def event_name(cls) -> str:
        return "MESSAGE_UPDATE"

    @property
    def channel_id(self) -> str:
        """The ID of the channel containing the edited message."""
        return self.message.channel_id

    @property
    def guild_id(self) -> str | None:
        """The ID of the guild, if this was a guild message."""
        return self.message.guild_id

    @property
    def content(self) -> str:
        """The new text content of the message."""
        return self.message.content

    def __repr__(self) -> str:
        return f"<MessageUpdateEvent message={self.message!r}>"


class MessageDeleteEvent(Event):
    """Fired when a message is deleted."""

    __slots__ = ("message_id", "channel_id", "guild_id")

    def __init__(self, app: Any, data: dict[str, Any]) -> None:
        super().__init__(app)
        self.message_id: str = data["id"]
        self.channel_id: str = data["channel_id"]
        self.guild_id: str | None = data.get("guild_id")

    @classmethod
    def event_name(cls) -> str:
        return "MESSAGE_DELETE"

    def __repr__(self) -> str:
        return (
            f"<MessageDeleteEvent message_id={self.message_id!r} "
            f"channel_id={self.channel_id!r}>"
        )
