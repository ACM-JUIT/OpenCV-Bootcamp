#import Libraries 
import cv2

#Reading Image File
image=cv2.imread('elon.jpg')
cv2.imshow("Image show", image)

#Preprocessing Part 
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #BGR To greyscale
cv2.imshow("Gray", gray)
rgb=cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #RGB To BGR

#Printing Image Part 
cv2.imshow("rgb", rgb)
cv2.waitKey(0)  
