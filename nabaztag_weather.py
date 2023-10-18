import requests
import math
import pygismeteo
from pygismeteo import *
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
    city=input('Введите город для погоды: ')
    gm = pygismeteo.Gismeteo()
    search_results = gm.search.by_query(city)
    print(search_results)
    city_id = search_results[0].id
    current = gm.current.by_id(city_id)
    currenttemp = round(current.temperature.air.c)
    tts_input = f"Погода сейчас в {city}: {currenttemp}"
    response_text = send_tts_request(tts_input)
    if response_text:
        print("Ответ сервера:", response_text)
