import paho.mqtt.client as mqtt
import uuid
from PIL import Image, ImageDraw, ImageFont
import board
import adafruit_rgb_display.st7789 as st7789
import os

import digitalio

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)

# ************************ init the screen *********************************
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000

spi = board.SPI()
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

height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90
draw = ImageDraw.Draw(image)
# ************************ end of init the screen *******************************





topic = 'IDD/xt75/door_bell/msg/'


def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(topic)

def on_message(cleint, userdata, msg):
    # if a message is recieved on the colors topic, parse it and set the color
    if msg.topic == topic:
        timer = msg.payload.decode('UTF-8')
        print(timer)
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((0,10),timer,font=font,fill="#FFAB4C")
        disp.image(image,rotation)

        if timer:
            os.system('espeak -ven+f2 -k5 -s150 --stdout  "Please wait for a moment" | aplay')

        # colors = list(map(int, msg.payload.decode('UTF-8').split(',')))
        # draw.rectangle((0, 0, width, height*0.5), fill=color)
        # disp.image(image)

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')
client.on_connect = on_connect
client.on_message = on_message

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

client.loop_forever()
