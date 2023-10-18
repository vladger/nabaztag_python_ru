import requests
import datetime
from datetime import *
import holidays
curdate=str(input("Введите дату в формате мм-дд-гггг "))
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
    ru_holidays=holidays.Russia()
    isholiday=curdate in ru_holidays
    holiday1=ru_holidays.get(curdate)
    if isholiday == True:
        tts_input=f"Сегодня праздник {holiday1}"
    else:
        tts_input="Сегодня нет праздников"
    print(tts_input)
    response_text = send_tts_request(tts_input)
    if response_text:
        print("Ответ сервера:", response_text)
