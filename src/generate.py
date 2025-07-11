import numpy as np

def generate_text(model, seed, char_to_idx, idx_to_char, length=100):
    input_seq = [char_to_idx[c] for c in seed.lower()]
    generated = seed

    for _ in range(length):
        x = np.zeros((1, len(input_seq), len(char_to_idx)))
        for t, char_idx in enumerate(input_seq):
            x[0, t, char_idx] = 1.0
        preds = model.predict(x, verbose=0)[0]
        next_idx = np.argmax(preds)
        next_char = idx_to_char[next_idx]
        generated += next_char
        input_seq = input_seq[1:] + [next_idx]

    return generated