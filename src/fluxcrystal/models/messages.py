"""
Message model types.
"""

from __future__ import annotations

from typing import Any

from fluxcrystal.models.users import User


class Message:
    """A message in a channel."""

    __slots__ = (
        "id",
        "channel_id",
        "guild_id",
        "author",
        "content",
        "timestamp",
        "edited_timestamp",
        "type",
        "tts",
        "mention_everyone",
        "pinned",
        "nonce",
        "webhook_id",
        "flags",
    )

    def __init__(self, data: dict[str, Any]) -> None:
        self.id: str = data["id"]
        self.channel_id: str = data["channel_id"]
        self.guild_id: str | None = data.get("guild_id")
        self.author: User = User(data["author"])
        self.content: str = data.get("content", "")
        self.timestamp: str = data["timestamp"]
        self.edited_timestamp: str | None = data.get("edited_timestamp")
        self.type: int = data.get("type", 0)
        self.tts: bool = data.get("tts", False)
        self.mention_everyone: bool = data.get("mention_everyone", False)
        self.pinned: bool = data.get("pinned", False)
        self.nonce: str | None = data.get("nonce")
        self.webhook_id: str | None = data.get("webhook_id")
        self.flags: int = data.get("flags", 0)

    @property
    def is_webhook(self) -> bool:
        """True if this message came from a webhook."""
        return self.webhook_id is not None

    def __repr__(self) -> str:
        return (
            f"<Message id={self.id!r} channel_id={self.channel_id!r} "
            f"author={self.author!r}>"
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Message):
            return self.id == other.id
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.id)
