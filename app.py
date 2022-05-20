from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request, redirect, url_for
import tensorflow as tf
import numpy as np

app = Flask(__name__)

client = MongoClient(
    'mongodb+srv://******@cluster0.******.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.Dog_and_cat

import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('../models/model.h5')


x_test = np.array([[4, 6]])

y_predict = model.predict(x_test)

label = labels[y_predict[0].argmax()]
confidence = y_predict[0][y_predict[0].argmax()]
print('{} {:.2f}%'.format(label, confidence * 100)) #


####################################################

@app.route('/')
def home():

    return render_template('index.html', contents=contents)