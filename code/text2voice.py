from gtts import gTTS
import os
from playsound import playsound


def speechTrans(data):
    speech = gTTS(data)
    speech.save("speech.mp3")
    # For Windows -
    # os.system("speech.mp3")
    # For Linux - 
    playsound('speech.mp3')
