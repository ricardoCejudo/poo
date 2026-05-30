from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def hablar(self):
        pass


class Perro(Animal):
    def hablar(self):
        return "GUAUUU"


class Gato(Animal):
    def hablar(self):
        return "miau"


perro1 = Perro()
gato1 = Gato()

print(perro1.hablar())
print(gato1.hablar())
