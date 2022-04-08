import discord_integration
import asyncio
import server
from hypercorn.config import Config
from hypercorn.asyncio import serve


if __name__ == '__main__':
    asyncio.run(serve(server.app, Config()))
    # discord_integration.start()
