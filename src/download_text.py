import requests

#The Adventures of Sherlock Holmes
url = "https://www.gutenberg.org/files/1661/1661-0.txt"
response = requests.get(url)

with open("../data/input.txt", "w", encoding="utf-8") as f:
    f.write(response.text)