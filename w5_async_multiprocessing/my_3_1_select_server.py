# *****************************
#  НЕБЛОКИРУЮЩИЙ ВЫВОД. СЕРВЕР
#
# кажется, в маке нету epoll
# у меня этот сервер не работает
#
# https://docs.python.org/3.6/library/select.html
# *****************************
import socket
import select


sock = socket.socket()
sock.bind(("", 10001))
sock.listen(socket.SOMAXCONN)

conn1, addr1 = sock.accept()
conn2, addr2 = sock.accept()

conn1.setblocking(0)
conn2.setblocking(0)

epoll = select.epoll()
epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)
epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)

conn_map = {
    conn1.fileno(): conn1,
    conn2.fileno(): conn2
}

# Неблокирующий ввод/вывод, обучающий пример
# Цикл обработки событий в epoll

while True:
    events = epoll.poll(1)

    for fileno, event in events:
        if event & select.EPOLLIN:
            # обработка чтения из сокета
            data = conn_map[fileno].recv(1024)
            print(data.decode("utf8"))
        elif event & select.EPOLLOUT:
            # обработка записи в сокет
            conn_map[fileno].send("pong".encode("utf8"))
