# Text Generation with LSTM

This is a character-level text generation project using LSTM in TensorFlow/Keras.  
It uses *The Adventures of Sherlock Holmes* from Project Gutenberg as training data.

## Structure

- `src/download_text.py` – Download raw text
- `src/preprocess.py` – Clean and normalize the text
- `src/model.py` – Build and train the LSTM model
- `src/generate.py` – Generate text from a trained model
- `main.py` – Complete workflow

## How to run

```bash
# Run from project root
python src/download_text.py
python src/preprocess.py
python main.py
