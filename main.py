import asyncio
import discord_integration
from hypercorn.asyncio import serve
from hypercorn.config import Config

import server

if __name__ == '__main__':
    discord_integration.start()
    asyncio.run(serve(server.app, Config()))
