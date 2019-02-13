import cv2

image= cv2.imread(r"ornek.jpg")

image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

hist_equalize = cv2.equalizeHist(image_gray)

cv2.imshow("Resim",image_gray)
cv2.imshow("Histogram Eşitleme",hist_equalize)

cv2.imwrite("image_gray.jpg",image_gray)
cv2.imwrite("hist_image.jpg",hist_equalize)
