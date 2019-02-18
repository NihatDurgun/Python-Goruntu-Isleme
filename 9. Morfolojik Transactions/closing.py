import cv2
import numpy as np

image  = cv2.imread("test.jpg",0)
kernel = np.ones((5,5),np.uint8)

closing = cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)

cv2.imshow("resim",closing)
cv2.imwrite("closing.jpg",closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
