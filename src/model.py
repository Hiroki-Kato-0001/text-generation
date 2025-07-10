from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np

def build_model(vocab_size, seq_length=40):
    model = Sequential()
    model.add(LSTM(128, input_shape, activation="softmax"))
    model.add(Dense(vocab_size, activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam")
    return model