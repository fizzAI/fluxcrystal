import logging
import os

from dotenv import load_dotenv

import fluxcrystal

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = fluxcrystal.GatewayBot(os.environ["FLUXER_TOKEN"])

# the event you listen for is implied by the type annotation!
@bot.listen()
async def on_ready(event: fluxcrystal.ReadyEvent) -> None:
    print(f"Logged in as {event.user.username}#{event.user.discriminator}")
    print(f"Cached {len(bot.cache.guilds)} guild(s)")


# alternatively, explicitly listen for event in the decorator
@bot.listen(fluxcrystal.MessageCreateEvent)
async def on_message(event: fluxcrystal.MessageCreateEvent):
    if not event.is_human:
        return
    if event.content == "!ping":
        _ = await bot.rest.create_message(
            event.channel_id,
            content="Pong! 🏓",
            message_reference=event.message.into_reply()
        )
    if event.content == "!forward":
        _ = await bot.rest.create_message(
            event.channel_id,
            message_reference=event.message.into_forward()
        )
    if event.content == "!embed":
        embed = (
            fluxcrystal.RichEmbed()
            .with_title("Hello from fluxcrystal!")
            .with_description("This is an embed sent from the ping bot example.")
            .with_color(0x7289DA)  # blurple color
            .with_author("Ping Bot", icon_url="https://i.imgur.com/AfFp7pu.png")
            .with_field("Field 1", "Some value", inline=True)
            .with_field("Field 2", "Another value", inline=True)
            .with_field("Field 3", "More info here", inline=False)
            .with_footer("Footer text here")
        )
        _ = await bot.rest.create_message(
            event.channel_id,
            content="Here is your embed:",
            embeds=[embed]
        )

if __name__ == "__main__":
    bot.run()
