import requests
from requests import get
import time
from rss_parser import *
import asyncio
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
    rss_url = input("Введите URL потока RSS: ")
    response = get(rss_url)
    rss = Parser.parse(response.text)
    
async def readrss():
 for item in rss.channel.items:
     tts_input = item.description[:500] #item.description[:250]
     response_text = send_tts_request(tts_input)
     if response_text:
        print("Ответ сервера:", response_text)
     await asyncio.sleep(25)
asyncio.run(readrss())


