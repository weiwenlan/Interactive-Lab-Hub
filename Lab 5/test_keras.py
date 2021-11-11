from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Load the model
model = load_model('face_test/keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image


"""
image = Image.open('<IMAGE_PATH>')
#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)
# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)
print(prediction)
"""

cap = cv2.VideoCapture(0)
if cap is None or not cap.isOpened():
    raise("No camera")
webCam = True

while(True):
    if webCam:
        ret, image = cap.read()

    rows, cols, channels = img.shape

    # Use the given image as input, which needs to be blob(s).
    tensorflowNet.setInput(cv2.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))

    # Runs a forward pass to compute the net output
    networkOutput = tensorflowNet.forward()

    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(prediction)




    # Loop on the outputs
    # for detection in networkOutput[0,0]:
    #     score = float(detection[2])
    #     if score > 0.2:
    #         left = detection[3] * cols
    #         top = detection[4] * rows
    #         right = detection[5] * cols
    #         bottom = detection[6] * rows

    #         #draw a red rectangle around detected objects
    #         cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (0, 0, 255), thickness=2)

    # if webCam:
    #     if sys.argv[-1] == "noWindow":
    #        print("Finished a frame")
    #        cv2.imwrite('detected_out.jpg',img)
    #        continue
    #     cv2.imshow('detected (press q to quit)',img)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         cap.release()
    #         break