import cv2 as cv
def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale) # img
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA) 
# Resizing an image needs a way to calculate pixel values for the new image from the original one. 
# The five such interpolation methods provided with OpenCV are INTER_NEAREST , INTER_LINEAR , 
# INTER_AREA , INTER_CUBIC , and INTER_LANCZOS4

img=cv.imread('D:\Machine Learning\Libraries\OpenCV\Photos\cat.jpg')
cv.imshow('cat',img)
img_rescale=rescale(img)
cv.imshow('Resized_cat',img_rescale)
cv.waitKey(0) 
