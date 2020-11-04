from gtts import gTTS
import os
import pyttsx3
from playsound import playsound

'''
def speechTrans(data):
    speech = gTTS(data)
    speech.save("speech.mp3")
    # For Windows -
    os.system("speech.mp3")
    # For Linux - 
    #playsound('speech.mp3')
'''

def speechTrans(data):
    engine = pyttsx3.init()
    engine.say(data)
    engine.runAndWait()