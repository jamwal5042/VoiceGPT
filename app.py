import streamlit as st
from gtts import gTTS
import os

SUPPORTED_LANGUAGES = {
    'English': 'en',
    'Hindi': 'hi',
    'Tamil': 'ta',
    'Bengali': 'bn',
    'Telugu': 'te',
    'Gujarati': 'gu',
    'Marathi': 'mr',
    'Kannada': 'kn',
    'Punjabi': 'pa',
    'Urdu': 'ur'
}

st.set_page_config(page_title="VoiceGPT 🎙️", layout="centered")
st.title("🎙️ VoiceGPT - Text to Audio Converter")

uploaded_file = st.file_uploader("📄 Upload a text file", type=["txt"])

language = st.selectbox("🌐 Choose Language", list(SUPPORTED_LANGUAGES.keys()))
speed = st.radio("🔊 Voice Speed", ["Normal", "Slow"])

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8").strip()

    if content:
        if st.button("🎧 Convert and Play"):
            try:
                lang_code = SUPPORTED_LANGUAGES[language]
                slow = speed == "Slow"

                tts = gTTS(text=content, lang=lang_code, slow=slow)
                output_file = "output.mp3"
                tts.save(output_file)

                with open(output_file, "rb") as f:
                    audio_data = f.read()
                    st.audio(audio_data, format="audio/mp3")
                    st.download_button("⬇️ Download Audio", data=audio_data, file_name="output.mp3", mime="audio/mp3")

                st.success("✅ Audio generated successfully!")

            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ File is empty.")
