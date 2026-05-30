print("=" * 50)
print("PARTE 1: Division con manejo de errores")
print("=" * 50)

try:
    a = int(input("Ingresa el numerador: "))
    b = int(input("Ingresa el denominador: "))
    total = a / b

except ValueError:
    print("Error: solo numeros enteros, no otros simbolos")

except ZeroDivisionError:
    print("Error: No se puede dividir por cero")

else:
    print(f"El resultado de {a} / {b} es: {total}")

finally:
    print("Gracias por usar el programa de division!")


print("\n" + "=" * 50)
print("PARTE 2: Acceso a una lista")
print("=" * 50)

colores = ["rojo", "verde", "azul", "amarillo"]
print(f"Lista de colores: {colores} (indices 0,1,2,3)")

try:
    indice = int(input("Que color quieres acceder? (0-3): "))
    print(f"El color seleccionado es: {colores[indice]}")

except ValueError as e:
    print(f"ValueError: {e}")

except IndexError as e:
    print(f"IndexError: {e}")
    print("Recuerda que los indices validos son del 0 al 3")

finally:
    print("-- Fin del programa --")


print("\n" + "=" * 50)
print("PARTE 3: Validacion con bucle")
print("=" * 50)

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Solo se aceptan numeros enteros. Intenta de nuevo.")

a = pedir_entero("Primer numero: ")
b = pedir_entero("Segundo numero: ")

print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicacion: {a * b}")

if b != 0:
    print(f"Division: {a / b:.2f}")
else:
    print("Division: no definida (b=0)")


print("\n" + "=" * 50)
print("PARTE 4: Leer archivo con manejo de errores")
print("=" * 50)

nombre = input("Nombre del archivo (.txt): ")

try:
    with open(nombre, "r", encoding="utf-8") as f:
        contenido = f.read()
    print("\n--- Contenido ---")
    print(contenido)

except FileNotFoundError:
    print(f"El archivo '{nombre}' no existe.")

except PermissionError:
    print("No tienes permisos para leer ese archivo.")

except Exception as e:
    print(f"Error inesperado: {e}")

finally:
    print("\nIntento de lectura concluido.")


print("\n" + "=" * 50)
print("PARTE 5: Excepciones personalizadas")
print("=" * 50)

class EdadInvalidaError(Exception):
    def __init__(self, edad):
        super().__init__(f"Edad invalida: {edad}. Debe estar entre 0 y 120.")
        self.edad = edad

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto):
        super().__init__(f"Saldo insuficiente. Tienes ${saldo}, necesitas ${monto}.")
        self.saldo = saldo
        self.monto = monto

def registrar_edad(edad):
    if not (0 <= edad <= 120):
        raise EdadInvalidaError(edad)
    return f"Edad {edad} registrada correctamente."

def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
    return saldo - monto

try:
    print(registrar_edad(200))
except EdadInvalidaError as e:
    print(f"Error: {e}")

try:
    nuevo_saldo = retirar(500, 800)
    print(f"Nuevo saldo: ${nuevo_saldo}")
except SaldoInsuficienteError as e:
    print(f"Error: {e}")
    print(f"Faltan ${e.monto - e.saldo} para completar el retiro.")
