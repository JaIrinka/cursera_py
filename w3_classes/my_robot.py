# *****************************
#         КЛАССЫ - 5
# https://python-course.eu/oop/class-instance-attributes.php
# https://python-course.eu/oop/properties-vs-getters-and-setters.php
# https://ru.wikibooks.org/wiki/Python/Объектно-ориентированное_программирование_на_Python
# *****************************


class Robot:

    def __init__(self, power, magic=10):
        self._power = power
        self._magic = magic

    power = property()

    @power.setter
    def power(self, value):
        if value >= 0:
            self._power = value
        else:
            self._power = 0

    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print('make robot usless')
        del self._power

    @property
    def magic(self):
        # тут вычисления магии - только геттер :)
        return self._magic


robot = Robot(100)
print(robot.power)
robot.power = -10
print(robot.power)
robot.power = 1000000
print(robot.power)
