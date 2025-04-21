import streamlit as st
import requests
import time
import base64
from io import BytesIO

# Hugging Face API Key

def generate_image(prompt):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    HEADERS = {"Authorization": "Bearer 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"}  # Replace with your API key

    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.content  # Return image bytes
    else:
        st.error("Failed to generate image. Try again!")
        return None

# Streamlit UI
st.header("_Enter your prompt to generate the image:_")
st.write("🔥 Watch your imagination come to life! 🔥")

prompt = st.chat_input("Enter your prompt")

if prompt:
    st.chat_message("human").write(prompt)
    
    with st.spinner("Generating Image..."):
        time.sleep(3)
        image_bytes = generate_image(prompt)
        
        if image_bytes:
            image = BytesIO(image_bytes)
            st.image(image, caption="Generated Image", use_column_width=True)

            # Add Download Button
            st.download_button(
                label="⬇️ Download Image",
                data=image_bytes,
                file_name="Generated-image-Deepvison.png",
                mime="image/png"
            )

# ---- API FUNCTION ----
