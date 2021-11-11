from flask import Flask,render_template
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys

app = Flask(__name__)
np.set_printoptions(suppress=True)
PATH_recipt = 'recipt_test/keras_model.h5'
PATH_COOK = 'cook_test/keras_model.h5'
PATH_LABEL_COOK = "cook_test/labels.txt"
PATH_LABEL_recipt = "recipt_test/labels.txt'

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
    


def Classify(webCam,cap,model,labels):
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
    print("I think its a:",labels[np.argmax(prediction)])

    return labels[np.argmax(prediction)]
    

def process():
    model,labels = init_model(PATH,LABEL)
    webcam, capture = init_camera()
    return Classify(webcam,capture,model,labels)


@app.route('/')
def index():
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
