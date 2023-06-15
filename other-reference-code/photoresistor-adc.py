# CircuitPython Reference
# Raspberry Pi Pico W

# Import libraries
import time
import board
from analogio import AnalogIn

# Define the photoresistor
photor = AnalogIn(board.A0)


def analog_volts(creading, cref):
    # Function to convert analog value to voltage value
    return creading / 65535 * cref


# Main program exectuion
while True:
    volts = analog_volts(photor.value, photor.reference_voltage)
    print("Photoresitor reading: " + str(volts) + " volts")
    time.sleep(0.5)
