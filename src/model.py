from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np

def build_model(vocab_size, seq_length=40):
    model = Sequential()
    model.add(LSTM(256, input_shape=(seq_length, vocab_size)))
    model.add(Dense(vocab_size, activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam")
    return model

def train_model(model, X, y, epochs=20, batch_size=128):
      model.fit(X, y, epochs=epochs, batch_size=batch_size)