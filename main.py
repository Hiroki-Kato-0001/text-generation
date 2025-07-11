from src.download_text import download_text
from src.preprocess import load_text
from src.model import build_model, train_model
from src.generate import generate_text
import numpy as np

# Prepare a data
text = load_text("data/cleaned.txt")

# Create a vocab dictionary
chars = sorted(list(set(text)))
char_to_idx = {c: i for i, c in enumerate(chars)}
idx_to_char = {i: c for c, i in char_to_idx.items()}

# Creqte sequences
seq_length = 40
step = 3
sequences = []
next_chars = []

for i in range(0, len(text) - seq_length, step):
    sequences.append(text[i: i + seq_length])
    next_chars.append(text[i + seq_length])

# Vectorize
X = np.zeros((len(sequences), seq_length, len(chars)), dtype=np.bool_)
y = np.zeros((len(sequences), len(chars)), dtype=np.bool_)
for i, seq in enumerate(sequences):
    for t, char in enumerate(seq):
        X[i, t, char_to_idx[char]] = 1
    y[i, char_to_idx[next_chars[i]]] = 1
X = X.astype("float32")
y = y.astype("float32")
print(np.sum(y, axis=1))  # すべて1であるべき
print(np.unique(np.sum(y, axis=1)))  # [1] のみであるべき
print(X[0])
print(y[0])


# Build and train a model
model = build_model(len(chars), seq_length)
print("X dtype:", X.dtype, "y dtype:", y.dtype)
print("X NaN:", np.isnan(X).any(), "X Inf:", np.isinf(X).any())
print("y NaN:", np.isnan(y).any(), "y Inf:", np.isinf(y).any())

train_model(model, X, y, epochs=10)

# Generate a text
seed = text[0:seq_length]
generated_text = generate_text(model, seed, char_to_idx, idx_to_char, length=300)

print("Generated text:\n")
print(generated_text)