# *****************************
#           SLOTS
# *****************************


class Class:
    __slots__ = ['anakin']

    def __init__(self):
        self.anakin = 'the chosen one'


obj = Class()

obj.luke = 'the chosen too'# - будет ошибка!
