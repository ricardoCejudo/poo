class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []

    def setCalificaciones(self, calificacion):
        self.calificaciones.append(calificacion)

    def getNombre(self):
        return self.nombre

    def mostrarPromedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def mostrarInformacionUsuario(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}"


estudiante1 = Estudiante("Ricardo", 20, "Ing. en Sistemas Computacionales")
estudiante2 = Estudiante("Carmen", 21, "Ing. Industrial")
estudiante3 = Estudiante("Ramon", 19, "Ing. Electronica")

print(estudiante1.mostrarInformacionUsuario())

estudiante1.setCalificaciones(95)
estudiante1.setCalificaciones(80)
estudiante1.setCalificaciones(70)

print(f"La calificacion de {estudiante1.getNombre()} es: {estudiante1.mostrarPromedio()}")
print(f"La calificacion de {estudiante2.getNombre()} es: {estudiante2.mostrarPromedio()}")
