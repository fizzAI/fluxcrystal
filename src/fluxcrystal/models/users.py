"""
User model types.
"""

from __future__ import annotations

from typing import Any


class User:
    """A user, either a regular user or a bot account."""

    __slots__ = (
        "id",
        "username",
        "discriminator",
        "global_name",
        "avatar",
        "avatar_color",
        "bot",
        "system",
        "flags",
    )

    def __init__(self, data: dict[str, Any]) -> None:
        self.id: str = data["id"]
        self.username: str = data["username"]
        self.discriminator: str = data["discriminator"]
        self.global_name: str | None = data.get("global_name")
        self.avatar: str | None = data.get("avatar")
        self.avatar_color: int | None = data.get("avatar_color")
        self.bot: bool = data.get("bot", False)
        self.system: bool = data.get("system", False)
        self.flags: int = data.get("flags", 0)

    @property
    def display_name(self) -> str:
        """What is shown in the UI for this user (global_name if they set one, otherwise username)"""
        return self.global_name or self.username

    def __repr__(self) -> str:
        return f"<User id={self.id!r} username={self.username!r} bot={self.bot!r}>"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.id == other.id
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.id)
