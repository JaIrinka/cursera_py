# *****************************
#    СОКЕТ. ПОТОКИ. СЕРВЕР
# *****************************
import socket
import threading


def process_request(conn, addr):
    print(f"connection with {addr}")
    # устанавливаем таймаут
    conn.settimeout(5)
    with conn:
        while True:
            try:
                data = conn.recv(1024)
            except socket.timeout:
                # если в течение 5 секунд ничего не пришло - завершаем соединение
                print("close connection by timeout")
                break

            if not data:
                break
            print(data.decode("utf-8"))


with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()
    while True:
        # в цикле принимаем соединения
        conn, addr = sock.accept()
        # создаём и запускаем процесс для обработки соединения
        th = threading.Thread(target=process_request, args=(conn, addr))
        th.start()

