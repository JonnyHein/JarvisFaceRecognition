# Python program to translate 
# speech to text and text to speech 
  

import speech_recognition as sr 
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
  
def runJarvis():
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
def facialRecognition():
    SpeakText("Running facial recognition")
    runJarvis()
def weather():
    SpeakText("It is 34 degrees and cloudy")
def date():
    SpeakText("today is Sunday the 27th of december")
def na():
    SpeakText("Im sorry i dont understand those commands yet. Shall i learn them?")
# Initialize the recognizer  
r = sr.Recognizer()  
switcher = {
        "facial recognition": facialRecognition,
        "date today": date,
        "weather": weather,
        "NA": na
}
# Function to convert text to 
# speech 
def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
      
      
# Loop infinitely for user to 
# speak 
  
while(1):     
      
    # Exception handling to handle 
    # exceptions at the runtime 
    try: 
          
        # use the microphone as source for input. 
        with sr.Microphone() as source2: 
              
            # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
            r.adjust_for_ambient_noise(source2, duration=0.2) 
              
            #listens for the user's input  
            audio2 = r.listen(source2) 
              
            # Using ggogle to recognize audio 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower() 
            for key in switcher.keys():
                if key in MyText:
                    switcher[key]()
                    break
            
            
            print("Did you say "+MyText) 
              
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("unknown error occured") 