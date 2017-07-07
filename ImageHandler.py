import cv2
import numpy as np
#Read Image
img = cv2.imread('React tutorial action cycle.png')
#Display Image
cv2.imshow('image',img)
cv2.waitKey(2)
cv2.destroyAllWindows()

#Applying Grayscale filter to image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Saving filtered image to new file
cv2.imwrite('graytest.jpg',gray)