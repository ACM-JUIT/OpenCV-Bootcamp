import cv2
import numpy as np

img = cv2.imread('images/elon.jpg')
img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

# OpenCV reads an image as B, G, R

# Extracting B G R values from original image
blue_channel = img[:, :, 0]
green_channel = img[:, :, 1]
red_channel = img[:, :, 2]


# Create empty images with each pixel value as 0 (Black)
blue_img = np.zeros(img.shape)
green_img = np.zeros(img.shape)
red_img = np.zeros(img.shape)

# Assigning values from channels to empty images
blue_img[:, :, 0] = blue_channel
green_img[:, :, 1] = green_channel
red_img[:, :, 2] = red_channel

# Isolated channels of original image
cv2.imshow('Red Channel', red_img)
cv2.imshow('Blue Channel', blue_img)
cv2.imshow('Green Channel', green_img)
cv2.waitKey()
