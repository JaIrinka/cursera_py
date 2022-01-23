# *****************************
#    КЛАССЫ - КОМПОЗИЦИЯ
# *****************************
import json


class PetExport:
    def export(self, dog):
        raise NotImplementedError


class ExportJSON(PetExport):
    def export(self, dog):
        return json.dumps({
            "name": dog.name,
            "breed": dog.breed
        })


class ExportXML(PetExport):
    def export(self, dog):
        return f"""<?xml version="1.0" encoding="utf-8"?>
<dog>
    <name>{dog.name}</name>
    <breed>{dog.breed}</breed>
</dog>"""


class Pet:
    def __init__(self, name):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed


class ExDog(Dog):
    def __init__(self, name, breed=None, exporter=None):
        super().__init__(name, breed)
        self._exporter = exporter or ExportJSON()
        if not isinstance(self._exporter, PetExport):
            raise ValueError("bad exporter", exporter)

    def export(self):
        return self._exporter.export(self)


if __name__ == "__main__":
    dog = ExDog('Sharry', 'Toy', exporter=ExportXML())
    print(dog.export())
    print('------------------------------------')
    dog_2 = ExDog('Tusic', 'Toy-2', exporter=ExportJSON())
    print(dog_2.export())
