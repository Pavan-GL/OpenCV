# Existing video
import cv2 as cv
def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale) # img
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA) 
# Resizing an image needs a way to calculate pixel values for the new image from the original one. 
# The five such interpolation methods provided with OpenCV are INTER_NEAREST , INTER_LINEAR , 
# INTER_AREA , INTER_CUBIC , and INTER_LANCZOS4


capture=cv.VideoCapture('D:\Machine Learning\Libraries\OpenCV\Videos\dog.mp4')

# 0 web cam,1 next connected camera(first cam)so on...
while True: # read video frame by frame
    isTrue,frame=capture.read() # reads video frame by frame return bool wheather it read or not
    frame_resize=rescale(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video_resized',frame_resize)
    
    if cv.waitKey(20) & 0xFF==ord('d'): # to stop
        break
capture.release() # to release capture point
cv.destroyAllWindows() 
# -215 video run out of frame