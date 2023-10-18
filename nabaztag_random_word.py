import requests
import random
import time
def send_tts_request(tts_text):
    base_url = "http://api.wizz.cc/"
    params = {
        "sn": "MAC_ADDRESS_HERE",
        "token": "TOKEN_HERE",
        "server": "pixel",
        "tts": tts_text,
        "ws_acapela": "alyona"
    }

    headers = {
        "User-Agent": "Mozilla/5.0" 
    }

    try:
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()

        return response.text
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None

if __name__ == "__main__":
    while True:
        with open("russian.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
            tts_text=random.choice(words)
            print(tts_text)
            send_tts_request(tts_text)
            time.sleep(5)
