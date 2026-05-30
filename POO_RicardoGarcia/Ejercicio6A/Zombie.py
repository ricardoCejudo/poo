from Mob import Mob

class Zombie(Mob):
    def hacer_sonido(self):
        return "Gruuuh"

    def comportamiento(self):
        return "agresivo"

    def moverse(self):
        return "camina lento arrastrando los pies"
