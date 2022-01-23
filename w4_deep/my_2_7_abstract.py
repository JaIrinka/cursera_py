# *****************************
#      АБСТРАКТНЫЕ КЛАССЫ
# *****************************
from abc import ABCMeta, abstractmethod


class Sender(metaclass=ABCMeta):
    """от этого класса только наследуемся, он абстрактный"""
    @abstractmethod
    def send(self):
        """ничего не происходит, но этот метод надо переопределить в своём классе"""


class Child(Sender):
    def send(self):
        print('что-то определили')


print(Child())
print('------------------------------------')


# PYTHON STYLE

class PythonWay:
    def send(self):
        """этот метод у класса-наследника нужно будет переопределить, чтобы можно было создать объект"""
        raise NotImplementedError


class Child2(PythonWay):
    def send(self):
        print('Переопределили')


print(Child2())
