import cv2 as cv
img=cv.imread("D:\Machine Learning\Libraries\OpenCV\Photos\cats.jpg")
cv.imshow("Cat",img)
cv.waitKey(0)

# Averaging
avg=cv.blur(img,(3,3))
cv.imshow("Blur",avg)
cv.waitKey(0)

#Gaussian 
gauss=cv.GaussianBlur(img,(3,3),0)
# 0 Standard deviation
cv.imshow("Gaussian Blur",gauss)
cv.waitKey(0)

# Median Blur
# advance and clear reduce more voice
median=cv.medianBlur(img,3)
cv.imshow("Median Blur",median)
cv.waitKey(0)

#bilateral
bil=cv.bilateralFilter(img,5,1,5,15)
cv.imshow("Bilateral",img)
cv.waitKey(0)