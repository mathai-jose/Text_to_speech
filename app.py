import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

def main():
    # Set your Gemini API key directly here
    api_key = 'AIzaSyBtIH4oUbbzCR2RmL1iG_DeMp7D90QEr18'  
    genai.configure(api_key=api_key)

    # Set up the Streamlit interface
    st.title("Text-to-Speech (TTS) Converter")

    # User input for text to convert to speech
    user_input = st.text_area(
        "Enter the text you want to convert to speech:",
        height=200
    )

    # Button to generate speech
    if st.button("Convert to Speech"):
        if user_input.strip():
            # Create a prompt for generating the spoken content
            prompt = f"""
            Based on the following text, convert it into speech:

            "{user_input}"
            """

            try:
                # Generate spoken text (this step assumes we use a text model to generate clearer content if needed)
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt)
                generated_text = response.text

                # Convert text to speech using gtts
                tts = gTTS(generated_text)
                tts.save("generated_speech.mp3")

                # Play the audio in Streamlit
                st.audio("generated_speech.mp3")

                # Provide download link for the audio file
                with open("generated_speech.mp3", "rb") as audio_file:
                    audio_bytes = audio_file.read()
                    st.download_button(
                        label="Download Speech as MP3",
                        data=audio_bytes,
                        file_name="generated_speech.mp3",
                        mime="audio/mpeg"
                    )

            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.warning("We couldn't generate the speech. Please try again later.")
        else:
            st.warning("Please provide some text to convert to speech.")

if __name__ == "__main__":
    main()
