import cv2 as cv
img=cv.imread("D:\Machine Learning\Libraries\OpenCV\Photos\cat.jpg")
cv.imshow("BGR Cat",img)
cv.waitKey(0)

# BGR to Gray scale image
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# src,code(Color Code)
cv.imshow("Gray Cat",gray)
cv.waitKey(0)

# Blur an image
blur=cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
# src,ksize(Kernal size it needs to be odd),sigmaX,borderType=None
cv.imshow("Blur",blur)
cv.waitKey(0)

# Edge cascade
edge=cv.Canny(img,125,175)
# src , t1,t2
cv.imshow('Edge',edge)
cv.waitKey(0)

# To reduce edge
edge=cv.Canny(blur,125,175)
# src , t1,t2
cv.imshow('Edge',edge)
cv.waitKey(0)

# dilating the image
dilated=cv.dilate(edge,(7,7),iterations=1)
cv.imshow('Dilated',dilated)
cv.waitKey(0)

# Eroding
eroded=cv.erode(edge,(7,7),iterations=1)
cv.imshow('Eroded',eroded)
cv.waitKey(0)

# resize
resize=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
# src,destination size
cv.imshow("Resized",resize)
cv.waitKey(0)

# Croping
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)
