# Drinkser 

![IMG_0381](https://user-images.githubusercontent.com/39228801/145053162-31a25fd9-dfc3-4644-8245-2f63b4ebcae6.jpg)


## IDD Final Project

Team Member: <br>
Jiacheng Peng (jp948)<br>
Wenlan Wei (ww367)<br>
Xingyu Tao (xt75)<br>

## Project Overview

Our project is called Drinkser, it is a cocktail dispenr that automatically mix differernt alcohol or drinks for you. All you have to do is place your empty bottle in front the machine, and press the drink you would like to have on the touch screen. Drinkser will make the drink for you.

## How to use it
First, place your empty cup under the tap in fornt of the machine. There will be selections of different cocktails/drinks shown on the touch screen. You will make your selection, and the machine will suck the liquid needed from the side to make your drink. 

## Parts needed
Raspberry pi 4 <br>
12V pumps <br> 
thing silicon tubing <br>
touch screen for Raspberry pi <br>
motors <br>
bread board <br>
battery box <br>
motor controller <br>


## Project Plan
Below is our original plan for the project
### Big idea
Introducing Drinkser, a smart Cocktail dispenser. This interactive device will allow users
to use a touchscreen to dispense different kinds of mixed drinks. The device will have a
box-like body with an inset concave area for drink dispensing. The main touchscreen on
the front side of the device will let users choose between drinks and also prompt the
user to place their cup in the dispensing area once they have made their choice.
Once the cup is placed in the dispensing area a distance sensing chip at the bottom will
detect the cup and start dispensing. Since the pump works at a constant rate (about
500ml per 6 min), we can control the dispensed amount simply by controlling the time of
the dispensing. Depending on the drink the user chose, different silicone tubing pumps
will activate and allow the dispensed liquids to mix in the cup. Once the dispensing is
complete, the LED strip on the top of the dispensing area and the touchscreen will
prompt the user to remove their cup.

### Timeline
Nov 23 Buy the additional parts once our idea gets approved <br>
Nov 28 Finish implementing the code for the pump and start working on the
physical<br>
Dec 2 Functional check off<br>
Dec 5 Finish building the physical part of the prototype, start implementing the<br>
code for touch screen<br>
Dec 11 Add the touch screen to our prototype<br>
Dec 12 Wrap things up and finish all the documentation<br>
Dec 13 Final deliverable<br>

### Risks / Contingencies
● The flux for the pump might be too small. We will use multiple pumps if
necessary.<br>
● We might not be able to build a working touch screen. We will use physical
buttons like capacity sensors instead.<br>
● We need more thought on how to refill the drinks being dispensed once they are
empty. We will need to design this part carefully if we want the device to be
refillable.<br>

### Fall Back plan
If the pump does not work as we expected, we will use a motor to tilt the bottle of the
alcohol to perform the same function. We will use a smaller bottle or even a cup for
tilting since our motor only has 9g of power.
## Design
Below is a picture of the general idea. <br>
<img width="884" alt="Screen Shot 2021-12-07 at 12 21 17 AM" src="https://user-images.githubusercontent.com/39228801/144971227-61becb18-6140-469d-b94d-5ad33fcb45e4.png">

## Demo
Below is a link to a demo video of the working prototype. <br>
[<img width="1138" alt="Screen Shot 2021-12-07 at 10 35 28 AM" src="https://user-images.githubusercontent.com/39228801/145059752-b644615d-5fc9-470c-9ce9-645721a4bf6c.png">](https://www.youtube.com/watch?v=HgxsOgSMFxE)

Take a look of the inside! Below is a video for how the products operates without the packaging.
[<img width="1162" alt="Screen Shot 2021-12-11 at 3 16 37 PM" src="https://user-images.githubusercontent.com/39228801/145690428-b295f16f-fe48-45e2-8d03-4c1dd6583111.png">](https://www.youtube.com/watch?v=8xsTz74DtQU&ab_channel=JiachengPeng)

## Design Process

We've compared our design with the mature product in the market. Through our prototype may look a little unpolished, but we've got our advantages.<br>
Below is a electric cocktail dispenser from the market.<br>
<img src="https://user-images.githubusercontent.com/39228801/145688724-1db57e4a-a896-4137-9f3d-e8462d0b6588.png" width="500">
<img src="https://user-images.githubusercontent.com/39228801/145688888-6ba47667-40b8-4a0a-93fe-6f444eae1498.png" width="500">
The basic idea is the same -- Using pumps to draw the drink from the bottle and dispense it from the tap on the other side. This product is making the dispencing button a manual control. It is more like a soda machine that in a fast food resturant than a real cocktail maker. Our product, however, using a touch screen that makes the product more convenient and robust.<br>
1. We pre-programed the scale for making different drinks by control the time the pump works. So that a novel user would be able to make the perfect drinks.
2. The touch screen could show pictures for differnt drinks so the UI is more intuitive.
3. We could easily adjust the selections of the drink by just reprogramming the system. For example, adding holiday special drinks for certain holidays.
4. The selections range could be easily expaned by adding more pumps in the product.

We've also identified some futher features that could be added to the product.<br>
1. Make user interface that allow the user to adujst the scale of drink which allows them to make their own personal drinks. They could even name the drink if they would like to.
2. Using a light sensor to detect if the cup is being placed on the correct place. If the bottle is not being placed, they dispenser would not start despencing to prevent a mis touch.
3. Adding a camera and suing computer vision to detect if the cup is full. If the cup is full and can not take more drinks, the dispenser would automatically stop dispencing to prevent the spill.

When we first start thinking about this idea, we were thinking about using motors to control the lid of a bottle for dispensing the drinks. But we found this is extremely hard to do. Instead we brought some pumps from Amazon, so that the pump could directly draw the liquid from the bottle. But there are no drivers or phiscal switch for the pump. The pump begins to work once its being connected to the current. We've tried using transisters to control the current. But the transister would cause a decrease of voltage and would not be able to actually starts the pump. Our solution is to tie the circuit on the tip of the motors. And we can contorl the motor for a indirect control of the pump. We use a battery pack for the power source of the pumps. Therefore the pumps would intiate sequentially instead of simultaneously. This could be avoid by using individual battery packs for each pump. And for the tap, we were thinking of using the 3D printing, but the queue for the 3D printer is so long at the end of the semester. So we use lego instead.

## Wiring
![3d_printing](https://user-images.githubusercontent.com/14202464/145690801-21210ecf-cd0e-4859-8a46-73a895f59f05.png)

After experimenting with the transistor setup and not getting a lot of success with it, we spent some time rethinking how we could control the pumps via the raspberry using parts we already have access to. 

We knew that the micro servo motors we have could provide accurate but small range movement with its arms, so we decided to test the approach of connecting the wiring of the pumps by physically moving the connection with the help of a servo motor, basically using the servo motor as a controllable relay switch. 

Our small scale test with one motor and pump actually worked out quite well, so we settled on this approach and built our final wiring design.

Below is a picture of the actual wireing of our product. 

![3d_printing](https://user-images.githubusercontent.com/14202464/145690855-4bbb4827-2e37-4a5c-a734-6a6e81011fc4.jpg)


## Pump Control

As our prime task is to control a 12V bump, we first need to build a switch which could be controlled by the raspberry pi. 

The raspberry Pi 4 has GPIO which could only provide **3.3v** output and **16 mA** which is not enough for our need. The second thought would be using a transistor to control our motor 
![Untitled 1](https://user-images.githubusercontent.com/39228801/145690170-d2c82033-3170-427f-87ae-33d302140340.png)
![Untitled 2](https://user-images.githubusercontent.com/39228801/145690174-3532fb55-19a8-47f5-9ba3-b3e3dfa00862.png)

However, the transistor did not work under this setup in the situation. We soon went on with a more controllable solution

<img src="https://user-images.githubusercontent.com/39228801/145690181-89208e7e-76f8-4c1f-abb2-2bc06664b9f7.png" width="300">



We used a breadboard to wire our 3 pumps in parallel to a 12V battery pack. The pumps would draw liquids and dispense them easily using lengths of silicone pipes. There is a small height difference between the liquid container and the dispensing head, but after testing out the setup we found out that this did not affect the pumping rate.

<img src="https://user-images.githubusercontent.com/14202464/145690871-1eda0a2e-07bc-428e-bc37-e36305ee69c5.jpg" width="400">

## Motor Control

As we described before, we encountered some difficulties in using transistors to control motors. Instead, we come up with the idea that using physical switches to control these motors and we used a motor controller to control pumps. 

<img src="https://user-images.githubusercontent.com/14202464/145690930-fef09438-ddb9-476e-b42c-a1745b0a3a0a.jpg" width="400">

This is a closeup of the servo motor setup we used to control the pump. To limit the movement of the motor, we drilled small holes onto the backboard and used thin wires to secure the servo motors. When the raspberry pi sends a signal to the servo controller, the servo connected will move by a small amount (between 40 to 60 degrees depending on our tuning) to connect the pump wiring and activate it.

```python
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
```

As we use a 16 channels motor controller to finish this task, we use three of them (3,7,15) and we initialize these motors with a fixed angle. Once the motor being activated they would adjust themselves to the start angle. After receiving specific command, it will start the motor. 

## GUI

![Untitled](https://user-images.githubusercontent.com/39228801/145690088-640b1714-04ed-416d-9259-af2e148249d5.png)


In the GUI, we have multiple buttons here. With the guizero, we are able to customize these buttons easily.

```python
drink1Button = PushButton(app, image="coke3.jpg", width=40, height=60, command=drink1, text="Coke", grid=[0, 3])
```

These buttons has an argument `command` which enables us to activate an function.

```python
def drink12():
    os.system('python3 drink.py 1 4')
    os.system('python3 drink.py 2 4')
```

Or we could use multiprocessing to speed up the whole progress.

```python
from threading import Thread

def drink1():
    os.system('python3 drink.py 1 4')

def drink2():
    os.system('python3 drink.py 2 4')

def drink12():
    t1 = Thread(target = drink1)
    t2 = Thread(target = drink2)
    t1.start()
    t2.start()
```
## 3-D Printing vs. Lego Prototype

| **3-D Printing Design** | **Lego Prototype** |
| --- | --- |
| <img src="https://user-images.githubusercontent.com/14202464/145690961-791d9b4a-84c7-42af-a009-64eeffcd4cdf.PNG" width="400"> | <img src="https://user-images.githubusercontent.com/14202464/145690951-34d8164d-0055-4c9c-a78d-940dba04f2f2.jpg" width="400"> |

An interesting tradeoff we made was to replace our designed 3-D printed dispenser parts with lego prototypes since the 3-D printers were fully occupied. The lego parts provided a similar design flexibility while being easily assembled and saved us a lot of time.

## Touch Screen Drive

We bought a screen from Elecrow. it is able to connect directly to the raspberry pi. Drive could be downloaded here. [https://github.com/goodtft/LCD-show](https://github.com/goodtft/LCD-show)

```python
sudo rm -rf LCD-show
git clone https://github.com/goodtft/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show/
sudo ./XXX-show 90
```

## Reflections on process

For the previous projects, we've never encountered problems with power supply. But for project that requires a usage of some power consuming parts (pump in our case), we should really take that seriouly in the design process. <br>
We were thinking of using the led light strip for decreating, but that would actually make it ugly. So, think over about the parts your really need before buying it.<br>


## User testing

We've asked many people to test our project. Below are some useful comments.<br>
<br>
How do you clean the the machine to make sure its clean and drinkable? (Our solution is to replace the tube reguarly)<br>
Can add a stop button to stop the dispensing process immdeially. So when user select the wrong drink they can fix it quickly.<br>
Instead of dispensing the fixed amount, can add the feature to let user decided how much drink they would have so there will be no waste.<br>



## Group work distribution 
Wenlan Wei is the main contributor, in charge of the implementation of the code for pump control and circuit building.<br>
Xingyu Tao implemented the code for the UI interface, and contributed for prototype building. Also did the 3D modeling, but not used in project.<br>
Jiacheng Peng is in charge of the documentation, the prototype building and testing.<br>
