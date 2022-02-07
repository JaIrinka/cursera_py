# *****************************
# СОКЕТ. ПРОЦЕССЫ. ПОТОКИ. СЕРВЕР
#
# если запустить сервер, а потом не выключая его несколько раз запустить клиента
# можно увидеть, что отрабатывают три разных процесса на сервере
# *****************************
import socket
import threading
import multiprocessing
import os


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


def worker(sock):
    while True:
        # в цикле принимаем соединения
        conn, addr = sock.accept()
        print(f"pid: {os.getpid()}")
        # создаём и запускаем процесс для обработки соединения
        th = threading.Thread(target=process_request, args=(conn, addr))
        th.start()


if __name__ == "__main__":
    with socket.socket() as sock:
        sock.bind(("", 10001))
        sock.listen()

        # создаём список процессов (воркеров) из workers_count процессов, где в функции worker обрабатываются сокеты
        workers_count = 3
        workers_list = [multiprocessing.Process(target=worker, args=(sock,)) for _ in range(workers_count)]

        for w in workers_list:
            w.start()

        for w in workers_list:
            w.join()
