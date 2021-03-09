#Importing Libraries
import cv2

#Reading Image File
img = cv2.imread('elon.jpg')
img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
cv2.imshow('Original', img)           #Showing Original Image 

#Preprocessing Part 
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (3,3), 0)   #Applying Image Blur Part 

#Canny edge editor
edged = cv2.Canny(img, 100, 200)

#Printing Image Part
cv2.imshow('Edges',edged)
cv2.waitKey()
