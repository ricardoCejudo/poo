from abc import ABC, abstractmethod

class Mob(ABC):
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def comportamiento(self):
        pass

    @abstractmethod
    def moverse(self):
        pass

    def presentarse(self):
        print(f"=== {self.nombre} ===")
        print(f"Vida: {self.vida} HP")
        print(f"Sonido: {self.hacer_sonido()}")
        print(f"Tipo: {self.comportamiento()}")
        print(f"Movimiento: {self.moverse()}")
        print()
