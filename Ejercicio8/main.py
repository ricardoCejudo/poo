from Jugador import Jugador
from Competidor import Competidor
from Observador import Observador

jugador1 = Jugador("Juan", "12345", "Principiante", 100)
competidor1 = Competidor("Ana", "54321", "Avanzado", 200, "Equipo A")
observador1 = Observador("Carlos", "67890", "Intermedio", 150, 5)

jugador1.mostrar_perfil()
print()
competidor1.mostrar_perfil()
print()
observador1.mostrar_perfil()

print()
competidor1.ganar_puntos(50)
competidor1.perder_puntos(20)

print()
observador1.ver_partida()
observador1.ver_partida()
