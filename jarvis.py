from FaceRecognize import recognizeFace
import os
import cv2
import numpy as np
import time
from playsound import playsound
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play
import threading


class _TTS:

    engine = None
    rate = None
    def __init__(self):
        self.engine = pyttsx3.init()


    def start(self,text_):
        self.engine.say(text_)
        self.engine.runAndWait()

def playACDC():
    playsound("/Users/jonnyhein/Apps/jarvisControl/Sounds/ACDC.mp3", False)
def jarvisWelcome():
    tts = _TTS()
    tts.start("Welcome back sir. all services will be prepared in a few minutes.. for now. grab a cup of coffee and prepare to have a good day.... I love you")
    #del(tts)
def JonnyIntro():
    os.system("clear")
    playACDC()
    p = threading.Thread(target=jarvisWelcome)
    p.start()
    print("Welcome Jonny")
    while True:
        time.sleep(5)
print("hi")
this = recognizeFace.RecognizeFace()
found = this.foundOwner()
if found:
    del(this)
    JonnyIntro()

