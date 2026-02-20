"""
Guild-related gateway events.
"""

from __future__ import annotations

from typing import Any

from fluxcrystal.events.base import Event
from fluxcrystal.models.guilds import Guild, GuildMember
from fluxcrystal.models.users import User


class GuildCreateEvent(Event):
    """Fired when the bot joins a guild, or on initial connect for all guilds."""

    __slots__ = ("guild",)

    def __init__(self, app: Any, data: dict[str, Any]) -> None:
        super().__init__(app)
        self.guild: Guild = Guild(data)

    @classmethod
    def event_name(cls) -> str:
        return "GUILD_CREATE"

    @property
    def guild_id(self) -> str:
        """The ID of the guild."""
        return self.guild.id

    def __repr__(self) -> str:
        return f"<GuildCreateEvent guild={self.guild!r}>"


class GuildUpdateEvent(Event):
    """Fired when a guild's settings are updated."""

    __slots__ = ("guild",)

    def __init__(self, app: Any, data: dict[str, Any]) -> None:
        super().__init__(app)
        self.guild: Guild = Guild(data)

    @classmethod
    def event_name(cls) -> str:
        return "GUILD_UPDATE"

    def __repr__(self) -> str:
        return f"<GuildUpdateEvent guild={self.guild!r}>"


class GuildDeleteEvent(Event):
    """Fired when the bot is removed from a guild, or the guild becomes unavailable."""

    __slots__ = ("guild_id", "unavailable")

    def __init__(self, app: Any, data: dict[str, Any]) -> None:
        super().__init__(app)
        self.guild_id: str = data["id"]
        self.unavailable: bool = data.get("unavailable", False)

    @classmethod
    def event_name(cls) -> str:
        return "GUILD_DELETE"

    def __repr__(self) -> str:
        return (
            f"<GuildDeleteEvent guild_id={self.guild_id!r} "
            f"unavailable={self.unavailable!r}>"
        )


class GuildMemberAddEvent(Event):
    """Fired when a user joins a guild."""

    __slots__ = ("member", "guild_id")

    def __init__(self, app: Any, data: dict[str, Any]) -> None:
        super().__init__(app)
        self.guild_id: str = data["guild_id"]
        self.member: GuildMember = GuildMember(data)

    @classmethod
    def event_name(cls) -> str:
        return "GUILD_MEMBER_ADD"

    def __repr__(self) -> str:
        return (
            f"<GuildMemberAddEvent guild_id={self.guild_id!r} "
            f"member={self.member!r}>"
        )


class GuildMemberRemoveEvent(Event):
    """Fired when a user leaves or is kicked from a guild."""

    __slots__ = ("guild_id", "user")

    def __init__(self, app: Any, data: dict[str, Any]) -> None:
        super().__init__(app)
        self.guild_id: str = data["guild_id"]
        self.user: User = User(data["user"])

    @classmethod
    def event_name(cls) -> str:
        return "GUILD_MEMBER_REMOVE"

    def __repr__(self) -> str:
        return (
            f"<GuildMemberRemoveEvent guild_id={self.guild_id!r} "
            f"user={self.user!r}>"
        )


class GuildMemberUpdateEvent(Event):
    """Fired when a guild member's properties are updated (nick, roles, etc.)."""

    __slots__ = ("guild_id", "user", "nick", "roles")

    def __init__(self, app: Any, data: dict[str, Any]) -> None:
        super().__init__(app)
        self.guild_id: str = data["guild_id"]
        self.user: User = User(data["user"])
        self.nick: str | None = data.get("nick")
        self.roles: list[str] = data.get("roles", [])

    @classmethod
    def event_name(cls) -> str:
        return "GUILD_MEMBER_UPDATE"

    def __repr__(self) -> str:
        return (
            f"<GuildMemberUpdateEvent guild_id={self.guild_id!r} "
            f"user={self.user!r}>"
        )


class GuildBanAddEvent(Event):
    """Fired when a user is banned from a guild."""

    __slots__ = ("guild_id", "user")

    def __init__(self, app: Any, data: dict[str, Any]) -> None:
        super().__init__(app)
        self.guild_id: str = data["guild_id"]
        self.user: User = User(data["user"])

    @classmethod
    def event_name(cls) -> str:
        return "GUILD_BAN_ADD"

    def __repr__(self) -> str:
        return (
            f"<GuildBanAddEvent guild_id={self.guild_id!r} user={self.user!r}>"
        )


class GuildBanRemoveEvent(Event):
    """Fired when a user's ban is removed from a guild."""

    __slots__ = ("guild_id", "user")

    def __init__(self, app: Any, data: dict[str, Any]) -> None:
        super().__init__(app)
        self.guild_id: str = data["guild_id"]
        self.user: User = User(data["user"])

    @classmethod
    def event_name(cls) -> str:
        return "GUILD_BAN_REMOVE"

    def __repr__(self) -> str:
        return (
            f"<GuildBanRemoveEvent guild_id={self.guild_id!r} user={self.user!r}>"
        )
