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
