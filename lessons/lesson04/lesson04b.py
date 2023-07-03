# Circuit Python Project 04 - buzzer (variant version with functions)
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

# define a function to play sounds according to supplied values


def soundoff(f, st1, st2):
    buzzer.frequency = f
    buzzer.duty_cycle = 65535 // 2
    time.sleep(st1)
    buzzer.duty_cycle = 0
    time.sleep(st2)


frequencies = (523, 392, 329, 220, 246, 223, 220)

# loop through notes pattern as designated by frequencies (f)
while True:
    for f in frequencies:
        soundoff(f, 0.25, 0.12)
        print("frequency :" + str(f))

# Code references from previous version of scripts
#    buzzer.frequency = 523
#    buzzer.duty_cycle = 65535 // 2
#    time.sleep(0.25)
#    buzzer.duty_cycle = 0
#    time.sleep(0.12)
#    for f in (523, 392, 329, 220, 246, 223, 220):
