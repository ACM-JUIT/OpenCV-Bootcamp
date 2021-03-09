# Loading/Importing libraries
import cv2

# Reading image file
img = cv2.imread('images/elon.jpg')
img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
cv2.imshow('Original', img)

# Converting to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Applying blurring
img = cv2.GaussianBlur(img, (3, 3), 0)

# Canny Edge Detector
edged = cv2.Canny(img, 100, 200)

cv2.imshow('Edges', edged)
cv2.waitKey()
