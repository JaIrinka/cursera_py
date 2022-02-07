# *****************************
#       СОКЕТ. КЛИЕНТ
#
# https://docs.python.org/3.6/library/socket.html
# *****************************
import socket


# создаём потоковый сокет, привязываем к адресу и отправляем сообщение
sock = socket.socket()
sock.connect(("127.0.0.1", 10001))
sock.sendall("pingogo".encode("utf-8"))
sock.close()

# более короткая запись (чтобы работала c первым сервером надо предыдущюю закомментить)
sock = socket.create_connection(("127.0.0.1", 10001))
sock.sendall("pinо CUCUMBER!".encode("utf-8"))
sock.close()
