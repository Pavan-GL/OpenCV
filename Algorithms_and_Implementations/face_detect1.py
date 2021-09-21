import numpy as np
import cv2 as cv
img=cv.imread("D:\Machine Learning\Libraries\OpenCV\Photos\group 2.jpg")
cv.imshow("Person",img)
cv.waitKey(0)
#no clr needed and edges are imp
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
cv.waitKey(0)

har=cv.CascadeClassifier('harsf.xml')
face_rect=har.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
#face_rect=har.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
print(f"Nor of faces={len(face_rect)}")
for (x,y,w,h)in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow("Detected Faces",img)
cv.waitKey(0)