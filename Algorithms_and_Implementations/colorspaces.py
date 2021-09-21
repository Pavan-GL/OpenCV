import cv2 as cv
img=cv.imread("D:\Machine Learning\Libraries\OpenCV\Photos\park.jpg")
cv.imshow("Park",img)
#cv.waitKey(0)

# BGR to Gray
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GRAY",gray)
#cv.waitKey(0)

# BGR to HSV 
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)
#cv.waitKey(0)

# BGR to LAB
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)
#cv.waitKey(0)

# BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)
cv.waitKey(0)


