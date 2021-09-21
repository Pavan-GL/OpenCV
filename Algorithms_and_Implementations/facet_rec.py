import numpy as np
import cv2 as cv
people=['Elon Musk','ABD']
har=cv.CascadeClassifier('harsf.xml')
#features=np.load('features.npy, allow_pickle=True')
#label=np.load('label.npy')
face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img=cv.imread(r'D:\Machine Learning\Libraries\OpenCV\Pics\ABD\images(1).jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
face_rect=har.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
for (x,y,w,h) in face_rect:
    face_roi=gray[y:y+h,x:x+w]
    label,confidence=face_recognizer.predict(face_roi)
    print(f'label={label} with confidence of {confidence}')
cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.reactangle(img,(x,y)(x+w,y+h),(0,255,0),thickness=2)
cv.imshow("Dected img",img)
cv.waitKey(0)