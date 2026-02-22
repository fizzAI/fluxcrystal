"""
Message model types.
"""

from __future__ import annotations

from typing import Any, TypedDict, TYPE_CHECKING
from copy import deepcopy

from fluxcrystal.models.users import User

if TYPE_CHECKING:
    from fluxcrystal.models.upload import Attachment

class MessageReference(TypedDict):
    type: int
    message_id: str
    channel_id: str

# FIXME: we really need to actually type the header, footer, etc but this is fine(?) for now
class EmbedField:
    __slots__ = ("name", "value", "inline")

    def __init__(self, data: dict[str, Any]) -> None:
        self.name: str = data["name"]
        self.value: str = data["value"]
        self.inline: bool = data.get("inline", False)

    def __repr__(self) -> str:
        return f"<EmbedField name={self.name!r} value={self.value!r} inline={self.inline!r}>"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, EmbedField):
            return (
                self.name == other.name
                and self.value == other.value
                and self.inline == other.inline
            )
        return NotImplemented

#FIXME: we really need to type everything else but tbh just fields is fine FOR NOW
class Embed:
    __slots__ = (
        "title",
        "type",
        "description",
        "url",
        "timestamp",
        "color",
        "footer",
        "image",
        "thumbnail",
        "video",
        "provider",
        "author",
        "fields"
    )

    def __init__(self, data: dict[str, Any]) -> None:
        self.title: str | None = data.get("title")
        self.type: str | None = data.get("type")
        self.description: str | None = data.get("description")
        self.url: str | None = data.get("url")
        self.timestamp: str | None = data.get("timestamp")
        self.color: int | None = data.get("color")
        self.footer: dict[str, Any] | None = data.get("footer")
        self.image: dict[str, Any] | None = data.get("image")
        self.thumbnail: dict[str, Any] | None = data.get("thumbnail")
        self.video: dict[str, Any] | None = data.get("video")
        self.provider: dict[str, Any] | None = data.get("provider")
        self.author: dict[str, Any] | None = data.get("author")
        self.fields: list[EmbedField] = [
            EmbedField(f) for f in data.get("fields", [])
        ]

    def __repr__(self) -> str:
        return f"<Embed title={self.title!r} description={self.description!r}>"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Embed):
            return (
                self.title == other.title
                and self.type == other.type
                and self.description == other.description
                and self.url == other.url
                and self.timestamp == other.timestamp
                and self.color == other.color
                and self.footer == other.footer
                and self.image == other.image
                and self.thumbnail == other.thumbnail
                and self.video == other.video
                and self.provider == other.provider
                and self.author == other.author
                and self.fields == other.fields
            )
        return NotImplemented

# FIXME: this is so fucking janky please save me from my suffering
class RichEmbed(Embed):
    def __init__(self) -> None:
        super().__init__({
            "type": "rich",
            "footer": {"text": "Made with `fluxcrystal`~ <3"}
        })
        self.type = "rich"

    @staticmethod
    def from_data(data: dict[str, Any]) -> "RichEmbed":
        """Create a RichEmbed from a data dictionary (for internal builder use)."""
        embed = object.__new__(RichEmbed)
        Embed.__init__(embed, data)
        embed.type = "rich"
        return embed

    def _copy_state(self) -> dict[str, Any]:
        """Create a copy of the current embed state for building a new instance."""
        return {
            "type": self.type,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "timestamp": self.timestamp,
            "color": self.color,
            "footer": self.footer.copy() if self.footer else None,
            "image": self.image.copy() if self.image else None,
            "thumbnail": self.thumbnail.copy() if self.thumbnail else None,
            "video": self.video.copy() if self.video else None,
            "provider": self.provider.copy() if self.provider else None,
            "author": self.author.copy() if self.author else None,
            "fields": [{"name": f.name, "value": f.value, "inline": f.inline} for f in self.fields],
        }

    def with_title(self, title: str) -> "RichEmbed":
        """Set the title of the embed."""
        state = self._copy_state()
        state["title"] = title
        return RichEmbed.from_data(state)

    def with_description(self, description: str) -> "RichEmbed":
        """Set the description of the embed."""
        state = self._copy_state()
        state["description"] = description
        return RichEmbed.from_data(state)

    def with_url(self, url: str) -> "RichEmbed":
        """Set the URL of the embed (makes the title clickable)."""
        state = self._copy_state()
        state["url"] = url
        return RichEmbed.from_data(state)

    def with_timestamp(self, timestamp: str) -> "RichEmbed":
        """Set the timestamp of the embed (ISO 8601 format)."""
        state = self._copy_state()
        state["timestamp"] = timestamp
        return RichEmbed.from_data(state)

    def with_color(self, color: int) -> "RichEmbed":
        """Set the color of the embed (decimal color value)."""
        state = self._copy_state()
        state["color"] = color
        return RichEmbed.from_data(state)

    def with_footer(self, text: str, icon_url: str | None = None) -> "RichEmbed":
        """Set the footer of the embed."""
        state = self._copy_state()
        state["footer"] = {"text": text, "icon_url": icon_url} if icon_url else {"text": text}
        return RichEmbed.from_data(state)

    def with_image(self, url: str, height: int | None = None, width: int | None = None) -> "RichEmbed":
        """Set the image of the embed."""
        state = self._copy_state()
        image_dict: dict[str, Any] = {"url": url}
        if height is not None:
            image_dict["height"] = height
        if width is not None:
            image_dict["width"] = width
        state["image"] = image_dict
        return RichEmbed.from_data(state)

    def with_thumbnail(self, url: str, height: int | None = None, width: int | None = None) -> "RichEmbed":
        """Set the thumbnail of the embed."""
        state = self._copy_state()
        thumb_dict: dict[str, Any] = {"url": url}
        if height is not None:
            thumb_dict["height"] = height
        if width is not None:
            thumb_dict["width"] = width
        state["thumbnail"] = thumb_dict
        return RichEmbed.from_data(state)

    def with_video(self, url: str, height: int | None = None, width: int | None = None) -> "RichEmbed":
        """Set the video of the embed."""
        state = self._copy_state()
        video_dict: dict[str, Any] = {"url": url}
        if height is not None:
            video_dict["height"] = height
        if width is not None:
            video_dict["width"] = width
        state["video"] = video_dict
        return RichEmbed.from_data(state)

    def with_provider(self, name: str | None = None, url: str | None = None) -> "RichEmbed":
        """Set the provider of the embed."""
        state = self._copy_state()
        provider_dict: dict[str, Any] = {}
        if name is not None:
            provider_dict["name"] = name
        if url is not None:
            provider_dict["url"] = url
        state["provider"] = provider_dict if provider_dict else None
        return RichEmbed.from_data(state)

    def with_author(self, name: str, url: str | None = None, icon_url: str | None = None) -> "RichEmbed":
        """Set the author of the embed."""
        state = self._copy_state()
        author_dict: dict[str, Any] = {"name": name}
        if url is not None:
            author_dict["url"] = url
        if icon_url is not None:
            author_dict["icon_url"] = icon_url
        state["author"] = author_dict
        return RichEmbed.from_data(state)

    def with_field(self, name: str, value: str, inline: bool = False) -> "RichEmbed":
        """Add a field to the embed."""
        state = self._copy_state()
        state["fields"] = state["fields"] + [{"name": name, "value": value, "inline": inline}]
        return RichEmbed.from_data(state)

    def with_fields(self, fields: list[dict[str, Any]]) -> "RichEmbed":
        """Set all fields of the embed (replaces existing fields)."""
        state = self._copy_state()
        state["fields"] = fields
        return RichEmbed.from_data(state)

    def clear_fields(self) -> "RichEmbed":
        """Clear all fields from the embed."""
        state = self._copy_state()
        state["fields"] = []
        return RichEmbed.from_data(state)

    def clear_author(self) -> "RichEmbed":
        """Clear the author from the embed."""
        state = self._copy_state()
        state["author"] = None
        return RichEmbed.from_data(state)

    def clear_footer(self) -> "RichEmbed":
        """Clear the footer from the embed."""
        state = self._copy_state()
        state["footer"] = None
        return RichEmbed.from_data(state)

    def clear_image(self) -> "RichEmbed":
        """Clear the image from the embed."""
        state = self._copy_state()
        state["image"] = None
        return RichEmbed.from_data(state)

    def clear_thumbnail(self) -> "RichEmbed":
        """Clear the thumbnail from the embed."""
        state = self._copy_state()
        state["thumbnail"] = None
        return RichEmbed.from_data(state)


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
        "attachments",
        "embeds",
    )

    def __init__(self, data: dict[str, Any]) -> None:
        from fluxcrystal.models.upload import Attachment
        
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
        self.attachments: list[Attachment] = [
            Attachment(a) for a in data.get("attachments", [])
        ]
        self.embeds: list[Embed] = [
            Embed(e) for e in data.get("embeds", [])
        ]

    @property
    def is_webhook(self) -> bool:
        """True if this message came from a webhook."""
        return self.webhook_id is not None
    
    def into_reply(self) -> MessageReference:
        """
        Returns a MessageReference of type REPLY for use
        with RESTClient.send_message to reply to
        the message that this Message represents
        """
        return {
            "type": 0,
            "message_id": self.id,
            "channel_id": self.channel_id,
        }
    
    def into_forward(self) -> MessageReference:
        """
        Returns a MessageReference of type FORWARD for use
        with RESTClient.send_message to forward
        the message that this Message represents
        to another channel
        """
        return {
            "type": 1,
            "message_id": self.id,
            "channel_id": self.channel_id,
        }

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
