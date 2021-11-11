#This example is directly copied from the Tensorflow examples provided from the Teachable Machine.

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys
import time

np.set_printoptions(suppress=True)
PATH_COOK = 'recipt_test/keras_model.h5'
PATH_LABEL_COOK = "recipt_test/labels.txt"

def init_model(path_model,path_label):
    # Load the model
    model = tensorflow.keras.models.load_model(path_model)
    # Load Labels:
    labels=[]
    f = open(path_label, "r")
    for line in f.readlines():
        if(len(line)<1):
            continue
        labels.append(line.split(' ')[1].strip())
    return model,labels

def init_camera():
    try:
        cap = cv2.VideoCapture(0)
        if cap is None or not cap.isOpened():
            raise("No camera")
        webCam = True
        return webCam,cap
    except:
        print("Unable to access webcam.")
        return False,None
    


def Classify(webCam,cap,model):
    if webCam:
        ret, img = cap.read()

    rows, cols, channels = img.shape
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    size = (224, 224)
    img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
    #turn the image into a numpy array
    image_array = np.asarray(img)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    #print("I think its a:",labels[np.argmax(prediction)])
    cv2.imshow('image_mow',img)
    cv2.waitKey(1)
    
    return np.argmax(prediction)
    

def main():
    model,labels = init_model(PATH_COOK,PATH_LABEL)
    webcam, capture = init_camera()
    while True:
        Classify(webcam,capture,model,labels)

def process():
    webcam, capture = init_camera()
    model_recipt, labels_recipt = init_model(PATH_COOK,PATH_LABEL_COOK)
    pic_0 = cv2.imread('images/0.jpg')
    cv2.imshow('RECIPE',pic_0)
    count=0
    pre = 0
    count_down =5
    while True:
        res = Classify(webcam,capture,model_recipt)
        print("I think its a:",labels_recipt[res])
        if res==pre:
            if count_down == 0:
                if res==1:
                    count+=1
                    
                elif res==2:
                    count-=1
                if count<0:
                    count=0
                if count>4:
                    count=4
                path = 'images/'+str(count)+'.jpg'
                pic_r = cv2.imread(path)
                cv2.imshow('RECIPE',pic_r)
                count_down=5
            else:
                count_down-=1
        pre =res
        #time.sleep(1)

    capture.release()


process()
