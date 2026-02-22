# fluxcrystal

An async Python bot framework for [Fluxer](https://fluxer.app), (heavily) inspired by [hikari](https://github.com/hikari-py/hikari).

Support server at [fluxer.gg/tJwWDS4g](https://fluxer.gg/tJwWDS4g).

```python
import fluxcrystal

bot = fluxcrystal.GatewayBot("your-token-here")

@bot.listen()
async def on_message(event: fluxcrystal.MessageCreateEvent) -> None:
    if event.is_human and event.content == "!ping":
        _ = await bot.rest.create_message(event.channel_id, content="Pong! 🏓")

bot.run()
```

WIP~ 🩷

## License

LGPL 3.0