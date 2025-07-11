import requests

#The Adventures of Sherlock Holmes
def download_text():
    url = "https://www.gutenberg.org/files/1661/1661-0.txt"

    proxies = {
        "http": None,
        "https": None,
    }
    response = requests.get(url, proxies=proxies, timeout=30)

    with open("../data/input.txt", "w", encoding="utf-8") as f:
        f.write(response.text)