from Mob import Mob

class Enderman(Mob):
    def hacer_sonido(self):
        return "Sonido distorsionado"

    def comportamiento(self):
        return "neutral"

    def moverse(self):
        return "se teletransporta"
