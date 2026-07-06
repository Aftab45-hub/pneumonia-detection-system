# 🩺 AI Pneumonia Detection System

An AI-powered web application that detects whether a chest X-ray image indicates **Pneumonia** or **Normal** using a Convolutional Neural Network (CNN).

---

## 📌 Project Overview

This project is developed using **Python, Flask, TensorFlow, HTML, CSS and JavaScript**.

The user uploads a chest X-ray image through the web interface. The Flask backend receives the image, preprocesses it and sends it to the trained CNN model. The model predicts whether the uploaded X-ray belongs to a **Normal** patient or a **Pneumonia** patient.

---

## 🚀 Features

- Upload Chest X-ray Images
- AI-based Pneumonia Detection
- CNN Deep Learning Model
- Flask Backend
- Responsive User Interface
- Real-time Prediction

---

## 🛠 Technologies Used

- Python
- Flask
- TensorFlow
- Keras
- NumPy
- HTML5
- CSS3
- JavaScript

---

## 📂 Project Structure

```
pneumonia-detection-system/
│
├── app.py
├── train.py
├── requirements.txt
├── README.md
│
├── model/
│
├── static/
│   ├── styles.css
│   └── script.js
│
├── templates/
│   └── index.html
│
└── uploaded_images/
```

---

## ⚙️ Working Process

1. User uploads a Chest X-ray image.

2. Flask receives the uploaded image.

3. The image is resized to **150 × 150 pixels**.

4. Pixel values are normalized.

5. CNN model processes the image.

6. Model predicts

- NORMAL
- PNEUMONIA

7. Prediction is displayed on the webpage.

---

## 🧠 CNN Architecture

- Conv2D
- MaxPooling2D
- Conv2D
- MaxPooling2D
- Flatten
- Dense Layer
- Output Layer (Sigmoid)

---

## 📊 Dataset

Dataset Source:

Chest X-Ray Images (Pneumonia)

Downloaded from Kaggle.

The dataset contains two classes:

- Normal
- Pneumonia

---

## ▶️ How to Run

Clone the repository

```
git clone https://github.com/Aftab45-hub/pneumonia-detection-system.git
```

Install dependencies

```
pip install -r requirements.txt
```

Train the model

```
python train.py
```

Run the application

```
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📈 Future Improvements

- Better CNN Architecture
- Mobile Responsive UI
- Confidence Score
- Medical Report Generation
- Multi Disease Detection

---

## 👨‍💻 Developer

**Aftab Alam**

B.Tech AIML Student

Artificial Intelligence & Machine Learning
