import socket
import subprocess

def execute_script(script_path):
    try:
        subprocess.run(['python', script_path])
    except Exception as e:
        print("Ошибка запуска:", e)

def main():
    host = '192.168.0.1'  #локальный IP-адрес
    port = 9000  #локальный порт

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    print(f"Прием запросов на {host}:{port}")

    while True:
        try:
            client, addr = server.accept()
            print(f"Подключение с : {addr}")

            client.send(b"Connected\n")
            client.close()

            script_to_execute = 'unattend_nabaztag_weather.py'  #Путь к файлу .py
            execute_script(script_to_execute)
        except KeyboardInterrupt:
            print("Сервер остановлен.")
            break
        except Exception as e:
            print("Ошибка:", e)

if __name__ == '__main__':
    main()
