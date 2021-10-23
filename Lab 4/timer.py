# SPDX-FileCopyrightText: 2021 John Furcean
# SPDX-License-Identifier: MIT

"""I2C rotary encoder simple test example."""

import board
from adafruit_seesaw import seesaw, rotaryio, digitalio
import time
import subprocess
#import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# For use with the STEMMA connector on QT Py RP2040
# import busio
# i2c = busio.I2C(board.SCL1, board.SDA1)
# seesaw = seesaw.Seesaw(i2c, 0x36)

# code for encoder
seesaw = seesaw.Seesaw(board.I2C(), addr=0x36)

seesaw_product = (seesaw.get_version() >> 16) & 0xFFFF
print("Found product {}".format(seesaw_product))
if seesaw_product != 4991:
    print("Wrong firmware loaded?  Expected 4991")

seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
button = digitalio.DigitalIO(seesaw, 24)
button_held = False

encoder = rotaryio.IncrementalEncoder(seesaw)
last_position = None
    
# code for display
# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
import digitalio
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys
import json

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 80)

font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# code the actual timer
def startTimer(position):
    t = int(position)
    while t:
        mins, secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((0,10),timer,font=font,fill="#D8E9A8")
        
        disp.image(image,rotation)
        print(timer,end="\r")
        if mpr121[1].value:
            os.system('espeak -ven+f2 -k5 -s150 --stdout  "Timer Stop" | aplay')
            while True:
                if mpr121[4].value:
                    os.system('espeak -ven+f2 -k5 -s150 --stdout  "Timer Start" | aplay')
                    break
                time.sleep(0.2)
 
        time.sleep(1)
        t-=1
    if t==0:
        timer = 'TIME IS UP'

        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((10,40),timer,font=font2,fill="#4E9F3D")
        
        disp.image(image,rotation)
        os.system('espeak -ven+f2 -k5 -s150 --stdout  "Time is up" | aplay')
    print("Time up!!")

import busio
import adafruit_mpr121
from adafruit_apds9960.apds9960 import APDS9960

# sensor - proximity
i2c1 = board.I2C()
apds = APDS9960(i2c1)
apds.enable_proximity = True

# sensor - capacitance touch
i2c2 = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c2)

# constants
HAND_DISTANCE_CLOSE = 10
PAUSE_BUTTON = 1
START_BUTTON = 4

# sensor values

#CUR_TIME = time.strftime("%H:%M:%S")
#PROXIMITY = 100
last_time_position = 0
while True:
    timer = 'WAITING'

    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((10,40),timer,font=font2,fill="#4E9F3D")
    
    disp.image(image,rotation)
    PROXIMITY = apds.proximity
    print(PROXIMITY)
    if PROXIMITY > HAND_DISTANCE_CLOSE:
        #print("Hand is close! " + CUR_TIME)
        timer = 'START TIMER'

        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((10,40),timer,font=font2,fill="#4E9F3D")
        
        disp.image(image,rotation)
        init_position = -encoder.position 
        # controller
        while True:
            
            # negate the position to make clockwise rotation positive
            position = -encoder.position-init_position
            if position != last_position:
                last_position = position
                mins, secs = divmod(last_position,60)
                timer = '{:02d}:{:02d}'.format(mins,secs)
                
                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                draw.text((0,10),timer,font=font,fill="#D8E9A8")
                
                disp.image(image,rotation)

                print("Position: {}".format(position))

            if not button.value and not button_held:
                button_held = True
                startTimer(position)
                last_time_position = position
                break
                # print("Button pressed")
            if mpr121[4].value:

                os.system('espeak -ven+f2 -k5 -s150 --stdout  "Timer Start" | aplay')
                startTimer(position)
                break
                # print("Button pressed")
           
            if button.value and button_held:
                button_held = False
                # print("Button released")
            
            
    
    # sleep time
    time.sleep(0.2)


