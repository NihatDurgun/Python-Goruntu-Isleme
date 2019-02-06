import cv2

image = cv2.imread(r".\ornek.jpg")

image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

ret,threshold_image = cv2.threshold(image_gray,0,255,cv2.THRESH_OTSU)

cv2.imshow("thresholding",threshold_image)

cv2.imwrite("thresholding.jpg",threshold_image)

