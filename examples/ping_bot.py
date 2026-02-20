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
        _ = await bot.rest.create_message(event.channel_id, content="Pong! 🏓")

if __name__ == "__main__":
    bot.run()
