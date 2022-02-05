# *****************************
#       ОЧЕРЕДЬ ПОТОКОВ
# *****************************
from queue import Queue
from threading import Thread


def worker(q, n):
    """
    следующий элемент очереди будет передаваться в освободившийся поток
    :param q: элемент очереди
    :param n: номер потока
    """
    while True:
        # получаем значение из элемента очереди
        item = q.get()
        # если получили None - выходим из цикла
        if item is None:
            break
        print(f'process data {n}, {item}')


# создаём объект "очередь" из пяти элементов
q = Queue(5)
# создаём и стартуем потоки, которые будут запускать функцию worker и передавать в неё номер потока и элемент очереди
th1 = Thread(target=worker, args=(q, 1))
th2 = Thread(target=worker, args=(q, 2))
th1.start()
th2.start()

# в цикле заполняем очередь последовательными значениями
for i in range(50):
    q.put(i)

# добавляем в очередь значения, которые завершат worker
q.put(None)
q.put(None)

th1.join()
th2.join()
