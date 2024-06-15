from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("models/gemini-pro-vision")

def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
        return response.text
    else:
        response=model.generate_content(image)
        return response.text

st.set_page_config(page_title="Vision")

st.header("Vision Unleashed")

input=st.text_input("Input: ",key="input")

# File uploader for image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image file
    image = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)
else:
    st.write("Please upload an image to display.")

submit=st.button("Tell me about the image")

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The answer is")
    st.write(response)