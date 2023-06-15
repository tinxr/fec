# Circuit Python Project 02
# Breadboard Wiring
#   GND to ground (-) rail of breadboard
#   VBUS to positive (+) rail of breadboard
#   Black wire from ground (-) rail to brown servo connector
#   Red wire from positive (+) rail to red servo connector
#   Blue wire from GP16 to orange servo connector
#
# Rename to code.py before loading onto Pico
# From the Adafruit v8 bundle copy adafruit_motor to the lib folder on the Pico Ws
#
# Import libraries
import time
import board
import pwmio
from adafruit_motor import servo

# Create a PWM object and myServo for operating device (connected via GP16)
pwm = pwmio.PWMOut(board.GP16, duty_cycle=2 ** 15, frequency=50)
myServo = servo.Servo(pwm)

# Loop over a range of sweeping positions with a short sleep to keep movements fluid
while True:
    for angle in range(0, 180, 5):
        myServo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5):
        myServo.angle = angle
        time.sleep(0.05)
