# *****************************
#    СОКЕТ. ТАЙМАУТЫ. КЛИЕНТ
# *****************************
import socket


with socket.create_connection(("127.0.0.1", 10001), 5) as sock:
    sock.settimeout(2)
    try:
        sock.sendall("TIME IS IT!".encode("utf-8"))
    except socket.timeout:
        print("set data timeout")
    except socket.error as ex:
        print("send data error:", ex)
