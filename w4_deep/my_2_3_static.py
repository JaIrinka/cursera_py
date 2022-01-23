# *****************************
#   ДЕСКРИПТОР STATICMETHOD
# *****************************


class StaticMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner=None):
        return self.func


class Class:
    @staticmethod
    def original():
        """ стандартный проперти-декоратор """
        return 'original'

    @StaticMethod
    def custom_sugar():
        """ кастомный проперти-декоратор """
        return 'custom sugar'

    def _custom_pure():
        return 'custom pure'

    """ кастомный проперти-дескриптор """
    custom_pure = StaticMethod(_custom_pure)


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
