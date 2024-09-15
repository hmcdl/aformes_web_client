import socket
import sys

def start_listening_log_socket(ip: str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((ip, 60606))  # связываем сокет с портом, где он будет ожидать сообщения
    sock.listen(1)  # указываем сколько может сокет принимать соединений
    print(f'Server is running  on host {ip}, port 60606, please, press ctrl+c to stop')
    conn, addr = sock.accept()
    print('connected:', addr)
    while True:
        # начинаем принимать соединения
        # выводим информацию о подключении
        data = conn.recv(1024).decode()  # принимаем данные от клиента, по 1024 байт
        if data != '':
            data = data.strip()
            print(str(data))
            if data.endswith('END OF JOB'):
                break
    conn.close()  # закрываем соединение
    input()

if __name__ == "__main__":
    ip = sys.argv[1]
    start_listening_log_socket(ip=ip)