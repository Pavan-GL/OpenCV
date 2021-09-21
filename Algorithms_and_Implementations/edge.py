import numpy as np
import cv2 as cv
img=cv.imread("D:\Machine Learning\Libraries\OpenCV\Photos\cats.jpg")
cv.imshow("Cat",img)
cv.waitKey(0)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
cv.waitKey(0)

# Laplacian gradient
lap=cv.Laplacian(gray,cv.CV_64F)
#64 ddepth
lap=np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)
cv.waitKey(0)

# sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)

combined=cv.bitwise_or(sobelx,sobely)

cv.imshow("Sobel X",sobelx)
cv.imshow("Sobel Y",sobely)
cv.imshow("Combined X Sobel Y",combined)
cv.waitKey(0)

# canny
canny=cv.Canny(gray,150,175)
cv.imshow("Canny",canny)
cv.waitKey(0)