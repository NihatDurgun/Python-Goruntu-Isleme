import cv2

image= cv2.imread(r"test.png")
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

image_blur = cv2.GaussianBlur(image_gray,(5,5),0)
image_edges = cv2.Canny(image_blur,20,20)

cv2.imshow("Resim Kenarları",image_edges)

cv2.imwrite("image_blured.jpg",image_blur)
cv2.imwrite("canny_image.jpg",image_edges)
