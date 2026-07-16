from fastapi import FastAPI, UploadFile, File
import tensorflow as tf
import numpy as np
from PIL import Image

app = FastAPI()

model = tf.keras.models.load_model("room_classification_model.h5")

class_names = [
    "bathroom",
    "bedroom",
    "closet",
    "corridor",
    "dining_room",
    "garage",
    "kitchen",
    "livingroom",
    "lobby",
    "office",
    "pantry"
]


@app.get("/")
def home():
    return {"message":"Room Classification API is running."}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img = Image.open(file.file).convert("RGB")
    img = img.resize((224, 224))
    img = np.array(img).astype(np.float32)
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)

    predicted_index = int(np.argmax(prediction))
    predicted_class = class_names[predicted_index]
    confidence = float(np.max(prediction) * 100)


    return {
        "room_type": predicted_class,
        "confidence": round(confidence,2)
    }

