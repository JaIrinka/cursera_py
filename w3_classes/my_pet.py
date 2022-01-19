# *****************************
#    КЛАССЫ - НАСЛЕДОВАНИЕ
# https://docs.python.org/3/tutorial/classes.html#inheritance
# *****************************
import json


class Pet:

    def __init__(self, name):
        self._name = name


class Dog(Pet):

    def __init__(self, name, breed=None):
        super().__init__(name)
        self._breed = breed

    def say(self):
        return f'{self._name}: wow!'


class ExportJSON:
    def to_json(self):
        return json.dumps({
            "name": self._name,
            "breed": self._breed
        })


class ExDog(Dog, ExportJSON):
    pass


class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        super(Dog, self).__init__(name)
        self._breed = f'woolen dog {breed}'


my_dog = ExDog('Sharic', 'Haskey')
my_tax = WoolenDog('Zuchka', 'taxa')
#my_dog = Dog('Sharic', 'Haskey')
print(my_dog.say())
print(my_dog.to_json())
print(my_tax.to_json())

#print(dir(ExDog))
#print(ExDog.__mro__)
