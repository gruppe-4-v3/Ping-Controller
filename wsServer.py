#!/usr/bin/python3

import asyncio
import websockets
import socket
from sense_hat import SenseHat, ACTION_PRESSED
from time import sleep

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
    global sense

    while True:
        sense.stick.wait_for_event()
        sleep(.5)

        speed = 0
        red = (255, 0, 0)

        while gameInProgress:
            acceleration = sense.get_accelerometer_raw()
            x = acceleration['x']
            
            speed *= 0.9
        
            if (x > 0.1 or x < -0.1):
                speed += x
            
            print("speed:", speed)
            websocket.send(speed)

            sense.clear()
            if (speed > 0.5 and speed < 1):
                sense.set_pixel(2, 5, red)
            if (speed > 1 and speed < 2):
                sense.set_pixel(1, 5, red)
            if (speed > 2):
                sense.set_pixel(0, 5, red)
            if (speed < -0.5 and speed > -1):
                sense.set_pixel(5, 5, red)
            if (speed < -1 and speed > -2):
                sense.set_pixel(6, 5, red)
            if (speed < -2):
                sense.set_pixel(7, 5, red)
            if (speed < 0.5 and speed > -0.5):
                sense.set_pixel(4, 5, red)
                sense.set_pixel(3, 5, red)


start_server = websockets.serve(main, localIp, 12000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



