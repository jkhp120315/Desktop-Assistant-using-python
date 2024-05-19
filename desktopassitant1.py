from src.speech import *
import streamlit as st

if __name__ == "__main__":
    st.title("Desktop Assistant System")
    
    speak("Hello, what can i do for you?")
    query = takeCommand().lower()

    if "youtube" in query:
        speak("Opening Youtube")
        webbrowser.open("youtube.com")

    elif "google" in query:
        speak("Opening Google")
        webbrowser.open("google.com")

    elif "netflix" in query:
        speak("Opening Netflix")
        webbrowser.open("netflix.com")

    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir right now time is {strTime}")

    elif "goodbye" in query:
        speak("Terminating the app")
        exit()