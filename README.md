# 🏠 Room Classification Using EfficientNetB0

An AI-powered room classification system that automatically categorizes indoor room images into different room types using **EfficientNetB0** and **TensorFlow**. The project also includes a **Streamlit web application** that allows users to upload one or multiple room images for instant classification.

## 📌 Project Overview

Manually labeling room images for property listings can be time-consuming. This project automates the process by classifying uploaded images into predefined room categories such as Bedroom, Kitchen, Bathroom, Living Room, etc.

This project is designed as a proof of concept for platforms like **Rentoller**, where users upload multiple property images and the AI automatically identifies each room.

---

## 🚀 Features

- Classifies indoor room images into **11 room categories**
- Built using **Transfer Learning (EfficientNetB0)**
- Streamlit-based web interface
- Supports **multiple image uploads**
- Displays predicted room category with confidence score
- Evaluated using:
  - Test Accuracy
  - Confusion Matrix
  - Classification Report

---

## 🧠 Model

- **Architecture:** EfficientNetB0
- **Framework:** TensorFlow / Keras
- **Learning Technique:** Transfer Learning

---

## 📂 Room Categories

- Bathroom
- Bedroom
- Closet
- Corridor
- Dining Room
- Garage
- Kitchen
- Living Room
- Lobby
- Office
- Pantry

---

## 📊 Results

| Metric | Value |
|---------|-------|
| Test Accuracy | **80%** |
| Weighted F1-Score | **0.79** |

The model performs well on most room categories while maintaining good generalization on unseen images.

---

## 🛠️ Tech Stack

- Python
- TensorFlow
- Keras
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Pillow

---

## 📁 Project Structure

```
Room-Classification-Using-EfficientNetB0/
│
├── app.py
├── predict.py
├── room_classification.ipynb
├── rooms.ipynb
├── requirements.txt
├── room_classification_model.h5
├── README.md
└── screenshots/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/EddyRauthan/Room-Classification-Using-EfficientNetB0.git
```

Move into the project directory

```bash
cd Room-Classification-Using-EfficientNetB0
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📷 Screenshots

Add screenshots of:

- Streamlit Home Page
- Single Image Prediction
- Multiple Image Prediction
- Confusion Matrix

---

## 📚 Dataset

This project uses the **MIT Indoor Scene Recognition Dataset**, with selected room categories used for training and evaluation.

---

## 🔮 Future Improvements

- Increase dataset size for better accuracy
- Fine-tune EfficientNetB0
- Add more room categories
- Deploy the model on the cloud
- Integrate directly with Rentoller

---

## 👨‍💻 Author

**Eddy Rauthan**

GitHub: https://github.com/EddyRauthan
