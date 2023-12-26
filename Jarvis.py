import pyttsx3 as pt
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def ListenText():
    listener=sr.Recognizer()
    with sr.Microphone() as Source:
        print("Listening....")
        listener.adjust_for_ambient_noise(Source)
        audio=listener.listen(Source)
        try:
            print("Recognizing...")
            data=listener.recognize_google(audio)
            print(data)
        except sr.UnknownValueError as e:
            print("Not understandable !")

# ListenText() 

def SpeakText(x):
    engine=pt.init()
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    rate=engine.getProperty("rate")
    engine.setProperty("rate",140)
    engine.say(x)
    engine.runAndWait()

SpeakText("Hello Rahul Bhaiya")