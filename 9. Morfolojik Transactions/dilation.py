import cv2
import numpy as np

image  = cv2.imread("test.jpg",0)
kernel = np.ones((5,5),np.uint8)

dilation = cv2.dilate(image,kernel,iterations = 1)

cv2.imshow("resim",dilation)
cv2.imwrite("dilation.jpg",dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
