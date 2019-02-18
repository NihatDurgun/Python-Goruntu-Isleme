import cv2
import numpy as np

image  = cv2.imread("test.jpg",0)
kernel = np.ones((5,5),np.uint8)

opening = cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)

cv2.imshow("resim",opening)
cv2.imwrite("opening.jpg",opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
