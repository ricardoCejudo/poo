class MascotaVirtual:
    def __init__(self, nombre, tipo, edad, nivelFelicidad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.nivelFelicidad = nivelFelicidad

    def alimentar(self):
        self.nivelFelicidad = self.nivelFelicidad + 10
        if self.nivelFelicidad > 100:
            self.nivelFelicidad = 100

    def jugar(self):
        self.nivelFelicidad = self.nivelFelicidad + 20
        if self.nivelFelicidad > 100:
            self.nivelFelicidad = 100

    def mostrarEstado(self):
        return f"Hola, me llamo {self.nombre}, tengo {self.edad} años y soy un {self.tipo}. Felicidad: {self.nivelFelicidad}"

    def esFeliz(self):
        if self.nivelFelicidad >= 70:
            return "Tu mascota esta feliz"
        else:
            return "Tu mascota no esta feliz"


mascota1 = MascotaVirtual("Firulais", "perro", 3, 10)
mascota1.alimentar()
mascota1.jugar()
print(mascota1.mostrarEstado())
print(mascota1.esFeliz())

mascota2 = MascotaVirtual("Michi", "gato", 2, 30)
mascota2.alimentar()
mascota2.alimentar()
mascota2.jugar()
print(mascota2.mostrarEstado())
print(mascota2.esFeliz())
