from Comida import Comida
from Bebida import Bebida
from Postre import Postre

pozole = Comida("Pozole", 100.00, "Plato Fuerte")
pozole.mostrarInformacion()

print("---")

soda = Bebida("Coca-Cola", 40.00, "Fria")
soda.mostrarInformacion()

print("---")

flan = Postre("Flan Napolitano", 80.00, False)
flan.mostrarInformacion()
print(flan.tipo())
