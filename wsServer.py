#!/usr/bin/python3

import asyncio
import websockets
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localIp = s.getsockname()[0]

print('Local ip:', localIp)

async def main(websocket, path):
    # Logic inside this method
    count = 0
    while True:
        await websocket.send(str(count))
        await asyncio.sleep(1)
        count = count + 1


start_server = websockets.serve(main, localIp, 12000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



