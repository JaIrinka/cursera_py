# *****************************
#          ГЕНЕРАТОР
# *****************************


def my_range_generator(top):
    current = 0
    while current < top:
        yield current
        current += 1


if __name__ == "__main__":
    counter = my_range_generator(3)
    print(counter)

    for it in counter:
        print(it)
