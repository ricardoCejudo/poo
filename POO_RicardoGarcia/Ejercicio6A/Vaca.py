from Mob import Mob

class Vaca(Mob):
    def hacer_sonido(self):
        return "Muuuu"

    def comportamiento(self):
        return "pasivo"

    def moverse(self):
        return "camina lento por el prado"
