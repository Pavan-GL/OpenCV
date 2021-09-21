import cv2 as cv
img=cv.imread("D:\Machine Learning\Libraries\OpenCV\Photos\cats.jpg")
cv.imshow("Cat",img)
cv.waitKey(0)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
cv.waitKey(0)

# Simple Thresholding
threshhold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
#thresh bin image,threshold : passed value
#src,tvalue,maxval,type
cv.imshow('Simple Threshold',thresh)
cv.waitKey(0)

threshhold,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
#thresh bin image,threshold : passed value
#src,tvalue,maxval,type
cv.imshow('Simple Inverse Threshold',thresh_inv)
cv.waitKey(0)


# Adaptive thresholding #optimal soln based on mean
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
#block size,c value
cv.imshow('Adaptive',adaptive_thresh)
cv.waitKey(0)

adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3)
#block size,c value
cv.imshow('Adaptive INV',adaptive_thresh)
cv.waitKey(0)