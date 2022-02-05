# *****************************
# СОЗДАНИЕ ПРОЦЕССОВ НАПРЯМУЮ ЧЕРЕЗ MULTIPROCESSING
#
# https://docs.python.org/3.6/library/multiprocessing.html
# *****************************
from multiprocessing import Process


def f(name):
    print(f'Hello, {name}')


# почему не работает без этого - я не поняла
if __name__ == '__main__':
    p = Process(target=f, args=("Uasya",))
    # внутри вызывается fork или аналог
    p.start()
    # внутри вызывается wait или аналог
    p.join()
