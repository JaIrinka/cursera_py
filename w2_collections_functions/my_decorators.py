#*****************************
#        ДЕКОРАТОРЫ
# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html
#*****************************


def identity_decorator(func):
    return func


def new_func_decorator(func):
    def new_func():
        print('NEW FUNC')
    return new_func


def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('logs', 'a') as log:
            data_string = ','.join(map(str, args))
            log.write(f'function: {func.__name__}\ndata: {data_string}\nresult: {result}\n\n')
        return result
    return wrapper


def super_logger(file):
    def logger(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file, 'a') as log:
                data_string = ','.join(map(str, args))
                log.write(f'function: {func.__name__}\ndata: {data_string}\nresult: {result}\n\n')
            return result
        return wrapper
    return logger


def italic(func):
    print('italic decorator')

    def wrapped():
        return '<i>' + func() + '</i>'
    return wrapped


def bold(func):
    print('bold decorator')

    def wrapped():
        return '<b>' + func() + '</b>'
    return wrapped


#    TESTS
@identity_decorator
def hello():
    print('hello!')


@new_func_decorator
def hello_2():
    print('Hello')


@super_logger('logs')
def summator(numbers):
    return sum(numbers)


@bold
@italic
def hello_3():
    return 'HELLO!'


hello()
hello_2()
print(hello_3())
summator(list(range(16)))
