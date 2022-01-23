# *****************************
#        METACLASS
# https://docs.python.org/3/reference/datamodel.html
# *****************************


class Class:
    pass


obj = Class()

print(type(obj))
print(type(Class))
print(type(type))

print(issubclass(Class, type))
print(issubclass(Class, object))
print('------------------------------------')


# ВОТ ЭТО ЧТО-ТО ПОКАЗЫВАЕТ, НО ПОКА НЕ ПОНЯТНО
# "Чтобы понять, как вообще классы задаются"
def dummy_factory():
    class Class:
        pass

    return Class


Dummy = dummy_factory()

print(Dummy() is Dummy())
print('------------------------------------')


# тут мы создаём новый класс, что по сути новый тип
NewClass = type('NewClass', (), {})

print(NewClass)
print(NewClass())
print('------------------------------------')


# TYPE - САМЫЙ ПЕРВЫЙ МЕТАКЛАСС, ВСЁ ЧТО НАСЛЕДУЕТСЯ ОТ НЕГО - ТОЖЕ МЕТАКЛАСС


class Meta(type):
    """ метакласс, в котором меняем метод создания класса """
    def __new__(cls, name, parents, attrs):
        print(f'Creating: {name}')

        if 'class_id' not in attrs:
            attrs['class_id'] = name.lower()

        return super().__new__(cls, name, parents, attrs)


class A(metaclass=Meta):
    pass


print(f'A.class_id: {A.class_id}')
print('------------------------------------')


class Meta2(type):
    """ метакласс, в котором меняем метод инициализации объекта - или нет... """
    def __init__(cls, name, bases, attr):
        print(f'Initialising: {name}')

        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            cls.registry[name.lower()] = cls

        super().__init__(name, bases, attr)


class Base(metaclass=Meta2):
    pass


class B(Base):
    pass


class C(Base):
    pass


print(Base.registry)
print(Base.__subclasses__())
print('------------------------------------')
