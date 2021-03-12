import cv2
import numpy as np

# Initializing classifier
CLASSIFIER_PATH = 'Classifiers\haarcascade_frontalface_default.xml'
classifier = cv2.CascadeClassifier(CLASSIFIER_PATH)

# Initializing recognizer and loading trained data
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainedData.yml')

cam = cv2.VideoCapture(0)
id = 0

while(True):

    _, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = classifier.detectMultiScale(gray, 1.3, 5)
    name = ''

    for face in faces:
        (x, y, w, h) = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        id, conf = recognizer.predict(gray[y:y+h, x:x+w])

        if(conf < 50):
            if (id == 1):
                name = "User #1"
                frame = cv2.putText(frame, name, (x, y+h),
                                    cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 255), 1)

    cv2.imshow('Face', frame)

    if(cv2.waitKey(1) == 27):
        break

cam.release()
cv2.destroyAllWindows()
