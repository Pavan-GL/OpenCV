import cv2 as cv
import numpy as np
img=cv.imread("D:\Machine Learning\Libraries\OpenCV\Photos\cat.jpg")
cv.imshow("Image",img)
cv.waitKey(0)

# Translation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimesnsions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimesnsions)
# warpAffine() function is the size of the output image, which should be in the form of (width, height).
# Remember width = number of columns, and height = number of rows.
    
# -x --- left
# -y --- up
# x ---- right
# y -----down
translated=translate(img,100,-100)
cv.imshow('Translated',translated)
cv.waitKey(0)

# Rotation
def rotate(img,angle, rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
        
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,2.0) #scale
    dimesnsions1=(width,height)
    return cv.warpAffine(img,rotMat,dimesnsions1)
rotated=rotate(img,45)
cv.imshow('Rotated',rotated)
cv.waitKey(0)

rotated1=rotate(img,-45)
cv.imshow('Rotated1',rotated1)
cv.waitKey(0)

# resize
resize=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
# src,destination size
cv.imshow("Resized",resize)
cv.waitKey(0)

# Flipping

flip=cv.flip(img,0)
# 0 for V and 1 for H -1 for both V and H
cv.imshow("Flipped",flip)
cv.waitKey(0)
    
    