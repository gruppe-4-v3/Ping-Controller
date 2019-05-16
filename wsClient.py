#!/usr/bin/python3

import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:12000') as websocket:
        name = input("What's your name? ")
        
        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

async def counter():
    async with websockets.connect('ws://localhost:12000') as websocket:
        while True:
            number = await websocket.recv()
            print('Recived:', number.decode())

asyncio.get_event_loop().run_until_complete(counter())
