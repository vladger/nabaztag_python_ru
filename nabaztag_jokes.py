import requests
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

def send_joke_request(ctype):
    base_url = "http://rzhunemogu.ru/RandJSON.aspx"
    params = {
        "CType": ctype,
    }

    headers = {
        "Accept": "application/json"
    }

    try:
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()

        return response.text
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None

if __name__ == "__main__":
    print("1 - Анекдот;")
    print("2 - Рассказы;")
    print("3 - Стишки;")
    print("4 - Афоризмы;")
    print("5 - Цитаты;")
    print("6 - Тосты;")
    print("8 - Статусы;")
    ctype=input("Выберите тип шутки: ")
    jokejson=send_joke_request(ctype)
    joketext=jokejson[12:][:-2]
    print(joketext)
    tts_input = joketext
    response_text = send_tts_request(tts_input)
    if response_text:
        print("Ответ сервера:", response_text)
