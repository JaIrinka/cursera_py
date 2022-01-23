# *****************************
#    ДЕСКРИПТОР CLASSMETHOD
# *****************************


class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner=None):
        if owner is None:
            owner = type(instance)

        def new_func(*args, **kwargs):
            return self.func(owner, *args, **kwargs)

        return new_func


class Class:
    @classmethod
    def original(self):
        """ стандартный классметод-декоратор """
        return 'original'

    @ClassMethod
    def custom_sugar(self):
        """ кастомный классметод-декоратор """
        return 'custom sugar'

    def _custom_pure(self):
        return 'custom pure'

    """ кастомный классметод-дескриптор """
    custom_pure = ClassMethod(_custom_pure)


if __name__ == '__main__':
    obj = Class()

    print(obj.original)
    print(obj.original())
    print(obj.custom_sugar())
    print(obj.custom_pure())
    print(Class.original)
    print(Class.original())
    print(Class.custom_sugar())
    print(Class.custom_pure())
