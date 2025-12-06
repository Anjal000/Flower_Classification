
import numpy as np;
import pandas as pd;
import cv2;
import matplotlib.pyplot as plt;
from PIL import Image;
import zipfile;
import os;
import keras;
from keras.preprocessing import image;
from tensorflow.keras import layers; 
from tensorflow.keras.models import load_model;
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img;
from tensorflow.keras.models import Sequential;
from tensorflow.keras.layers import Conv2D, MaxPooling2D;
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense;
from tensorflow.keras.optimizers import Adam;
from tensorflow.keras.utils import plot_model;
from flask import Flask, render_template, request
from tensorflow.keras.preprocessing import image
import tensorflow as tf;
import scipy;
import graphviz;
import pydot;


# img_size = 224
# batch = 32

# train_datagen = ImageDataGenerator(rescale=1. / 255, shear_range=0.2, 
#                                    zoom_range=0.2, horizontal_flip=True,
#                                    validation_split=0.2)

# test_datagen = ImageDataGenerator(rescale=1. / 255,
#                                   validation_split=0.2)

# train_datagen = train_datagen.flow_from_directory(base_dir,
#                                                   target_size=(
#                                                       img_size, img_size),
#                                                   subset='training',
#                                                   batch_size=batch,
#                                                   class_mode="sparse")
# test_datagen = test_datagen.flow_from_directory(base_dir,
#                                                 target_size=(
#                                                     img_size, img_size),
#                                                 subset='validation',
#                                                 batch_size=batch,
#                                                 class_mode="sparse")

# model = Sequential()
# model.add(Conv2D(filters=32, kernel_size=(5, 5), padding='same',
#                  activation='relu', input_shape=(224, 224, 3)))
# model.add(MaxPooling2D(pool_size=(2, 2)))


# model.add(Conv2D(filters=32, kernel_size=(3, 3),
#                  padding='same', activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))


# model.add(Conv2D(filters=32, kernel_size=(3, 3),
#                  padding='same', activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# model.add(Conv2D(filters=32, kernel_size=(3, 3),
#                  padding='same', activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# model.add(Flatten())
# model.add(Dense(512))
# model.add(Activation('relu'))
# model.add(Dense(8, activation="softmax"))

# model.summary()

# keras.utils.plot_model(
#     model,
#     show_shapes = True,
#     show_dtype = True,
#     show_layer_activations = True
# )

# model.compile(optimizer=tf.keras.optimizers.Adam(),
#               loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# epochs=30
# model.fit(train_datagen,epochs=epochs,validation_data=test_datagen)

# model.save('Model.h5')

app = Flask(__name__)
model = load_model('Model.h5')

labels = ['astilbe','bellflower', 'dandelion','marigold', 'rose', 'sunflower', 'tulip', 'water lily']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if not file:
        return "No file uploaded", 400

    file_path = os.path.join('static', file.filename)
    file.save(file_path)

    img = image.load_img(file_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)
    predicted_label = labels[np.argmax(prediction)]

    return render_template('index.html', prediction=predicted_label, image=file_path)

if __name__ == '__main__':
    app.run(debug=True)

