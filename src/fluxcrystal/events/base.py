"""
Base event type for all fluxcrystal events.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Event(ABC):
    """
    Base class for all gateway events.

    All events carry a reference to the `fluxcrystal.GatewayBot`
    that received them, accessible via the `app` attribute.
    """

    __slots__ = ("app",)

    #: The `fluxcrystal.GatewayBot` instance this event belongs to.
    app: Any

    def __init__(self, app: Any, data: dict[str, Any] | None = None) -> None:
        self.app = app

    @classmethod
    @abstractmethod
    def event_name(cls) -> str:
        """
        The gateway dispatch event name this event corresponds to (ie `"MESSAGE_CREATE"`).
        """
