class Value:
    def __init__(self):
        self.amount = 0

    def __set__(self, instance, value):
        self.amount = (1 - getattr(instance, 'commission')) * value

    def __get__(self, instance, owner):
        return self.amount
