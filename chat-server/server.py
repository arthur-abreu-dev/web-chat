import asyncio
import websockets

conections = set()
async def handler(websocket):
    conections.add(websocket)
    async for message in websocket:
        websockets.broadcast(conections, message)

async def main():
    async with websockets.serve(handler, "localhost", 8000):
        await asyncio.Future()  # run forever

asyncio.run(main())