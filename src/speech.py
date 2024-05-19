
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Taking voice from my system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

# Speak Function
def speak(text):
    """
    This function takes text as argument and return voice

    Args:
        text(_type_): string
    """
    print("speaking ...")
    engine.say(text)
    engine.runAndWait()

# Speech Recognition function
def takeCommand():
    """
    This function takes voice as argument and return voice
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recongnizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}")

        except Exception as e:
            print("Say that again")
            return "None"
        
        return query
