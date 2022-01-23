# *****************************
#   КЛАССЫ - 1, 2, 3, 4, 5
# https://docs.python.org/3.6/tutorial/classes.html
# https://docs.python.org/3/tutorial/classes.html
# https://python-course.eu/oop/object-oriented-programming.php
# *****************************


class Human:
    """Человеческий класс"""

    def __init__(self, name, age=0):
        self._name = name
        self._age = age

    def __repr__(self):
        print('__repr__ method')
        return self._name

    # когда-нибудь тут может измениться код! Говорить будем не принтом, а по-нормальному, например :)
    def _say(self, text):
        print(text)

    def say_name(self):
        self._say(f'My name is {self._name}')

    def say_your_old(self):
        self._say(f'I am {self._age} years old')

    # аннотация типа для красоты
    @staticmethod
    def is_age_valid(age: int):
        return 0 < age < 150


class Planet:
    """робочий класс"""
    count = 0

    #    def __new__(cls, *args, **kwargs):
    #        print('__new__ method')
    #        obj = super().__new__(cls)
    #        return obj

    def __init__(self, name, population=None):
        print('__init__ method Planet')
        self.name = name
        self.population = population or []
        Planet.count += 1

    # аннотация типа не обязательна!
    def add_human(self, human: Human):
        print(f'human added on {self.name} planet!')
        self.population.append(human)

    #    def __str__(self):
    #        print('__str__ method')
    #        return self.name


print(Planet)
print(dir(Planet))
print('------------------------------------1')

earth = Planet("Earth")
mars = Planet("Mars")
print('------------------------------------2')

print(earth)
print(earth, mars)
print('------------------------------------3')

print(dir(mars))
print('------------------------------------4')
print(earth.__dict__)
print('------------------------------------5')
print(Planet.__dict__)
print('------------------------------------6')

person1 = Human("Uasya")
earth.add_human(person1)
print(earth.population)
print('------------------------------------7')

person1.say_name()
person1.say_your_old()
