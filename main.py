import streamlit as st
import pickle
import cv2
import face_recognition
import numpy as np
from PIL import Image

st.set_page_config(page_title="FaceSearcher.ai", layout="centered")


st.title("Face Searching")


uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])


st.info("Loading encoded face data...")
try:
    with open("EncodeFile.p", "rb") as file:
        encodelistknownwithnames = pickle.load(file)
        encodeListKnown, names = encodelistknownwithnames
    st.success("Encoding file loaded successfully.")
except FileNotFoundError:
    st.error("Encoding file not found. Please check the file path.")
    st.stop()


if uploaded_image is not None:
    img = Image.open(uploaded_image)
    img_array = np.array(img)

    
    face_locations = face_recognition.face_locations(img_array)
    face_encodings = face_recognition.face_encodings(img_array)

    if face_encodings:
        encode_face = face_encodings[0]
        face_distances = face_recognition.face_distance(encodeListKnown, encode_face)
        match_index = np.argmin(face_distances)

        
        col1, col2 = st.columns(2)
        with col1:
            st.image(img, caption="Uploaded Image", use_column_width=True)

        
        if face_distances[match_index] <= 0.65:
            with col2:
                st.write(f"Match Found: {names[match_index]}")
                st.write(f"Confidence: {round((1 - face_distances[match_index]) * 100, 2)}")
        else:
            with col2:
                st.write("No match found.")
                st.write(f"Closest match distance: {round(face_distances[match_index], 2)}%")
    else:
        st.warning("No face detected in the uploaded image.")
else:
    st.info("Please upload an image to search for a face.")
