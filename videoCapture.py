import cv2

# Initializing input device
cam = cv2.VideoCapture(0)

while(True):

    # Function .read() returns a boolean and video capture frame by frame
    # flag returns True or False depending on whether it reads video
    flag, frame = cam.read()

    # Grayscaling
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame Gray', gray)

    # Blurring and Canny Edge Detection
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    edges = cv2.Canny(blur, 100, 200)

    # Displaying processed video, frame by frame
    cv2.imshow('Frame', edges)

    # Grabbing which key was pressed
    key = cv2.waitKey(1)

    # Escape key
    if(key == 27):
        break

cam.release()
cv2.destroyAllWindows()
