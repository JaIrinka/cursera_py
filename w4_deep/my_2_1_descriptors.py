# *****************************
#        ДЕСКРИПТОРЫ
# https://docs.python.org/3/howto/descriptor.html
# *****************************


class Descriptor:
    def __get__(self, instance, owner):
        print('get')

    def __set__(self, instance, value):
        print('set')

    def __delete__(self, instance):
        print('delete')


class Value:
    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(value):
        return value * 10

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = self._prepare_value(value)


class ImportantValue:
    def __init__(self, amount):
        self.amount = amount

    def __get__(self, instance, owner):
        return self.amount

    def __set__(self, instance, amount):
        with open('log_file', 'a') as f:
            f.write(f'Change amount {self.amount} -> {amount}\n')

        self.amount = amount


class Class:
    attr = Value()


class Account:
    amount = ImportantValue(100)


if __name__ == '__main__':
    instance = Class()
    instance.attr = 10
    print(instance.attr)

    a = Account()
    a.amount = 150
    print(a.amount)
