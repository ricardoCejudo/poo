from abc import ABC, abstractmethod

DAÑO_MATERIAL = {
    "madera": 2,
    "piedra": 3,
    "hierro": 4,
    "oro": 3,
    "diamante": 6,
    "netherita": 8,
}


class Herramientas(ABC):
    def __init__(self, material, durabilidad):
        self._material = material.lower()
        self._durabilidad = durabilidad
        self._usos_restantes = durabilidad

    @property
    @abstractmethod
    def nombre(self):
        pass

    @abstractmethod
    def usar(self, objetivo):
        pass

    def calcular_daño(self):
        return DAÑO_MATERIAL.get(self._material, 1)

    def desgastar(self):
        if self._usos_restantes > 0:
            self._usos_restantes -= 1

    @property
    def rota(self):
        return self._usos_restantes == 0

    def estado(self):
        if self.rota:
            print(f"[{self.nombre} de {self._material}] ROTA")
        else:
            print(f"[{self.nombre} de {self._material}] {self._usos_restantes} usos restantes")
