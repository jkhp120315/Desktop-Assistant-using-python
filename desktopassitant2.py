import streamlit as st
from src.speechgeminiai import *
import base64

def main():
    st.title("Multilingual AI Assistant")
    if st.button("Ask me anything"):
        with st.spinner("Listen"):
            text = voice_input()
            response = llm_model_object(text)
            text_to_speech(response)

            # Display audio player and download link
            audio_file = open("speech.mp3", 'rb')
            audio_bytes = audio_file.read()
            
            st.text_area(label="Response:", value=response, height=350)
            st.audio(audio_bytes, format='audio/mp3')
      #      autoplay_audio("speech.mp3")

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

main()