import os
import cv2 as cv
import numpy as np
import DatabaseConnection as dbClass

class CreateTraining():

    def TrainAllImage(self):
        db = dbClass.DbConnection()
        res = db.getlistofidsfromdb()
        arr = np.array(res).ravel()
        self.people = []
        for name in arr:
            self.people.append(str(name))

    def create_train(self,people):
        for person in people:
            path = os.path.join(self.DIR, person)
            label = people.index(person)

            for img in os.listdir(path):
                img_path = os.path.join(path, img)

                img_array = cv.imread(img_path)
                if img_array is None:
                    continue

                gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

                # faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
                faces_rect = self.haar_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=6)

                print(img)
                for (x, y, w, h) in faces_rect:
                    faces_roi = gray[y:y + h, x:x + w]
                    self.features.append(faces_roi)
                    self.labels.append(label)


    def StartTraining(self,people):
        self.TrainAllImage();
        self.DIR= r'ImageBasic\Train'

        self.haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

        self.features = []
        self.labels = []
        self.create_train(self.people)
        self.features = np.array(self.features, dtype='object')
        self.labels = np.array(self.labels)

        face_recognizer = cv.face.LBPHFaceRecognizer_create(
            radius=1,
            neighbors=6,
            grid_x=8,
            grid_y=8)

        # Train the Recognizer on the features list and the labels list
        '''if os.path.exists('face_trained.yml'):
            print('model exists')
            face_recognizer.train(self.features, self.labels)
            face_recognizer.update(self.features,self.labels)
        else:
            print('model not exists')
'''
        face_recognizer.train(self.features, self.labels)
        face_recognizer.save('face_trained.yml')
        np.save('features.npy', self.features)
        np.save('labels.npy', self.labels)


CreateTraining().StartTraining(1)
#CreateTraining().StartTraining(['123','456','789'])
#CreateTraining().StartTraining(['123','888','333','111'])