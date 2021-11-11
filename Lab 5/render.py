import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys
import matplotlib.pyplot as plt
import matplotlib.image  as ming


np.set_printoptions(suppress=True)
PATH_recipt = 'recipt_test/keras_model.h5'
PATH_COOK = 'cook_test/keras_model.h5'
PATH_LABEL_COOK = "cook_test/labels.txt"
PATH_LABEL_recipt = "recipt_test/labels.txt"

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

    return np.argmax(prediction)
    

def process():
    pic_0 = plt.imread('images/0.png')
    plt.imshow(pic_0)
    webcam, capture = init_camera()
    model_cook,labels_cook = init_model(PATH_COOK,PATH_LABEL_COOK)
    while True:
        res = Classify(webcam,capture,model_cook)
        if res!=4:
            if res ==0:
                pic_1 = plt.imread('images/1.png')
                plt.imshow(pic_1)
                print('one tomato prepared')
            if res==1:
                print('two tomato prepared')
            if res==2:
                pic_1 = plt.imread('images/2.png')
                plt.imshow(pic_2)
                print('one egg prepared')
            if res==3:
                print('eggs prepared')
            if res==5:
                print('sliced tomatos prepared')
            if res==6:
                print('mixed eggs prepared')
        if res==6:
            break
    model_recipt, labels_recipt = init_model(PATH_COOK,PATH_LABEL_COOK)
    while True:
        res = Classify(webcam,capture,model_recipt)
        count =3
        if res==1 or res==3:
            count+=1
            
        else:
            count-=1
        if count<0:
            count=0
        if count>4:
            count=4
        path = 'images/'+str(count)+'.png'
        pic_r = plt.imread(path)
        plt.imshow(pic_r)
    capture.release()



                

img = cv2.imread('images/0.jpeg')
cv2.imshow('test',img)
cv2.waitKey(1)

print('*'*20,'START','*'*20)
process()