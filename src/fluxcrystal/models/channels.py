"""
Channel model types.
"""

from __future__ import annotations

from typing import Any


class Channel:
    """Any type of channel."""

    __slots__ = (
        "id",
        "type",
        "guild_id",
        "name",
        "topic",
        "nsfw",
        "last_message_id",
        "position",
        "parent_id",
        "rate_limit_per_user",
    )

    def __init__(self, data: dict[str, Any]) -> None:
        self.id: str = data["id"]
        self.type: int = data["type"]
        self.guild_id: str | None = data.get("guild_id")
        self.name: str | None = data.get("name")
        self.topic: str | None = data.get("topic")
        self.nsfw: bool = data.get("nsfw", False)
        self.last_message_id: str | None = data.get("last_message_id")
        self.position: int | None = data.get("position")
        self.parent_id: str | None = data.get("parent_id")
        self.rate_limit_per_user: int | None = data.get("rate_limit_per_user")

    def __repr__(self) -> str:
        return (
            f"<Channel id={self.id!r} name={self.name!r} type={self.type!r}>"
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Channel):
            return self.id == other.id
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.id)
