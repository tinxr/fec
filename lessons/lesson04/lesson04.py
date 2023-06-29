# Circuit Python Project 04 - buzzer
# Breadboard Wiring
#   Connect the 3V3 pin to a positive terminal on your breadboard
#   Connect one of the GND pins to the negative terminal on your breadboard
#   Connect GP15 to the positive leg of the passive buzzer
#   Connect the negative leg of the passive buzzer to the ground rail
#
# Rename to code.py before loading onto Pico
#
# Import libraries
import board
import pwmio
import time

# Initialize a buzzer object via PWM
buzzer = pwmio.PWMOut(board.GP15, duty_cycle=0,
                      frequency=440, variable_frequency=True)

# loop through notes pattern as designated by frequencies (f)
while True:
    for f in (523, 392, 329, 220, 246, 223, 220):
        buzzer.frequency = f
        buzzer.duty_cycle = 65535 // 2  # On @ 50%
        time.sleep(0.25)
        buzzer.duty_cycle = 0  # Off
        time.sleep(0.25)
    time.sleep(0.5)
