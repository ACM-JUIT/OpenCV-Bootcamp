# Loading/Importing libraries
import cv2

# Initializing constants
OUTPUT = "ELON MUSK"

# Reading image file
img = cv2.imread('images/elon.jpg')
resized_image = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Copying images
img_copy = resized_image.copy()

# Drawing a green rectangle
cv2.rectangle(img_copy, (100, 40), (150, 60), (0, 255, 0), 2)

# Drawing a blue circle
cv2.circle(img_copy, (300, 150), 20, (255, 0, 0), 1)

# Writing text on images
cv2.putText(img_copy, OUTPUT, (250, 50),
            cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 255), 2)

cv2.imshow('Drawn', img_copy)

cv2.waitKey()
