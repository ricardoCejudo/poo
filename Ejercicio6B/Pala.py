from Herramientas import Herramientas

class Pala(Herramientas):
    @property
    def nombre(self):
        return "Pala"

    def usar(self, objetivo):
        daño = self.calcular_daño()
        self.desgastar()
        return f"Pala de {self._material} excava {objetivo} (daño: {daño})"
