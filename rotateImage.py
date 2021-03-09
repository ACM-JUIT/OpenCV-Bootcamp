# Importing libraries
import cv2

# Reading image file
img = cv2.imread('images/elon.jpg')
cv2.imshow('Image', img)


# Resizing image
img = cv2.resize(img, (400,400))

#Rotating Image 90 deg clockwise 
# ROTATE_90_CLOCKWISE
# ROTATE_180
# ROTATE_90_COUNTERCLOCKWISE
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)


#Displaying rotated Image
cv2.imshow('Image', img)
cv2.waitKey(0)