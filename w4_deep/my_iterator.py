# *****************************
#          ИТЕРАТОРЫ
# *****************************


class SquareIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.current ** 2
        self.current += 1
        return result


class IndexIterable:
    def __init__(self, obj):
        self.obj = obj

    def __getitem__(self, index):
        return self.obj[index]


if __name__ == "__main__":
    num = SquareIterator(2, 8)
    print(next(num))
    print(next(num))
    print(next(num))

    for n in SquareIterator(1, 10):
        print(n)

    s_iter = IndexIterable('STR')
    print(s_iter[0])
    print(s_iter[1])
    print(s_iter[2])

    for s in IndexIterable('string'):
        print(s)

