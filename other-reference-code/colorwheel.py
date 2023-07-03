# 2023-07-03
# Source: https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel
# Simple CircuitPython Neopixel example
# requires neopixel.mpy from Adafruit library be included in device lib folder

import time
import board
from rainbowio import colorwheel
import neopixel

pixel_pin = board.NEOPIXEL
num_pixels = 1

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)
        
while True:
    # adjust value below to increase delay in color transitions
    rainbow_cycle(0.05)