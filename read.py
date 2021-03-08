# Loading/Importing libraries
import cv2

# Reading image file
img = cv2.imread('images/elon.jpg')
cv2.imshow('Image', img)

# Dimensions
print("Original Dimensions")
dims = img.shape
print(dims)

# Extracting height and width
(h, w) = img.shape[0], img.shape[1]

# Resizing image to half its original dimensions
resized_image = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
print("Resized Dimensions")
print(resized_image.shape)

# Displaying resized image
cv2.imshow('Resize', resized_image)
cv2.waitKey()
