# *****************************
#       СОКЕТ. СЕРВЕР
# *****************************
import socket


# AF - address family
# потоковый сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# привязываем сокет к адресу сети и порту
sock.bind(("127.0.0.1", 10001))
# слушаем сокет
sock.listen(socket.SOMAXCONN)

# начинаем принимать соединения
conn, addr = sock.accept()
while True:
    # читаем из канала
    data = conn.recv(1024)
    if not data:
        break

    print(data.decode("utf-8"))

# закрываем канал и сокет
conn.close()
sock.close()
