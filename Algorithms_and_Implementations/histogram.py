import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("D:\Machine Learning\Libraries\OpenCV\Photos\cats.jpg")
cv.imshow("Cat",img)
cv.waitKey(0)

gray_scale=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image",gray_scale)
cv.waitKey(0)

# To plot histogram
gray_hist=cv.calcHist([gray_scale],[0],None,[256],[0,256])
#img, channels(index),mask,histsize(nor of bins),range(All possible pixel values)
plt.figure()
plt.title("Gray Scale Histogram")
plt.xlabel("Bins")
plt.ylabel("# no of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
