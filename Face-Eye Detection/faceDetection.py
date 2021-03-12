import cv2

# Initializing classifier path
CLASSIFIER_PATH = "Classifiers/haarcascade_frontalface_default.xml"

# Live video capturing
cam = cv2.VideoCapture(0)

# Initializing classifier
face_classifier = cv2.CascadeClassifier(CLASSIFIER_PATH)

while (True):

    _, frame = cam.read()

    # Converting to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Returns coordinates of all faces in the frame
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    # Cycle through each coordinate list
    for face_dims in faces:

        # Destructuring data and extracted bounding box coordinates
        (x, y, w, h) = face_dims

        # Extracting mid points of bounding box
        mid_x = int(x + w/2)
        mid_y = int(y + h/2)

        # Drawing - "bounding box"
        frame = cv2.rectangle(frame, (x, y), (x + h, y + h), (0, 255, 255), 2)

        # Writing 'x-coordinate' on live feed
        frame = cv2.putText(frame, str(x), (x, y),
                            cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 255), 2)

        frame = cv2.putText(frame, ".", (mid_x, mid_y),
                            cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 255), 3)

    # Displaying video feed with detected faces
    cv2.imshow('Frame', frame)

    # Reading for keyboard interrupts
    key = cv2.waitKey(1)
    if (key == 27):
        break

cam.release()
cv2.destroyAllWindows
