from Herramientas import Herramientas

class Espada(Herramientas):
    @property
    def nombre(self):
        return "Espada"

    def usar(self, objetivo):
        daño = self.calcular_daño()
        self.desgastar()
        return f"Espada de {self._material} ataca a {objetivo} (daño: {daño})"
