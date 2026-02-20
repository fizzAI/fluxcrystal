"""
Gateway lifecycle events (READY, RESUMED, etc.).
"""

from __future__ import annotations

from typing import Any

from fluxcrystal.events.base import Event
from fluxcrystal.models.users import User


class ReadyEvent(Event):
    """Fired when the bot has successfully connected and is ready to receive events."""

    __slots__ = ("user", "session_id", "resume_gateway_url")

    def __init__(self, app: Any, data: dict[str, Any]) -> None:
        super().__init__(app)
        self.user: User = User(data["user"])
        self.session_id: str = data.get("session_id", "")
        self.resume_gateway_url: str | None = data.get("resume_gateway_url")

    @classmethod
    def event_name(cls) -> str:
        return "READY"

    def __repr__(self) -> str:
        return f"<ReadyEvent user={self.user!r} session_id={self.session_id!r}>"
