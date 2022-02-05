# *****************************
# СОЗДАНИЕ ПРОЦЕССОВ ЧЕРЕЗ НАСЛЕДОВАНИЕ ОТ PROCESS
# *****************************
from multiprocessing import Process


class PrintProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f'hello, {self.name}')


if __name__ == '__main__':
    p = PrintProcess("Banana Mamma")
    # внутри вызывается fork или аналог
    p.start()
    # внутри вызывается wait или аналог
    p.join()
