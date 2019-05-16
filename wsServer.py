#!/usr/bin/python3

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

async def counter(websocket, path):
    count = 0
    while True:
        await websocket.send(str(count).encode())
        await asyncio.sleep(1)
        count = count + 1


start_server = websockets.serve(counter, 'localhost', 12000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

