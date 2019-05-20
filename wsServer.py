#!/usr/bin/python3

import asyncio
import websockets
import socket
from sense_hat import SenseHat, ACTION_PRESSED

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localIp = s.getsockname()[0]

print('Local ip:', localIp)

sense = SenseHat()

gameInProgress = False

def middle_Click(event):
    global gameInProgress
    if event.direction == "middle" and event.action == ACTION_PRESSED:
        gameInProgress = not(gameInProgress)
        print("change; gameInProgress value:", gameInProgress)

sense.stick.direction_middle = middle_Click

async def main(websocket, path):
    # Logic inside this method
    global gameInProgress

    while True:
        event = sense.stick.wait_for_event()
        if event.direction == "middle":
            while gameInProgress:
                print("test")
                await asyncio.sleep(1)


start_server = websockets.serve(main, localIp, 12000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



