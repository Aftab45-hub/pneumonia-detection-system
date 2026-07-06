import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

UPLOAD_FOLDER = 'uploaded_images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

MODEL_PATH = 'model/cnn_model.h5'

model = None

try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model Loaded")
except:
    print("Model Not Found")

def model_predict(img_path, model):

    img = image.load_img(
        img_path,
        target_size=(150,150)
    )

    img = image.img_to_array(img)

    img = np.expand_dims(img, axis=0)

    img = img/255.0

    pred = model.predict(img)

    if pred[0] < 0.5:
        return "NORMAL"

    return "PNEUMONIA"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    if model is None:
        return jsonify({
            "prediction":"MODEL ERROR"
        })

    file = request.files['file']

    path = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(path)

    result = model_predict(
        path,
        model
    )

    os.remove(path)

    return jsonify({
        "prediction":result
    })


if __name__=="__main__":
    app.run(debug=True)