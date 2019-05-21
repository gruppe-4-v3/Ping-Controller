from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

gameInProgress = False

def middle_Click(event):
    global gameInProgress
    if event.action == "released":
        gameInProgress = not(gameInProgress)
        print("change; gameInProgress value:", gameInProgress)

sense.stick.direction_middle = middle_Click


while True:
    event = sense.stick.wait_for_event()

    while gameInProgress:
        print("test")
        sleep(1)