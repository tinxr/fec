# Circuit Python Project 01
# Breadboard Wiring
#   GND to ground (-) rail of breadboard
#   GP20 - Cathode leg of Red LED
#   Anode leg to 220R resistor
#   220R to ground (-) rail
#
# Rename to code.py before loading onto Pico
#
# Import libraries
import board
import digitalio
import time

# Initialize variables
sleepTime = 0.75 # controls duration of sleep between blinks

# Initialize LED (connected to GP20) object and set direction
led = digitalio.DigitalInOut(board.GP20)
led.direction = digitalio.Direction.OUTPUT

# Loop infinitely and alter LED state with sleep between state changes
while True:
    led.value = True
    time.sleep(sleepTime)
    led.value = False
    time.sleep(sleepTime)