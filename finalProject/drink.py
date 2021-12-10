import time
from adafruit_servokit import ServoKit
import sys

para = sys.argv

para[1]=int(para[1])
para[2]=int(para[2])

mot_dic = {1:15,2:7,3:3}

kit = ServoKit(channels=16)

servo = kit.servo[mot_dic[para[1]]]
if para[1]==1:
    start = 60
    end = 30
elif para[1]==2:
    start = 60
    end = 20
elif para[1] ==3:
    start =60 
    end = 15



servo.set_pulse_width_range(500,2500)

servo.angle = start
time.sleep(2)

servo.angle = end

time.sleep(para[2])


servo.angle = start
time.sleep(2)
