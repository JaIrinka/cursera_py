# *****************************
#       СОКЕТ. КЛИЕНТ
# *****************************
import socket


with socket.create_connection(("127.0.0.1", 10001)) as sock:
    sock.sendall("pinо CUCUMBERIONIO!".encode("utf-8"))
