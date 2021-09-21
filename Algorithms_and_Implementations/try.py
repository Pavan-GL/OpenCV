import cv2 as cv
vd=cv.VideoCapture("D:\Machine Learning\Libraries\OpenCV\Videos\dog.mp4")
if (vd.isOpened()==False):
    print("Error")
while(vd.isOpened()==True):
    boolval,frame=vd.read()
    if boolval==True:
        cv.imshow("Video",frame)
        cv.waitKey(0)
        break
    else :
        break
vd.release()
cv.destroyAllWindows()