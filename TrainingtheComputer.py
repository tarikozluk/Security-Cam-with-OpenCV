"""
Firstly you need to save the pictures of your faces to any folder that python can see.
When you want to do it from python, you can use opencv for checking your face.

"""
import numpy as np
import cv2
import os
from PIL import Image


recognizer=cv2.face.LBPHFaceRecognizer_create()         #Method for Face Recognizing
faceCascade=cv2.CascadeClassifier(face.xml)
path='Faces folder'
""" Training and Understanding time for computer
    Computer must know how the faces are. Opencv recognizing modul give us this chance to understand. 
    From File where we added the pictures of face details computer can understand with Haar Cascade methods.
    """
def gettingimages(path):
    image_paths=[os.path.join(path,f) for f in os.listdir(path)]
    images=[]
    labels=[]
    for image_path in image_paths:
        image_pil=Image.open(image_path).convert('L')     #making gray the data
        image=np.array(image_pil,'uint8')
        etiket = int(os.path.split(image_path)[1].split(".")[0].replace("namedFace-",""))
        print(etiket)
        faces=faceCascade.detectMultiScale(image)
        for (x,y,w,h) in faces:
            images.append((image[y:y+h,x:x+w]))
            labels.append(etiket)
            cv2.imshow("photos loading...",image[y:y+h,x:x+w])
            cv2.waitKey(10)
    return images,labels
images,labels=gettingimages(path)
cv2.imshow('test',images[0])
cv2.waitKey(1)
recognizer.train(images,np.array(labels))


#Now computer knows the face and how it works. We must write these data on any yml file
#Face Recognizing method help us here with cv2.face.LBPHFaceRecognizer_create().write(file.yml)


recognizer.write('Creating .yml File for writing of the images that you saved at computer. ')
cv2.destroyAllWindows()