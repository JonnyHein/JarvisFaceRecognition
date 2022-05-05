import cv2
import numpy as np
import os 


class RecognizeFace:
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('/Users/jonnyhein/Apps/facialRecognition/trainer/trainer.yml')
        self.faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.id = 0
        self.names = ['None', 'Jonny'] 
        self.cam = cv2.VideoCapture(0)
    def foundOwner(self):
        foundOwner = False
        while True:
            ret, img = self.cam.read()

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            faces = self.faceCascade.detectMultiScale( 
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (30, 30),
            )
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                id, confidence = self.recognizer.predict(gray[y:y+h,x:x+w])
                
                # If confidence is less them 100 ==> "0" : perfect match 
                if (confidence < 100) and id == 1:
                    foundOwner = True
                    id = "Jonny Boi"
                
                else:
                    id = "Not Jonny"
                    confidence = "  {0}%".format(round(100 - confidence))
                
                cv2.putText(
                            img, 
                            str(id), 
                            (x+5,y-5), 
                            self.font, 
                            1, 
                            (255,255,255), 
                            2
                        )
                cv2.putText(
                            img, 
                            str(confidence), 
                            (x+5,y+h-5), 
                            self.font, 
                            1, 
                            (255,255,0), 
                            1
                        )  
            
            cv2.imshow('camera',img) 
            k = cv2.waitKey(10) & 0xff 
            if k == 27 or foundOwner:
                break

        self.cam.release()
        cv2.waitKey(1)
        cv2.waitKey(1)
        cv2.waitKey(1)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        cv2.waitKey(1)
        cv2.waitKey(1)
        cv2.waitKey(1)
        return True


