"""
Guild and guild-member model types.
"""

from __future__ import annotations

from typing import Any

from fluxcrystal.models.users import User


class Role:
    """A guild role."""

    __slots__ = (
        "id",
        "name",
        "color",
        "hoist",
        "position",
        "permissions",
        "mentionable",
    )

    def __init__(self, data: dict[str, Any]) -> None:
        self.id: str = data["id"]
        self.name: str = data["name"]
        self.color: int = data.get("color", 0)
        self.hoist: bool = data.get("hoist", False)
        self.position: int = data.get("position", 0)
        self.permissions: str = data.get("permissions", "0")
        self.mentionable: bool = data.get("mentionable", False)

    def __repr__(self) -> str:
        return f"<Role id={self.id!r} name={self.name!r}>"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Role):
            return self.id == other.id
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.id)


class GuildMember:
    """A member of a guild - a user who has joined."""

    __slots__ = (
        "user",
        "nick",
        "roles",
        "joined_at",
        "deaf",
        "mute",
        "communication_disabled_until",
    )

    def __init__(self, data: dict[str, Any]) -> None:
        self.user: User = User(data["user"])
        self.nick: str | None = data.get("nick")
        self.roles: list[str] = data.get("roles", [])
        self.joined_at: str = data["joined_at"]
        self.deaf: bool = data.get("deaf", False)
        self.mute: bool = data.get("mute", False)
        self.communication_disabled_until: str | None = data.get(
            "communication_disabled_until"
        )

    @property
    def display_name(self) -> str:
        """The name shown for this member - their nick if set, otherwise their display name."""
        return self.nick or self.user.display_name

    def __repr__(self) -> str:
        return f"<GuildMember user={self.user!r} nick={self.nick!r}>"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, GuildMember):
            return self.user.id == other.user.id
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.user.id)


class Guild:
    """A guild (also called a server in some clients)."""

    __slots__ = (
        "id",
        "name",
        "icon",
        "owner_id",
        "features",
        "verification_level",
        "default_message_notifications",
        "explicit_content_filter",
        "mfa_level",
        "system_channel_id",
        "rules_channel_id",
    )

    def __init__(self, data: dict[str, Any]) -> None:
        self.id: str = data["id"]
        # Unavailable guilds (sent during READY / GUILD_CREATE before the full
        # payload arrives) only carry id + unavailable=True.
        self.name: str = data.get("name", "")
        self.icon: str | None = data.get("icon")
        self.owner_id: str = data.get("owner_id", "")
        self.features: list[str] = data.get("features", [])
        self.verification_level: int = data.get("verification_level", 0)
        self.default_message_notifications: int = data.get(
            "default_message_notifications", 0
        )
        self.explicit_content_filter: int = data.get("explicit_content_filter", 0)
        self.mfa_level: int = data.get("mfa_level", 0)
        self.system_channel_id: str | None = data.get("system_channel_id")
        self.rules_channel_id: str | None = data.get("rules_channel_id")

    def __repr__(self) -> str:
        return f"<Guild id={self.id!r} name={self.name!r}>"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Guild):
            return self.id == other.id
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.id)
