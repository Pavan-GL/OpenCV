# To read video
import cv2 as cv
capture=cv.VideoCapture('D:\Machine Learning\Libraries\OpenCV\Videos\dog.mp4')
# 0 web cam,1 next connected camera(first cam)so on...
while True: # read video frame by frame
    isTrue,frame=capture.read() # reads video frame by frame return bool wheather it read or not
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'): # to stop
        break
capture.release() # to release capture point
cv.destroyAllWindows() 
# -215 video run out of frame