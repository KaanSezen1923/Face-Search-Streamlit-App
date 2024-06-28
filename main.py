import streamlit as st
import pickle
import cv2
import face_recognition
import numpy as np
from PIL import Image

st.title("Face Searching")

img = st.file_uploader("Image", type=["jpg", "png", "jpeg"])

print("Loading Encode File")
with open("EncodeFile.p", "rb") as file:
    encodelistknownwithnames = pickle.load(file)
encodeListKnown, names = encodelistknownwithnames
print(names)
print("Loaded encoding file")

if img is not None:
    img = Image.open(img)
    img = np.array(img)
    

    faceloc = face_recognition.face_locations(img)
    encodeface = face_recognition.face_encodings(img)

    if len(encodeface) > 0:  # Check if any faces are found
        encodeface = encodeface[0]
        facedis = face_recognition.face_distance(encodeListKnown, encodeface)
        matchIndex = np.argmin(facedis)
        col1,col2=st.columns(2)
        with col1:
            st.image(img)
        if facedis[matchIndex] < 0.65:
            with col2:
                st.write(f"{names[matchIndex]}  %  {str(round(facedis[matchIndex],2))}" )
        else:
            with col2:
                st.write("Resim eşlenemedi.",str(round(facedis[matchIndex],2)))
    else:
        st.write("Yüz bulunamadı.")
