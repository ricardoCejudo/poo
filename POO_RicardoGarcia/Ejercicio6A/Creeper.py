from Mob import Mob

class Creeper(Mob):
    def hacer_sonido(self):
        return "...Ssssss"

    def comportamiento(self):
        return "agresivo"

    def moverse(self):
        return "corre directamente hacia el jugador"
