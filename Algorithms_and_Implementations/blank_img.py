import cv2 as cv
import numpy as np

blank=np.zeros((500,500),dtype='uint8')
cv.imshow('Blank',blank)
cv.waitKey(0)

# To draw color
blank=np.zeros((500,500,3),dtype='uint8')# h,w,number of color channels
cv.imshow('Blank',blank)
blank[:]=0,255,0
cv.imshow('Green',blank)
cv.waitKey(0)

# color with shape

blank=np.zeros((500,500,3),dtype='uint8')# h,w,color
cv.imshow('Blank',blank)
blank[200:300,300:400]=255,0,0 # certain portion of an image
cv.imshow('blue',blank)
cv.waitKey(0)


# capture.set(3,width)

