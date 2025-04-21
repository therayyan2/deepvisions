import streamlit as st
import requests
import time
from PIL import Image
from io import BytesIO

# Set page config (optional)
st.set_page_config(page_title="DeepVision", page_icon="🔍", layout="wide")

# Main content
st.title("Welcome to DeepVision")
st.write("AI-powered image generation at its best! 🚀")

def generate_image(prompt):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    HEADERS = {"Authorization": "Bearer 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"}  # Replace with your API key

    with st.spinner("Generating Image..."):
        response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
        st.subheader("Generated Image...")
    
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))  # Convert response to image
            st.image(image, caption=prompt)
        else:
            st.error(f"❌ Image generation failed! Error Code: {response.status_code}")
            st.write(response.text)  # Print error details



fantasy, scenery, city, Ancivilization = st.columns(4)


with scenery:
    if st.button("A 15 Year old boy is riding the horse very Agressively and confidently"):
        generate_image("A 15 Year old boy is riding the horse very Agressively and confidently")


with city:
    if st.button("A futuristic neon-lit city with flying cars and holographic billboards at night"):
        generate_image("A futuristic neon-lit city with flying cars and holographic billboards at night")

with Ancivilization:
    if st.button("A lost city in the jungle, covered in vines, with golden temples and mysterious artifacts"):
        generate_image("A lost city in the jungle, covered in vines, with golden temples and mysterious artifacts")

with fantasy:
    if st.button("A mystical floating island with waterfalls, glowing trees, and a giant moon"):
        generate_image("A mystical floating island with waterfalls, glowing trees, and a giant moon")





