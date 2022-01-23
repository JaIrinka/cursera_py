# *****************************
#     ДЕСКРИПТОР PROPERTY
# *****************************


class Property:
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner=None):
        if instance is None:
            return self

        return self.getter(instance)


class Class:
    @property
    def original(self):
        """ стандартный проперти-декоратор """
        return 'original'

    @Property
    def custom_sugar(self):
        """ кастомный проперти-декоратор """
        return 'custom sugar'

    def custom_pure(self):
        return 'custom pure'

    """ кастомный проперти-дескриптор """
    custom_pure = Property(custom_pure)


if __name__ == '__main__':
    obj = Class()

    print(obj.original)
    print(obj.custom_sugar)
    print(obj.custom_pure)
