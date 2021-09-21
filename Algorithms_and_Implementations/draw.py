import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)
cv.waitKey(0)

# To draw recatangle
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)

# to fill inside the box use thickness=cv.Filled
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED)
# img,pt1,pt2,color,thickness=None,lineType=None,shift=None,/)
cv.imshow('Reactangle',blank)
cv.waitKey(0)


# To draw circle
cv.circle(blank,(250,250),40,(0,0,255),thickness=3)
# To fill we can use -1 to the thickness
# img,center,radius,color,thicknesss,
cv.imshow('Circle',blank)
cv.waitKey(0)

# To draw Line
cv.line(blank,(0,0),(250,250),(255,255,255),thickness=2)
# img,pt1,pt2,color
cv.imshow('Line',blank)
cv.waitKey(0)

# To put a text
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255),2)
# img,text,origin,fontface,fontscale,color,thickness
cv.imshow("Text",blank)
cv.waitKey(0)
