# Import libraries
import board
import analogio
import digitalio
import time

# Initialize our component objects
led1 = digitalio.DigitalInOut(board.GP14)
led2 = digitalio.DigitalInOut(board.GP15)
led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
cell = analogio.AnalogIn(board.A0)

diff_value = 32000

# let's loop a few times and read values while blocking some light
while True:
    print("Photocell value: " + str(cell.value))
    if int(cell.value) > diff_value:
        led1.value = True
        led2.value = False
    else:
        led2.value = True
        led1.value = False
    time.sleep(0.5)
