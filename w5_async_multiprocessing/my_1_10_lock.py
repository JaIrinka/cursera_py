# *****************************
#        БЛОКИРОВКИ
# RLock = reenterable lock
# *****************************
import threading


class Point:
    """
    пример создания класса, использующего мьютекс (способ блокировки через внутренний объект блокировки)
    помогает избежать гонки:
    когда один поток пишет, а второй в то же самое время пытается читать и считывает в итоге хрень
    """
    def __init__(self):
        self._mutex = threading.RLock()
        self._x = 0
        self._y = 0

    def get(self):
        with self._mutex:
            return self._x, self._y

    def set(self, x, y):
        with self._mutex:
            self._x = x
            self._y = y


# другой способ блокировки
a = threading.RLock()
b = threading.RLock()


def foo():
    try:
        # захватываем блокировки
        a.acquire()
        b.acquire()
    finally:
        # отпускаем блокировки
        a.release()
        b.release()


class Queue:
    """
    реализация очереди через условные переменные
    """
    def __init__(self, size):
        self._size = size
        self._queue = []
        self._mutex = threading.RLock()
        self._empty = threading.Condition(self._mutex)
        self._full = threading.Condition(self._mutex)

    def put(self, val):
        with self._full:
            while len(self._queue) >= self._size:
                self._full.wait()

            self._queue.append(val)
            self._empty.notify()

    def get(self):
        with self._empty:
            while len(self._queue) == 0:
                self._empty.wait()

            ret = self._queue.pop()
            self._full.notify()
            return ret
