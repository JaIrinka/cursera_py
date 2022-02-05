# *****************************
#           ПОТОК
#
# https://docs.python.org/3.6/library/threading.html
# *****************************
from threading import Thread


def f(name):
    print(f'hello, {name}')


class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f'Hello! {self.name}')


print('через передачу аргумента:')
th = Thread(target=f, args=("Huggy",))
th.start()
th.join()
print('------------------------------------')
print('через наследование:')
th_obj = PrintThread('Bunny')
th_obj.start()
th_obj.join()
