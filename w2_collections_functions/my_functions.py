#*****************************
#          ФУНКЦИИ
# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# https://docs.python.org/3/library/functions.html
# https://docs.python.org/3/howto/sorting.html
# https://docs.python.org/3/howto/functional.html
# https://docs.python.org/3/library/functools.html
#*****************************
from datetime import datetime
#from functools import reduce
#from functools import partial


# Аннотация типов (просто сахар, не кидает ошибок)
def get_seconds(multiply: int) -> int:
    """LOL _ DOCS"""
    return datetime.now().second


# Передача нескольких неименованных аргументов
def printer(*args):
    print(type(args))

    for a in args:
        print(a)


# Передача нескольких именованных аргументов
def printer_2(**kwargs):
    print(type(kwargs))

    for k, w in kwargs.items():
        print(f'{k} -> {w}')


def get_multiplyer(n):
    def inner(a):
        return a * n
    return inner


# возведение в квадрат
def squarify(a):
    return a ** 2


# проверка делимости на 3
def is_three(a):
    return not (a % 3)


names = ['cat1', 'cat2', 'axolotle', 'zebra', 'good dog', 'Forest cat']
simple_dict = {
    'first': 'FIRST',
    'second': ['pip', 'pibip']
}


multiplyer_two = get_multiplyer(2)
print(multiplyer_two(3))

# использование map
print(list(map(squarify, range(1, 20, 2))))

# использование filter
print(list(filter(is_three, range(20))))

# через lambda
print(list(map(lambda x: x ** 2, range(5))))
print(list(filter(lambda x: not (x % 3), range(100))))

# reduce
#print(int(reduce(lambda x, y: x * y, range(10))))

# zip
n1 = list(range(10))
n2 = list(range(5))
print(list(zip(n1, n2)))

#print(get_seconds('zoPA'))
#printer(1, 2, 3, 4, 5)
#printer(*names)
#printer_2(**simple_dict)
