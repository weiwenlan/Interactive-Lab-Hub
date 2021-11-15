import time
import board
import busio
from adafruit_seesaw import seesaw, rotaryio, digitalio

import paho.mqtt.client as mqtt
import uuid

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/xt75/twiz_test/'

i2c = busio.I2C(board.SCL, board.SDA)


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






while True:
    position = -encoder.position

    if position != last_position:
        last_position = position
        val = f"Position: {position}"
        client.publish(topic, val)
        print("Position: {}".format(position))
    time.sleep(0.25)
    # if not button.value and not button_held:
    #     button_held = True
    #     print("Button pressed")

    # if button.value and button_held:
    #     button_held = False
    #     print("Button released")



    # for i in range(12):
    #     if mpr121[i].value:
    #     	val = f"Twizzler {i} touched!"
    #     	print(val)
    #     	client.publish(topic, val)
    # time.sleep(0.25)
