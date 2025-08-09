import asyncio
from src.api.coins import websocket_client


async def main():
    await websocket_client()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
