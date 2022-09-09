# pylint:disable=no-member

import numpy as np
import cv2 as cv
import DatabaseConnection as dbClass

CapimageStorLoc = "CapturedImage"
db = dbClass.DbConnection()
res = db.getlistofidsfromdb()
arr = np.array(res).ravel()
people = []
haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

class face_recog():
    def facePrediction(self,imgpath):

        db = dbClass.DbConnection()
        res = db.getlistofidsfromdb()
        arr = np.array(res).ravel()
        people = []

        print(imgpath)
        for name in arr:
            people.append(str(name))

        # features = np.load('features.npy', allow_pickle=True)
        # labels = np.load('labels.npy')

        face_recognizer = cv.face.LBPHFaceRecognizer_create(
            radius=1,
            neighbors=6,
            grid_x=8,
            grid_y=8)
        face_recognizer.read('face_trained.yml')

        img = cv.imread(imgpath)

        # img = cv.resize(img,(300,300))
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        #cv.imshow('Person', gray)
        RollNumber = ""
        # Detect the face in the image
        faces_rect = haar_cascade.detectMultiScale(gray,  1.3, 6)
        print(len(faces_rect))
        if(len(faces_rect) > 0):
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y + h, x:x + w]
                print(faces_rect)
                label, confidence = face_recognizer.predict(faces_roi)
                print(label)
                print(people)
                names = db.getnamefromrollno(people[label])
                b = [i for sub in names for i in sub]
                print(b)
                print(f' with a confidence of {confidence}')
                RollNumber = str(people[label])
                '''cv.putText(img, str(" ".join(b)), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
                cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)'''
        else:
            RollNumber = -1
        return RollNumber
        '''cv.imshow('Detected Face', img)

        cv.waitKey(0)'''

    def DetectFace(self,path):
        print(path)
        img = cv.imread(path)
        # convert to gray scale of each frames
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Detects faces of different sizes in the input image
        faces = haar_cascade.detectMultiScale(gray, 1.3, 6)
        print(faces)
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                faces = img[y:y + h, x:x + w]
                grayCroppedImage = cv.cvtColor(faces, cv.COLOR_BGR2GRAY)
                fileName = rf"{CapimageStorLoc}/CroppedImage_1.jpg"
                faces = cv.resize(faces, (400, 400))
                cv.imwrite(filename=fileName, img=faces)
                return fileName

    def DetectFaceWithParentFolder(self,path,Parentfolder):
        print(path)
        img = cv.imread(path)
        # convert to gray scale of each frames
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Detects faces of different sizes in the input image
        faces = haar_cascade.detectMultiScale(gray, 1.3, 6)
        print(faces)
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                faces = img[y:y + h, x:x + w]
                grayCroppedImage = cv.cvtColor(faces, cv.COLOR_BGR2GRAY)
                fileName = rf"{Parentfolder}/CroppedImage.jpg"
                faces = cv.resize(faces, (400, 400))
                cv.imwrite(filename=fileName, img=faces)
                return fileName



#face_recog().facePrediction(r'ImageBasic\test23.jpg')