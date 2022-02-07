# *****************************
#       СОКЕТ. СЕРВЕР
# *****************************
import socket


with socket.socket() as sock:
    # привязываем сокет к адресу сети и порту
    sock.bind(("", 10001))
    # слушаем сокет
    sock.listen()

    while True:
        # начинаем принимать соединения
        conn, addr = sock.accept()
        while True:
            # читаем из канала
            data = conn.recv(1024)
            if not data:
                break

            print(data.decode("utf-8"))
