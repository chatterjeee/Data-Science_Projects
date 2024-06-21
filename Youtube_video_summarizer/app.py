import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt=''' Provide me a detailed summary of this transcript in less than 250 words.

'''
def generate_gemini_content(transcript,prompt):
    model= genai.GenerativeModel("gemini-pro")
    response= model.generate_content(transcript+prompt)
    return response.text

def extract_transcript_details(url):
    try:
        video_id=url.split("=")[1]
        transcript_text= YouTubeTranscriptApi.get_transcript(video_id)
        print(transcript_text)
        transcript=" "
        for i in transcript_text:
            transcript= transcript + " " + i["text"]

        return transcript

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

st.title("Youtube transcipt summarizer")

url= st.text_input("Enter the youtube link")
if url:
    video_id=url.split("=")[1]
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg",use_column_width=True)

if st.button("Summarise the video transcripts"):
    x=extract_transcript_details(url)
    summary=generate_gemini_content(x,prompt)
    st.write(summary)






