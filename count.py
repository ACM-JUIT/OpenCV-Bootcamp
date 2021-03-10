import cv2
import imutils

#reading image and converting into grayscale
image=cv2.imread('images/lego.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Thresholding (pixels with a value greater than 233 will be converted to white, less than 233 will be converted to white)
ret,thresh=cv2.threshold(gray, 233, 255, cv2.THRESH_BINARY_INV) #read "Otsu's Binarization" to know about the significance of the "ret" value

#finding contours
contours=cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours=imutils.grab_contours(contours)
print(contours[1][1])

output=image.copy()     #copying the original image 
#drawing contours
for c in contours:
    cv2.drawContours(output, [c], -1, (204,0,102),3 )
    cv2.imshow("Contours",output)
    cv2.waitKey(0)

#adding text on the image
text = "{} Lego pieces!".format(len(contours))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (204, 0, 102), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)




