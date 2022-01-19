# *****************************
#    КОНТЕКСТНЫЙ МЕНЕДЖЕР
# *****************************
import time


class open_file:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, *args):
        self.file.close()


class suppress_exception:
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == self.exc_type:
            print("I'm fine...")
            return True


class timer:
    def __init__(self):
        self.start_time = time.time()

    def current_time(self):
        return time.time() - self.start_time

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Elapsed: {self.current_time()}')


if __name__ == "__main__":
    with open_file('log_file', 'w') as f:
        f.write("Inside open-file's context manager")

    with suppress_exception(ZeroDivisionError):
        bad_gay = 1 / 0

    with timer() as t:
        time.sleep(1)
        print(f'Current: {t.current_time()}')
        time.sleep(2)
