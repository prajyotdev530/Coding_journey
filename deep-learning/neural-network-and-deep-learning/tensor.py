import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pandas as pd

w=tf.Variable(0,dtype=tf.float32)
optimizer=tf.keras.optimizers.Adam(learning_rate=0.1)
def train_step():
    with tf.GradientTape() as tape:
        cost=w**2+-10*w+25
    trainable_variables=[w]
    grads=tape.gradient(cost,trainable_variables)
    optimizer.apply_gradients(zip(grads,trainable_variables))
print(w)
train_step()
print(w)
for i in range(1000):
    train_step()
print(w)
