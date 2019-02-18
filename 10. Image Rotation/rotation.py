import cv2


image  = cv2.imread("test.png")
height,width = image.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2),180, .9)

rotated_image = cv2.warpAffine(image, rotation_matrix,(width,height))

cv2.imshow("rotated image",rotated_image)
cv2.imwrite("rotated-image.jpg",rotated_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
