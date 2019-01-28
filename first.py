import cv2

cap =cv2.VideoCapture(0)

while(1):
    ret,frame = cap.read()
    if(ret):
        
