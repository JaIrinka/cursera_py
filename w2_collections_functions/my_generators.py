#*****************************
#        ГЕНЕРАТОРЫ
#*****************************


def feb(numbers):
    a = b = 1
    for n in range(numbers):
        yield a
        a, b = b, a + b


def accumulator():
    total = 0
    while True:
        value = yield total
        print(f'Input: {value}')

        if not value:
            break

        total += value


generator = accumulator()
next(generator)

print(f'Accumulate: {generator.send(1)}')
print(f'Accumulate: {generator.send(10)}')
print(f'Accumulate: {generator.send(-3)}')
print(f'Accumulate: {generator.send(2)}')
