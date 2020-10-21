import requests as req
import mail1
import scrapper
import handleFile
import text2voice as t2v
import scrapper
import x
from bs4 import BeautifulSoup 

import speech_recognition as sr

def stot():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Speak......")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except Exception as e:
            return "Voice not recognised Speak again"
            exit(0)


t2v.speechTrans("Tell the topic")
topic=stot()
# topic='kolkata'
print(topic)
data=scrapper.get(topic)
print(data)
print("1. Speak 1 for storing it in text file")
print("2. Speak 2 for getting it mailed to your mail id")
print("3. Speak 3 for summarizing the text")
print("4. Speak 4 for speech output of summarized text")
option=int(input())
t2v.speechTrans(str(option))

s=x.summarize(data)

if(option=="1" or option=="one" or option==1):
    print(handleFile.CreateFile(s,topic))
if(option==2 or option=="two" or  option=="2"):
    handleFile.CreateFile(s,topic)
    mail1.sendMail(topic)
if option==3:
    print(s)
if option==4:
    t2v.speechTrans(s)