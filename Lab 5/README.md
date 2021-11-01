# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms needs to be aware of.

## Prep

1.  Pull the new Github Repo.
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2021/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:

1. Raspberry Pi
1. Webcam 
1. Microphone (if you want to have speech or sound input for your design)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

Following is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.<br>
**Contours Detection**<br>
potential design example: Object classifing system.<br>
We can use the fact that different object has different contours to classify what type of object is showed in the camera by applying this algorithm.<br>
![1635535976(1)](https://user-images.githubusercontent.com/39228801/139492152-4d5278de-926d-409c-acd2-1822b039cc04.png)
<br>
**Face Detection** <br>
potential design example: Automatic Check-In system.<br>
We can use the face detection algorithm to create a check-in system. Where the camera would automaticly check the student in if it sees the student. <br>
![1635536393(1)](https://user-images.githubusercontent.com/39228801/139492746-6dd93420-310f-400f-b274-87df81d79947.png)
<br>
**Flow detection**<br>
potential design example: Pet motion tracker. <br>
We can use this to find out what our pet is doing when we are not home by monitoring the moving path of the pets.<br>
![1635536589](https://user-images.githubusercontent.com/39228801/139493082-192d1222-2fff-4144-b56b-3755a042b15d.png)
<br>
**Object Detection**<br>
potential design example: unattended object detection. <br>
We can applying this algorithm to surveillance camera, when there are extraneous object showed in the room for a long time. It means we identified an unattended object.<br>
![1635536715(1)](https://user-images.githubusercontent.com/39228801/139493312-c7a11d7c-ec0c-4ce2-85f1-4dae1754c17c.png)

<br>


\*\*\***

#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi4 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

#### Hand Pose Detection
We tried the hand pose detection model and noted the pinch percentage feature.

| **Hand open** | **Hand close** |
| --- | --- |
| ![hand_pose_4](https://user-images.githubusercontent.com/14202464/139499719-64ccf4f4-867c-4281-b7c5-b2b87aaa6f23.PNG) |![hand_pose_1](https://user-images.githubusercontent.com/14202464/139499728-090150f1-ef68-44d5-9cb7-22511d442316.PNG) |

We also noticed how the system would not be able to detect hand pose if some part of the hand is blocked by an object, for example when I'm hodling up a piece of cardboard

| **Hand pose detected** | **Hand pose not detected** |
| --- | --- |
| ![hand_pose_2](https://user-images.githubusercontent.com/14202464/139499894-b0fc161e-bb93-4842-b8bd-0672035290a4.PNG) | ![hand_pose_3](https://user-images.githubusercontent.com/14202464/139499906-e8b1e3ff-d145-42b8-afb8-aebaebd722c7.PNG) |


**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)

Using the hand pose pinching percentage, I can think of applying it to Human Computer Interactions, like using hand pinching to zoom in and out of an image, or using hand pinching to toggle volume up and down. 

More interesting is how we could use a similar tracking for face or body pose tracking. We brainstormed some application for them:

**Face Tracking**
- Detect mood of a person based on facial features
- Detect distracted or fatigued driving behaviour in long-haul trucking
- Detect eye movement in polic interogation scenario

**Body Pose Tracking**
- Detect limb position in rehabilitation exercises (for patients recovering from injuries)
- Detect limb position for bodybuilders looking to perfect their forms
- Detect body movement for child or elder care, and alert caregivers when movmement is not detected


#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


| **Tester 1 detected** | **Tester 2 detected** |
| --- | --- |
| ![image](https://user-images.githubusercontent.com/40989769/139597495-f3ddc51e-df6e-4be0-a93a-9aec18a598df.png) | ![image](https://user-images.githubusercontent.com/40989769/139597533-21e5b66b-a974-4fe4-a6fd-020bbb48531a.png) |


### DEPLOY THE MODEL

<img width="1316" alt="iShot2021-10-31 17 19 27" src="https://user-images.githubusercontent.com/40989769/139601652-f3f19dd7-fb35-41be-80ce-ef78d72eb832.png">






(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***


*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


#### Filtering, FFTs, and Time Series data. (optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***


### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***\\

One of the interesting class of objects we played around with is hand gesture detection using Hand Pose and object detection using Teaching Machine. We brainstormed an idea to build a **Cooking Instructor** using object detection and hand gesture detection. This system would be hooked up to a screen that can take you step by step through assembling a recipe and making a meal.

1. **Select Recipe**: The user can browse and select a recipe to make, the screen then shows what ingredients the user needs to gather.
2. **Preparing the Ingredients**: Once the user has gathered all the ingredients, they can proceed to the next step. The **cooking instructor** will walk the user through the steps of preparing the ingredients, by detecting the ingredients present on the cutting board and instructing the user to proceed to cut them into pieces. The device will detect what ingredients are on the board, and if the ingredient processing is done and proceed to the next step.
3. **Cooking**: For the cooking portion, the **cooking instructor** will provide automatic timers for the user to use. They can also flip through the recipe steps using hand gestures to review or preview steps.

**[insert story board]**
### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?<br>
    When you are cooking. It is hard to use your phone to looking at the recepie with your wet hands. This system would use camera to detect the food indegredient on the table, determine what step you are in the recipe and display it on the monitor. You can also change the step you are in by using the hand gestures. (Moving forward or backword for the recepie displayed on the monitor)<br>
2. When does it fail?<br>
    The object on the table might not be correct detected. And that leads to a fail of moving forward in the recepie.<br>
3. When it fails, why does it fail?<br>
    The food indegredient might be cutted in different shapes. And that leads to a confusion of determine what kind of indregident it is.<br>
4. Based on the behavior you have seen, what other scenarios could cause problems?<br>
    The system may not detect the hand gesture correctly. <br>
**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?<br>
    It is not intuitive that control the height by using hand gesture. <br>
3. How bad would they be impacted by a miss classification?<br>
    It will not be really bad. If the system do not work properly, the user would jsut dry their hands and check the recepie manually.<br>
4. How could change your interactive system to address this?<br>
    We could display a user guid in the monitor when a user approaches.<br>
5. Are there optimizations you can try to do on your sense-making algorithm.<br>
    We could take more pictures of hand gestures, and catetorized them into a single category. That would increase the rate for detecting the gesture if the gesture is not perfect. <br>
### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
