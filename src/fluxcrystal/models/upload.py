"""
Upload and attachment model types.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypedDict, NotRequired

if TYPE_CHECKING:
    from fluxcrystal.models.users import User


class AttachmentUpload:
    """An attachment to upload to Discord."""

    def __init__(
        self,
        content: str | bytes,
        *,
        filename: str | None = None,
        title: str | None = None,
        description: str | None = None,
        content_type: str | None = None,
    ) -> None:
        self.content = content
        self.filename = filename
        self.title = title
        self.description = description
        self.content_type = content_type

    def __repr__(self) -> str:
        return f"<AttachmentUpload filename={self.filename!r}>"


class Attachment:
    """A file attached to a message."""

    __slots__ = (
        "id",
        "filename",
        "title",
        "description",
        "content_type",
        "size",
        "url",
        "proxy_url",
        "width",
        "height",
        "ephemeral",
    )

    def __init__(self, data: dict[str, Any]) -> None:
        self.id: str = data["id"]
        self.filename: str = data["filename"]
        self.title: str | None = data.get("title")
        self.description: str | None = data.get("description")
        self.content_type: str | None = data.get("content_type")
        self.size: int = data.get("size", 0)
        self.url: str = data["url"]
        self.proxy_url: str | None = data.get("proxy_url")
        self.width: int | None = data.get("width")
        self.height: int | None = data.get("height")
        self.ephemeral: bool = data.get("ephemeral", False)

    @property
    def is_image(self) -> bool:
        """Check if the attachment is an image."""
        if self.content_type:
            return self.content_type.startswith("image/")
        return False

    @property
    def is_video(self) -> bool:
        """Check if the attachment is a video."""
        if self.content_type:
            return self.content_type.startswith("video/")
        return False

    def __repr__(self) -> str:
        return f"<Attachment id={self.id!r} filename={self.filename!r} size={self.size}>"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Attachment):
            return self.id == other.id
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.id)
