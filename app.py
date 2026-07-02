import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image

model = tf.keras.models.load_model("room_classification_model.h5")

class_names = [
    "bathroom", "bedroom", "closet", "corridor",
    "dining_room", "garage", "kitchen",
    "livingroom", "lobby", "office", "pantry"
]

st.title(" Room Classification")
st.write("Upload image.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg","jpeg","png"],
    accept_multiple_files=True
)

if uploaded_file:

    for file in uploaded_file:

        img = Image.open(file)

        st.image(img, caption=file.name, width=300)

        img = img.resize((224,224))
        img = np.array(img)

        img = np.expand_dims(img, axis=0)

        prediction = model.predict(img, verbose=0)

        predicted_class = class_names[np.argmax(prediction)]
        confidence = np.max(prediction) * 100

        st.success(f"📌 {file.name}")
        st.write(f"**Room:** {predicted_class}")
        st.write(f"**Confidence:** {confidence:.2f}%")
        st.divider()