import cv2


image  = cv2.imread("test.png")
height,width = image.shape[:2]

start_row, start_col = int (height * .07), int (width * .42)
end_row, end_col = int (height * .65), int (width * .75)

cropped = image [start_row : end_row , start_col : end_col]
cv2.imshow("cropped image",cropped)
cv2.imwrite("cropped-image.jpg",cropped)


cv2.waitKey(0)
cv2.destroyAllWindows()
