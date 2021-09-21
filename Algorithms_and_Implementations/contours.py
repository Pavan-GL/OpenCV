import cv2 as cv
import numpy as np
img=cv.imread("D:\Machine Learning\Libraries\OpenCV\Photos\cats.jpg")
cv.imshow("Image",img)
cv.waitKey(0)

# Contours 

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
cv.waitKey(0)

# Blur
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
cv.waitKey(0)


# edges
canny=cv.Canny(blur,125,175)
cv.imshow("Canny Edges",canny)
cv.waitKey(0)

# or
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)
cv.waitKey(0)

# below 125 set to 0 black
# above 1 white
countours,hierarches=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(countours)}countour(s)found!')

# Contours looks at the structuring of an image and returen the edges in 2 values
# i.e list of coordinates,hi rep(rec--squre)
countours,hierarches=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(countours)}countour(s)found!')
# RETR_TREE returns all hii contours
# RETR_EXTERNAL returns exteranl contours
# RETR_LIST all the con
# cv.CHAIN_APPROX_NONE returns all the contours
# cv.CHAIN_APPROX_SIMPLE compressed countours(compress into 2 end points(LINE))

# Visulize the contour that found on the image
blank=np.zeros(img.shape,dtype='uint8')
cv.imshow("Blank",blank)
cv.waitKey(0)

# To draw
cd=cv.drawContours(blank,countours,-1,(0,0,255),2)
# -1 all
cv.imshow("CDrawn",cd)
cv.waitKey(0)

# canny---contours
