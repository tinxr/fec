# Circuit Python Project 02
# Breadboard Wiring
#   GND to ground (-) rail of breadboard
#   VBUS to positive (+) rail of breadboard
#   Black wire from ground (-) rail to brown servo connector
#   Red wire from positive (+) rail to red servo connector
#   Blue wire from GP16 to orange servo connector
#   Black wire from GND to the 3rd pin of the pot
#   White wire from GP20/A0 to the middle pin of the pot
#   Red wire from 3v3 to the 1st pin of the pot
# Rename to code.py before loading onto Pico
# From the Adafruit v8 bundle copy adafruit_motor to the lib folder on the Pico Ws
#
# Import libraries
import time
import board
import pwmio
from adafruit_motor import servo
from analogio import AnalogIn

# Create a PWM object and myServo for operating device (connected via GP16)
pwm = pwmio.PWMOut(board.GP16, duty_cycle=2 ** 15, frequency=50)
myServo = servo.Servo(pwm)

# Create a potentiometer ("pot") object
potentiometer = AnalogIn(board.A0)

# Loop while reading the value of the pot and adjusting the servo with
# a short sleep to keep movements fluid
while True:
    angle = (potentiometer.value * 180 / 65535)
    myServo.angle = angle
    time.sleep(0.05)
