import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

servo = kit.servo[7]

servo.set_pulse_width_range(500,2500)

servo.angle = 60
time.sleep(2)

servo.angle = 15

time.sleep(10)


servo.angle = 60
time.sleep(2)