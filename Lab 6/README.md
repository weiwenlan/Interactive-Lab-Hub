# Little Interactions Everywhere

## Lab Partners
For this Lab, we are a team of 3 people.

```
- Xingyu Tao (xt75)
- Wenlan Wei (ww367)
- Jiacheng Peng (jp948)
```


1. Pull the new changes from the class interactive-lab-hub. (You should be familiar with this already!)
2. Install [MQTT Explorer](http://mqtt-explorer.com/) on your laptop.
3. Readings before class:
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Overview

The point of this lab is to introduce you to distributed interaction. We have included some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects if wanted. However, we want to emphasize that the grading will focus on your ability to develop interesting uses for messaging across distributed devices. Here are the four sections of the lab activity:

A) [MQTT](#part-a)

B) [Send and Receive on your Pi](#part-b)

C) [Streaming a Sensor](#part-c)

D) [The One True ColorNet](#part-d)

E) [Make It Your Own](#part-)

## Part 1.

### Part A
### MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of [Internet of Things (IoT)](https://en.wikipedia.org/wiki/Internet_of_things) devices. 

#### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`. Imagine that the Broker is the messaging center!
* **Client** - A device that subscribes or publishes information to/on the network.
* **Topic** - The location data gets published to. These are *hierarchical with subtopics*. For example, If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. With this setup, the info/updates of the sidelamp's `light_status` and `voltage` will be store in the subtopics. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on the topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe. Following the previouse example of home IoT smart bulbs, subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage.
* **Publish** - This is a way of sending messages to a topic. Again, with the previouse example, you can set up your IoT smart bulbs to publish info/updates to the topic or subtopic. Also, note that you can publish to topics you do not subscribe to. 


**Important note:** With the broker we set up for the class, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`. Also, setting up a broker is not much work, but for the purposes of this class, you should all use the broker we have set up for you!


#### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.


![input settings](imgs/mqtt_explorer.png?raw=true)


Once connected, you should be able to see all the messages under the IDD topic. , go to the **Publish** tab and try publish something! From the interface you can send and plot messages as well. Remember, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`.

![publish settings](imgs/mqtt_explorer_2.png?raw=true)

### Testing MQTT Publishing
<img src="https://user-images.githubusercontent.com/14202464/141701278-d24d42ee-9bcd-4277-a36c-67cf81b80708.PNG" width="600">


### Part B
### Send and Receive on your Pi

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python. Let's spend a few minutes running these and seeing how messages are transferred and shown up. Before working on your Pi, keep the connection of `farlab.infosci.cornell.edu/8883` with MQTT Explorer running on your laptop.

**Running Examples on Pi**

* Install the packages from `requirements.txt` under a virtual environment, we will continue to use the `circuitpython` environment we setup earlier this semester:
  ```
  pi@ixe00:~ $ source circuitpython/bin/activate
  (circuitpython) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 6
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ pip install -r requirements.txt
  ```
* Run `sender.py`, fill in a topic name (should start with `IDD/`), then start sending messages. You should be able to see them on MQTT Explorer.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python sender.py
  pi@ReiIDDPi:~/Interactive-Lab-Hub/Lab 6 $ python sender.py
  >> topic: IDD/ReiTesting
  now writing to topic IDD/ReiTesting
  type new-topic to swich topics
  >> message: testtesttest
  ...
  ```
* Run `reader.py`, and you should see any messages being published to `IDD/` subtopics.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python reader.py
  ...
  ```

**\*\*\*Consider how you might use this messaging system on interactive devices, and draw/write down 5 ideas here.\*\*\***

1. We can use it to send the moisture level information for monitoring differernt plants, and use it to create a smart plant watering system. They key function is that when the moisture level of all the plants are below certain level, the system initiates and starts watering all the plants.
2. We can use it for smart furniture. You can turn the bathroom's light on and off when you are in the bedroom.
3. We can use it on the door bell. When the door bell rings, the messges could be sent to other device in the home, for example the TV, the lights.
4. We can use the speech to text algorithm along with the message function to create a voice controlling system to control electronics like lights.
5. We can use the text to speech algorithm along with the message funciton to read emails for you.

### Part C
### Streaming a Sensor

We have included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Fall2021/Lab%204) that streams the [capacitor sensor](https://learn.adafruit.com/adafruit-mpr121-gator) inputs over MQTT. We will also be running this example under `circuitpython` virtual environment.

Plug in the capacitive sensor board with the Qwiic connector. Use the alligator clips to connect a Twizzler (or any other things you used back in Lab 4) and run the example script:

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
<img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150"/>
<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" height="150">
</p>

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python distributed_twizzlers_sender.py
 ...
 ```

**\*\*\*Include a picture of your setup here: what did you see on MQTT Explorer?\*\*\***

#### Capacitive Sensor Setup
<img src="https://user-images.githubusercontent.com/14202464/141701372-004122a3-bebe-49a8-8194-657d1a20ed73.jpg" width="600">

#### MQTT Response
<img width="1136" alt="twizzler_test_2" src="https://user-images.githubusercontent.com/14202464/141701414-e6165fd1-16f5-48d3-944c-022d328c4b4a.png" width="600">

**\*\*\*Pick another part in your kit and try to implement the data streaming with it.\*\*\***

#### Rotatry Sensor Setup
<img src="https://user-images.githubusercontent.com/14202464/141701540-51df236f-1444-4783-a424-0eb4650efc5c.jpg" width="600">

#### MQTT Response
<img src="https://user-images.githubusercontent.com/14202464/141701598-9e584c40-d38c-4c81-9e4f-c3ef8c459410.PNG" width="600">

### Part D
### The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB, we too can find unity in our heart, minds and souls. With the help of machines, we can overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [MiniPiTFT Display](https://www.adafruit.com/product/4393). You are almost there!

<p float="left">
  <img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
  <img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
  <img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="150">
</p>


The second step to achieving our great enlightenment is to run `color.py`. We have talked about this sensor back in Lab 2 and Lab 4, this script is similar to what you have done before! Remember to ativate the `circuitpython` virtual environment you have been using during this semester before running the script:

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python color.py
 ...
 ```

By running the script, wou will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one.

(A message from the previous TA, Ilan: I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also, I haven't load-tested it so things might just immediately break when everyone pushes the button at once.)

You may ask "but what if I missed class?" Am I not admitted into the collective enlightenment of the *OneColor*?

Of course not! You can go to [https://one-true-colornet.glitch.me/](https://one-true-colornet.glitch.me/) and become one with the ColorNet on the inter-webs. Glitch is a great tool for prototyping sites, interfaces and web-apps that's worth taking some time to get familiar with if you have a chance. Its not super pertinent for the class but good to know either way. 

**\*\*\*Can you set up the script that can read the color anyone else publish and display it on your screen?\*\*\***

#### Colors Universal Receiver
We set up a script that would receive all the colors output from different users by modifying the `reader.py` file into a version called `color_reader.py` where it would display all color values that are streamed to the channel topic `IDD/colors`. This way by running `python color_reader.py` we can read all the different color values being read in different Raspberry Pis.

<img src="https://user-images.githubusercontent.com/14202464/141701687-2d7a79bd-94a8-43fa-93d8-45c07744d421.PNG" width="600">


### Part E
### Make it your own

Find at least one class (more are okay) partner, and design a distributed application together based on the exercise we asked you to do in this lab.

**\*\*\*1. Explain your design\*\*\*** <br>
Our design is called the “Omnipresent Doorbell”. The basic idea is that when the door bell being hit, people in the house that is not close to the door might not hear the sound. The device in other rooms could receive the message sent by the door bell and act simultaneously. For example, when the doorbell rings, the speaker in the bathroom will generate a sound to notify the people there are someone coming. And in the study room, because people in the study room are studying or having a meeting, which they do not like to be disrupted by a sound. The light in the study would room flash as the doorbell being hit. This is a more gentle approach to notify the user that someone is coming. And the people in the house could hit a button to confirm that they accquired the fact that someone is outside. After the button being hit, the doorbell will play a voice saying that the hsot have being notified. The “Omnipresent Doorbell” will solve the problem missing the sound of doorbell and make sure you got notified when someone hit the doorbell. <br>

**\*\*\*2. Diagram the architecture of the system.\*\*\*** <br>
Input: When the doorbell is being hit, it will get the input from the button that being hit. <br>
Output: The out put will be the sound generated from the speaker at the bathroom, and the flashing light being generated at the study room. <br>
Computation: The pi connect to the doorbell is the sender. When it the doorbell being hit, it will send a message in the channel to all the receivers. The pi at the bathroom and the study room are the receivers. They will play sound/ flash lights when they receive the message from the doorbell. The receivers also have a button. The people in the room could hit the button, and the receivers will send a message to the doorbell, the doorbell would generate a voice to indicate the guest that the host has being notified. <br>
![806346247209795563](https://user-images.githubusercontent.com/39228801/141711221-4af236ff-d09e-4356-97c4-3208e7bb26e2.jpg)

**\*\*\*3. Build a working prototype of the system.\*\*\*** <br>
The user interface and user interaction is intuitive and straight forward. All the interaction are based on a very common interaction ---- hit the doorbell. The guest are just doing what they normally do. And when the host confirmed their presence, the doorbell will play a voice notify the guest. Since the voice is a speech, there will no obstacles for the guest to understand at all. For the host side, since he/she is the one who uses the system, they are expected to understand the whole system. <br>

**\*\*\*4. Document the working prototype in use.\*\*\*** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.

[![1636935813](https://user-images.githubusercontent.com/39228801/141705107-ef2e7b49-6bd8-4541-9ec5-4102d4ca4f25.png)](https://www.youtube.com/watch?v=wy4fX0s_vVo)

### User Testing <br>
We’ve asked three people to test our product, below are the feedbacks they give us.<br>
1.	Could build a talking channel let the guest and host talk directly through the doorbell.<br>
2.	Let the light in the study room changed color from green to red if the guest pushed the doorbell consistently to indicate they have emergencies.<br>
3.	Can apply the speech to text, to let the guest talk to the doorbell and convert it into message to be sent to the host.<br>

<!--**\*\*\*5. BONUS (Wendy didn't approve this so you should probably ignore it)\*\*\*** get the whole class to run your code and make your distributed system BIGGER.-->
