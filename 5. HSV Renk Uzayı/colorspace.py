import cv2

image = cv2.imread(r".\ornek.jpg")

imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow("Image HSV",imageHSV)

cv2.imwrite("imagehsv.jpg",imageHSV)

