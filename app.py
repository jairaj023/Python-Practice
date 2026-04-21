import streamlit as st
from src.predict2 import predict_crop
# import numpy as np
# import tensorflow as tf
from PIL import Image
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras import layers, models
from src.predict import predict_disease
from precautions import precautions

st.set_page_config(page_title="Smart Crop Advisor", layout="centered")

st.title("🌱 Smart Crop Advisor System")

st.write("Enter soil and environmental details to get crop recommendation.")

# Inputs
N = st.number_input("Nitrogen (N)", min_value=0)
P = st.number_input("Phosphorus (P)", min_value=0)
K = st.number_input("Potassium (K)", min_value=0)
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
ph = st.number_input("pH Value")
rainfall = st.number_input("Rainfall (mm)")

# Prediction
if st.button("Predict Crop"):
    input_data = [N, P, K, temperature, humidity, ph, rainfall]

    result = predict_crop(input_data)

    st.success(f"🌾 Recommended Crop: {result}")


# For Upload Image/ Camera
st.title("🌿 Plant Disease Detection System")

# ADD THIS PART (replace old uploader)
option = st.radio("Choose Input Method:", ["Upload Image", "Use Camera"])

image = None

if option == "Upload Image":
    uploaded_file = st.file_uploader("Upload leaf image", type=["jpg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)

elif option == "Use Camera":
    camera_image = st.camera_input("Take a picture of the leaf")
    if camera_image:
        image = Image.open(camera_image)

# KEEP THIS (prediction part)
if image:
    st.image(image, caption="Input Image", width="stretch")

    with st.spinner("Analyzing image..."):
        disease, confidence = predict_disease(image)

    st.subheader(f"Prediction: {disease}")
    st.write(f"Confidence: {confidence*100:.2f}%")

    st.subheader("Precautions:")
    st.write(precautions[disease])
