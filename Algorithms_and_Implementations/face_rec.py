import os
import numpy as np
import cv2 as cv
people=['Elon Musk','ABD']
"""p=[]
for i in os.listdir("D:\Machine Learning\Libraries\OpenCV\Pics"):
    p.append(i)
print(p)"""
DIR=r'D:\Machine Learning\Libraries\OpenCV\Pics'
har=cv.CascadeClassifier('harsf.xml')

features=[] # img raise on the face
label=[]

def create_train(): # loop over folder and imag
    for person in people:
        path=os.path.join(DIR,person)
        label1=people.index(person)
        #label.append(label1)
        
        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            
            face_rect=har.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
            for (x,y,w,h) in face_rect:
                face_roi=gray[y:y+h,x:x+w]
                features.append(face_roi)
                label.append(label1)
create_train()
print(f'lenght of featurs ={len(features)}')
print(f' length of label ={len(label)}')
print("Training is done ---------------------------------")
features=np.array(features)
label=np.array(label)


face_recognizer=cv.face.LBPHFaceRecognizer_create()

# Train on f and L
face_recognizer.train(features,labels)
face_recpgnizer.save('face_trained.yml')
np.save('Features.npy',features)
np.save('Labels.npy',label)



    