import cv2
import numpy as np

image  = cv2.imread("test.jpg",0)
kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(image,kernel,iterations = 1)

cv2.imshow("resim",erosion)
cv2.imwrite("erode.jpg",erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
