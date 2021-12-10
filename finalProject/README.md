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

## Design
Below is a picture of the general idea. <br>
<img width="884" alt="Screen Shot 2021-12-07 at 12 21 17 AM" src="https://user-images.githubusercontent.com/39228801/144971227-61becb18-6140-469d-b94d-5ad33fcb45e4.png">

This is a picture of the circuit of inside the prototype.<br>
![image](https://user-images.githubusercontent.com/39228801/145515759-ae47967a-8dcf-4f15-980e-bde8c356853a.png)

## Demo
Below is a link to a demo video of the working prototype. <br>
[<img width="1138" alt="Screen Shot 2021-12-07 at 10 35 28 AM" src="https://user-images.githubusercontent.com/39228801/145059752-b644615d-5fc9-470c-9ce9-645721a4bf6c.png">](https://www.youtube.com/watch?v=HgxsOgSMFxE)

## Design Process

When we first start thinking about this idea, we were thinking about using motors to control the lid of a bottle for dispensing the drinks. But we found this is extremely hard to do. Instead we brought some pumps from Amazon, so that the pump could directly draw the liquid from the bottle. But there are no drivers or phiscal switch for the pump. The pump begins to work once its being connected to the current. We've tried using transisters to control the current. But the transister would cause a decrease of voltage and would not be able to actually starts the pump. Our solution is to tie the circuit on the tip of the motors. And we can contorl the motor for a indirect control of the pump. We use a battery pack for the power source of the pumps. Therefore the pumps would intiate sequentially instead of simultaneously. This could be avoid by using individual battery packs for each pump. And for the tap, we were thinking of using the 3D printing, but the queue for the 3D printer is so long at the end of the semester. So we use lego instead.

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
