class Jugador:
    def __init__(self, nombre, numero_de_control, nivel, puntos):
        self.nombre = nombre
        self.numero_de_control = numero_de_control
        self.nivel = nivel
        self.puntos = puntos

    def ganar_puntos(self, cantidad):
        self.puntos += cantidad
        print(f"{self.nombre} gano {cantidad} puntos. Total: {self.puntos}")

    def perder_puntos(self, cantidad):
        self.puntos -= cantidad
        if self.puntos < 0:
            self.puntos = 0
        print(f"{self.nombre} perdio {cantidad} puntos. Total: {self.puntos}")

    def mostrar_perfil(self):
        print(f"Nombre: {self.nombre}")
        print(f"Numero de Control: {self.numero_de_control}")
        print(f"Nivel: {self.nivel}")
        print(f"Puntos: {self.puntos}")
