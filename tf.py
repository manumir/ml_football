#! /usr/bin/python3

import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data=pd.read_csv('finall.csv')
data=data[:10000]

y=data.pop('result')
x=data
x,y=np.array(x), np.array(y)

x, x_test, y, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42)

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(6),
  tf.keras.layers.Dense(36, activation=tf.nn.sigmoid),
  tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)
])
model.compile(optimizer='adam',
              loss='mse',
              metrics=['accuracy'])

model.fit(x, y, epochs=500,verbose=2)
print(model.evaluate(x_test, y_test))

