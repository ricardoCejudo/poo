from Mob import Mob
from Vaca import Vaca
from Creeper import Creeper
from Enderman import Enderman
from Zombie import Zombie

print("--- SIMULADOR DE MOBS ---")

try:
    print("\nIntentando crear un Mob generico...")
    test_mob = Mob("Test", 10)
except TypeError as e:
    print(f"ERROR ESPERADO: {e}")
    print("No se puede instanciar Mob porque es una clase abstracta.")

mobs = [
    Vaca("Clara", 10),
    Creeper("Explosi", 20),
    Enderman("Tall Boi", 40),
    Zombie("Eddy", 20)
]

print("\n--- REPORTE DE MOBS ---")
for mob in mobs:
    mob.presentarse()
