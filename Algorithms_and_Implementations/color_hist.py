import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("D:\Machine Learning\Libraries\OpenCV\Photos\cats.jpg")
cv.imshow("Cat",img)
cv.waitKey(0)
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.figure()
    plt.title("Color Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# no of pixels")
    plt.xlim([0,256])
    plt.show()