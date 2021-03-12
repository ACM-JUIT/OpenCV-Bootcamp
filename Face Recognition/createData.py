# Creating a dataset

import cv2
import numpy as np

# Initializing Cascade Classifier
CLASSIFIER_PATH = 'Classifiers\haarcascade_frontalface_default.xml'
classifier = cv2.CascadeClassifier(CLASSIFIER_PATH)

# Initializing camera device
cam = cv2.VideoCapture(0)

# Taking input unique user id
id = input('ID: ')
num = 0

while(True):

    _, frame = cam.read()

    # Converting to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Extract faces from frame
    faces = classifier.detectMultiScale(gray, 1.3, 5)

    # Loop through each face
    for face in faces:
        num += 1
        (x, y, w, h) = face

        # Writing data - saving face as jpg image
        cv2.imwrite('dataset/User.' + str(id) + "." +
                    str(num) + ".jpg", gray[y:y+h, x:x+w])

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.waitKey(1)

    cv2.imshow('Face', frame)
    cv2.waitKey(1)

    # Breaking out of loop when 60 images are saved
    if (num > 60):
        break

cam.release()
cv2.destroyAllWindows()
