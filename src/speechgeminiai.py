import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS # For text to speech conversion
import base64

GOOGLE_API_KEY = "" # Google Gemini API Key
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY # Setting env variable


def voice_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio) # Using Google Speech Recognition
        print("You said:", text)
        return text
    
    except sr.UnknownValueError:
        print("Sorry voice not clear")

    except sr.RequestError as e:
        print(f"Could not request resule from Google Speech Recongnition server; {e}")

def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    tts.save("speech.mp3") # Saving Speech as mp3


def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_text)
    result = response.text    
    return result