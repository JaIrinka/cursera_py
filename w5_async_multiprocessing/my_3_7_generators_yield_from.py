# *****************************
#          ГЕНЕРАТОР
#
# PEP 380
# https://www.python.org/dev/peps/pep-0380/
# *****************************


def chain(x_iterable, y_iterable):
    yield from x_iterable
    yield from y_iterable


def the_same_chain(x_iterable, y_iterable):
    for x in x_iterable:
        yield x

    for y in y_iterable:
        yield y


if __name__ == "__main__":
    a = {1, 2, 3, 4}
    b = (27, 37, 47, 57, 67)

    for i in chain(a, b):
        print(i)
