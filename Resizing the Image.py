import cv2

#Reads the image as a gray scale image
img = cv2.imread("Image1.jpg",0)

#resize image
resize_image = cv2.resize(img,(650,500)) 

#opens a window to display the image
cv2.imshow("Image1",resized_image)

# waits until the user presses a key
cv2.waitKey(0)

#closes the window based on wait for key parameter
cv2.destroyAllWindows()
