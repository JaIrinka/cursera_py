# *****************************
#         КЛАССЫ - 4
# *****************************
from datetime import datetime


# делаем вид, что обрабатываем пользовательский ввод, на деле - всегда ПУНЬК :)
def extract_description(user_string):
    return "Сделать ПУНЬК"


# делаем вид, что обрабатываем пользовательский ввод, на деле - всегда сегодня :)
def extract_date(user_string):
    return datetime.today()


class Event:

    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f'Event "{self.description}" at {self.date}'

    # создаёт экземпляр класса якобы из вводимой пользователем строки
    # на деле функции-обработчики ничего не обрабатывают :)
    # аннотация типа для красоты
    @classmethod
    def from_string(cls, user_string: str):
        description = extract_description(user_string)
        date = extract_date(user_string)
        return cls(description, date)


event_description = "Поглаживание и начёсывание кота"
event_date = datetime.today()

event = Event(event_description, event_date)
print(event)

event2 = Event.from_string("Типа футбол, работа, ололо")
print(event2)
