from __future__ import annotations

import logging
from typing import Any

from fluxcrystal.models.channels import Channel
from fluxcrystal.models.guilds import Guild
from fluxcrystal.models.users import User

log = logging.getLogger("fluxcrystal.cache")


class Cache:
    """
    Caches guilds, channels, and users from the gateway.
    """

    def __init__(self) -> None:
        self.guilds: dict[str, Guild] = {}
        self.channels: dict[str, Channel] = {}
        self.users: dict[str, User] = {}
        self.me: User | None = None

    def get_guild(self, guild_id: str) -> Guild | None:
        """Grab a guild by ID, or None if we haven't seen it."""
        return self.guilds.get(guild_id)

    def get_channel(self, channel_id: str) -> Channel | None:
        """Grab a channel by ID, or None if we haven't seen it."""
        return self.channels.get(channel_id)

    def get_user(self, user_id: str) -> User | None:
        """Grab a user by ID, or None if we haven't seen them."""
        return self.users.get(user_id)

    def _update(self, event_name: str, data: dict[str, Any]) -> None:
        """
        Update the cache when gateway events come in.

        This fires *before* listeners get the event, so your handlers
        always see fresh data.
        """
        try:
            if event_name == "READY":
                self.me = User(data["user"])
                # Cache all guilds received in READY (they may be partial/unavailable)
                for guild_data in data.get("guilds", []):
                    gid = guild_data.get("id")
                    if gid:
                        # Unavailable guilds only have id + unavailable=True
                        if not guild_data.get("unavailable"):
                            try:
                                self.guilds[gid] = Guild(guild_data)
                            except Exception:
                                pass  # Partial data – skip

            elif event_name in ("GUILD_CREATE", "GUILD_UPDATE"):
                guild = Guild(data)
                self.guilds[guild.id] = guild
                # Cache channels sent with GUILD_CREATE
                for ch_data in data.get("channels", []):
                    ch_data.setdefault("guild_id", guild.id)
                    channel = Channel(ch_data)
                    self.channels[channel.id] = channel
                # Cache members sent with GUILD_CREATE
                for member_data in data.get("members", []):
                    user_data = member_data.get("user")
                    if user_data:
                        try:
                            user = User(user_data)
                            self.users[user.id] = user
                        except Exception:
                            pass

            elif event_name == "GUILD_DELETE":
                gid = data.get("id")
                if gid:
                    self.guilds.pop(gid, None)

            elif event_name in ("CHANNEL_CREATE", "CHANNEL_UPDATE"):
                channel = Channel(data)
                self.channels[channel.id] = channel

            elif event_name == "CHANNEL_DELETE":
                cid = data.get("id")
                if cid:
                    self.channels.pop(cid, None)

            elif event_name in ("MESSAGE_CREATE", "MESSAGE_UPDATE"):
                # Cache the author
                author_data = data.get("author")
                if author_data:
                    try:
                        user = User(author_data)
                        self.users[user.id] = user
                    except Exception:
                        pass

            elif event_name == "GUILD_MEMBER_ADD":
                user_data = data.get("user")
                if user_data:
                    try:
                        user = User(user_data)
                        self.users[user.id] = user
                    except Exception:
                        pass

            elif event_name == "GUILD_MEMBER_UPDATE":
                user_data = data.get("user")
                if user_data:
                    try:
                        user = User(user_data)
                        self.users[user.id] = user
                    except Exception:
                        pass

        except Exception:
            log.debug(
                "Cache update silently failed for event %r", event_name, exc_info=True
            )
