"""tarikozluk
Istanbul/Turkey"""

from telegram.ext import Updater, CommandHandler
import telebot
import cv2
import time
import os


recognizer=cv2.face.LBPHFaceRecognizer_create()     #method for the recognizing by openCV library
recognizer.read('Yml file for faces of user')
faceCascade=cv2.CascadeClassifier('face.xml')       #haar cascade xml file
path='Faces Folder'
cam=cv2.VideoCapture(0)
Botun_Tokeni = "Token of Your Bot"
ChatID= "Your Chat ID"
Araci= telebot.TeleBot(Botun_Tokeni)
while True:
    ret, frame=cam.read()
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gri,1.5,5)
    for (x,y,w,h) in faces:
        PredictedPerson,conf=recognizer.predict(gri[y:y+h,x:x+w])      #her bir yuzu kıyaslamak icin trainerla kıyaslıyoruz
        if (PredictedPerson==1):
            Person= "User"
        else:
            Person="undefined"
    cv2.imshow('pencere', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
if  Person =="User":
    Araci.send_message(ChatID, text=f'User is at the Computer')     #we understand, who is on computer
elif Person=="undefined":
    Araci.send_message(ChatID, text=f'Undefined Person is using your computer\n Waiting...')
def resimyolla(bot,Update):
    if Person == 'undefined':   #here we must see who is on computer as undefined
        camera = cv2.VideoCapture(0)
        return_value, Image = camera.read()
        cv2.imshow('Busted', Image)
        time.sleep(5)
        cv2.imwrite('undefinedPerson.jpg', Image)
        time.sleep(5)
        camera.release()
        cv2.destroyAllWindows()
    Resim2 = open(r'undefinedPerson.jpg', 'rb')
    time.sleep(5)
    bot.send_photo(ChatID, Resim2)      #sending the image of undefined person
    time.sleep(10)
def resimSil(bot, Update):
    bot.send_message(ChatID,text='The image of undefined person is removing from computer')
    os.remove('undefinedPerson.jpg')
def calistir():
    updater= Updater(Botun_Tokeni)
    dispatch=updater.dispatcher
    dispatch.add_handler(CommandHandler('Resimyolla',resimyolla))
    dispatch.add_handler(CommandHandler('Resimsil', resimSil))
    updater.start_polling()
    updater.idle()
if __name__=='__main__':
    calistir()

"""tarikozluk
Istanbul/Turkey
"""