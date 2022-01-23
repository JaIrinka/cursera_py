# *****************************
#     МАГИЧЕСКИЕ МЕТОДЫ
# https://docs.python.org/3/reference/datamodel.html
# *****************************


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_email_data(self):
        return {
            "name": self.name,
            "email": self.email
        }

    def __str__(self):
        return f"{self.name} <{self.email}>"

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, other):
        return self.email == other.email


class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance


class Researcher:
    # когда аттрибут не найден
    def __getattr__(self, name):
        return "Nothing found :(\n"

    # когда обращаемся к аттрибуту
    def __getattribute__(self, name):
        # return "nope"
        print(f"Looking for {name}")
        # return super().__getattribute__(name)
        return object.__getattribute__(self, name)

    def __setattr__(self, key, value):
        print(f"Not gonna set {key}!")

    def __delattr__(self, name):
        value = getattr(self, name)
        print(f"Goodby {name}, you were {value}!")

        object.__delattr__(self, name)


class Logger:
    def __init__(self, filrname):
        self.filrname = filrname

    def __call__(self, func):
        """ так делается обычный класс-декоратор """
        def wrapped(*args, **kwargs):
            with open(self.filrname, 'a') as f:
                f.write("Oh Danny boy...\n")

            return func(*args, **kwargs)
        return wrapped


logger = Logger('log_file')


@logger
def completley_useless_function():
    pass


if __name__ == "__main__":
    joe = User("Joe", "joe@mail.com")
    joe_jr = User("Joe junior", "joe@mail.com")
    print(hash(joe), joe)
    print(hash(joe_jr), joe_jr)
    print(joe == joe_jr)
    print(joe.get_email_data())

    a = Singleton()
    b = Singleton()
    print(a == b)

    obj = Researcher()
    print(obj.attr)
    print(obj.method)
    print(obj.Sujrl7d)
    obj.match = True
    print(obj.match)

    completley_useless_function()
