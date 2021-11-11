
#This example is directly copied from the Tensorflow examples provided from the Teachable Machine.

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys

np.set_printoptions(suppress=True)
PATH_COOK = 'cook_test/keras_model.h5'
PATH_LABEL_COOK = "cook_test/labels.txt"

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
    pic_0 = cv2.imread('images/0.jpg')
    cv2.imshow('RECIPT',pic_0)
    # cv2.waitKey(5)
    webcam, capture = init_camera()
    model_cook,labels_cook = init_model(PATH_COOK,PATH_LABEL_COOK)
    while True:
        res = Classify(webcam,capture,model_cook)
        
        if res!=4:
            print("I think its a:",labels_cook[res])
            if res ==0:
                pic_1 = cv2.imread('images/1.jpg')
                cv2.imshow('RECIPT',pic_1)
                print('one tomato prepared')
            if res==1:
                print('two tomato prepared')
            if res==2:
                pic_1 = cv2.imread('images/2.jpg')
                cv2.imshow('RECIPT',pic_1)
                print('one egg prepared')
            if res==3:
                print('eggs prepared')
            if res==5:
                print('sliced tomatos prepared')
            if res==6:
                print('mixed eggs prepared')
        #if res==6:
        #    break

process()

# Disable scientific notation for clarity


# img = None
# webCam = False
# if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
#    try:
#       print("I'll try to read your image");
#       img = cv2.imread(sys.argv[1])
#       if img is None:
#          print("Failed to load image file:", sys.argv[1])
#    except:
#       print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
# else:
#    try:
#       print("Trying to open the Webcam.")
#       cap = cv2.VideoCapture(0)
#       if cap is None or not cap.isOpened():
#          raise("No camera")
#       webCam = True
#    except:
#       print("Unable to access webcam.")


# # Load the model
# model = tensorflow.keras.models.load_model('cook_test/keras_model.h5')
# # Load Labels:
# labels=[]
# f = open("cook_test/labels.txt", "r")
# for line in f.readlines():
#     if(len(line)<1):
#         continue
#     labels.append(line.split(' ')[1].strip())


# while(True):
#     if webCam:
#         ret, img = cap.read()

#     rows, cols, channels = img.shape
#     data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

#     size = (224, 224)
#     img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
#     #turn the image into a numpy array
#     image_array = np.asarray(img)

#     # Normalize the image
#     normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
#     # Load the image into the array
#     data[0] = normalized_image_array

#     # run the inference
#     prediction = model.predict(data)
#     print("I think its a:",labels[np.argmax(prediction)])

#     if webCam:
#         if sys.argv[-1] == "noWindow":
#            cv2.imwrite('detected_out.jpg',img)
#            continue
#         cv2.imshow('detected (press q to quit)',img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             cap.release()
#             break
#     else:
#         break

# cv2.imwrite('detected_out.jpg',img)
# cv2.destroyAllWindows()
