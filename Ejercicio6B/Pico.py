from Herramientas import Herramientas

class Pico(Herramientas):
    @property
    def nombre(self):
        return "Pico"

    def usar(self, objetivo):
        daño = self.calcular_daño()
        self.desgastar()
        return f"Pico de {self._material} mina {objetivo} (daño: {daño})"
