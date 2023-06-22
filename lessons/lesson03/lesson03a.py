# Circuit Python Project 03 - Part 1
# Breadboard Wiring
#   Connect the 3V3 pin to a positive terminal on your breadboard
#   Connect one of the GND pins to the negative terminal on your breadboard
#   Connect GP15 to the Anode leg of a red LED
#   Connect a 220 ohm resistor to the Cathode leg of the LED and to the ground rail
#   Attach the slide switch across any three empty rows on the breadboard
#   Connect the top pin to the ground rail
#   Connect the middle pin to GP16
#   Connect the bottom pin to the positive rail
#
# Rename to code.py before loading onto Pico
#
# Import libraries
import board
import digitalio

# Define LED object
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

# Define switch object
switch = digitalio.DigitalInOut(board.GP16)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# Loop and test for switch state
while True:
    if switch.value:
        led.value = True
    else:
        led.value = False
