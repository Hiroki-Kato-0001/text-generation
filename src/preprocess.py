import re

def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
def preprocess_text(text):
    # Delete information such as copyright
    start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
    end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"

    start_idx = text.find(start_marker)
    end_idx = text.find(end_marker)
    print(start_idx)
    print(end_idx)

    if start_idx != -1 and end_idx != -1:
        text = text[start_idx + len(start_marker):end_idx]

    # Convert all the text in lower case
    text = text.lower()

    # Delete line breaks, numbers, and symbols
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z ,.!?']", "", text)

    return text.strip()

if __name__ == "__main__":
    raw_text = load_text("../data/input.txt")
    cleaned = preprocess_text(raw_text)

    with open("../data/cleaned.txt", "w", encoding="utf-8") as f:
        f.write(cleaned)


