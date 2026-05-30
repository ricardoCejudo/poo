from Pico import Pico
from Espada import Espada
from Pala import Pala

herramientas = [
    Pico("diamante", 5),
    Espada("hierro", 3),
    Pala("madera", 2),
]

print("--- PRUEBA DE HERRAMIENTAS ---\n")

for h in herramientas:
    h.estado()
    print(h.usar("bloque de piedra"))
    h.estado()
    print()

print("=== Desgaste hasta rotura ===")
pico = Pico("piedra", 3)
while not pico.rota:
    print(pico.usar("roca"))
    pico.estado()
print("El pico se rompio!")
