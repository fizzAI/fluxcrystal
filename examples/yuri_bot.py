"""
Yuri bot - showcases the attachments system with images from Safebooru (SFW).

This bot demonstrates how to upload images as message attachments using
the fluxcrystal framework's AttachmentUpload system.
"""

import logging
import os
import random

import httpx
from dotenv import load_dotenv

import fluxcrystal

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = fluxcrystal.GatewayBot(os.environ["FLUXER_TOKEN"])

# Safebooru API configuration
SAFEBOORU_API_URL = "https://safebooru.org/index.php"
YURI_TAG = "yuri"

# MIME type mapping for common image extensions
CONTENT_TYPE_MAP = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".gif": "image/gif",
    ".webp": "image/webp",
    ".bmp": "image/bmp",
}


def get_content_type(filename: str) -> str:
    """Get the MIME content type based on file extension."""
    ext = os.path.splitext(filename)[1].lower()
    return CONTENT_TYPE_MAP.get(ext, "application/octet-stream")


async def fetch_yuri_image() -> tuple[bytes, str] | None:
    """
    Fetch a random yuri image from Safebooru.
    
    Returns:
        Tuple of (image_bytes, filename) or None if no image found
    """
    async with httpx.AsyncClient(timeout=30.0) as client:
        params = {
            "page": "dapi",
            "s": "post",
            "q": "index",
            "json": "1",
            "tags": YURI_TAG,
            "limit": "100",
        }
        
        try:
            response = await client.get(SAFEBOORU_API_URL, params=params)
            response.raise_for_status()
            posts = response.json()
            
            if not posts or not isinstance(posts, list):
                return None
            
            post = random.choice(posts)
            
            image_dir = str(post.get("directory", ""))
            image_hash = str(post.get("image", ""))
            
            if not image_hash:
                return None
            
            image_url = f"https://safebooru.org/images/{image_dir}/{image_hash}"
            
            image_response = await client.get(image_url)
            image_response.raise_for_status()
            
            original_filename = post.get("image", "yuri_image")
            filename = f"yuri_{post.get('id', 'unknown')}.{original_filename.split('.')[-1]}"
            
            return image_response.content, filename
            
        except Exception as e:
            logging.error(f"Error fetching yuri image: {e}")
            return None


@bot.listen()
async def on_ready(event: fluxcrystal.ReadyEvent) -> None:
    print(f"Logged in as {event.user.username}#{event.user.discriminator}")
    print(f"Cached {len(bot.cache.guilds)} guild(s)")
    print("Yuri bot is ready! Use !yuri to get yuri images")


@bot.listen(fluxcrystal.MessageCreateEvent)
async def on_message(event: fluxcrystal.MessageCreateEvent):
    if not event.is_human:
        return
    
    if event.content == "!yuri":
        await bot.rest.send_typing(event.channel_id)
        
        image_data = await fetch_yuri_image()
        
        if image_data is None:
            await bot.rest.create_message(
                event.channel_id,
                content="Sorry, I couldn't find a yuri image right now!",
            )
            return
        
        image_bytes, filename = image_data
        
        # Get the content type based on file extension
        content_type = get_content_type(filename)
        
        # Create an AttachmentUpload with the image data and content_type
        attachment = fluxcrystal.AttachmentUpload(
            content=image_bytes,
            filename=filename,
            content_type=content_type,
            description=f"Yuri image from Safebooru - {filename}",
        )
        
        await bot.rest.create_message(
            event.channel_id,
            content="Here's some yuri for you! 💕",
            attachments=[attachment],
        )
    
    elif event.content == "!help":
        await bot.rest.create_message(
            event.channel_id,
            content="""**Yuri Bot Commands:**
- `!yuri` - Get a random yuri image from Safebooru
- `!help` - Show this help message

This bot showcases the attachments system by uploading images directly to Discord!""",
        )


if __name__ == "__main__":
    bot.run()
