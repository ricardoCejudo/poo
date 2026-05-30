# Programacion Orientada a Objetos

**Ricardo Garcia Cejudo**  
Ingenieria en Sistemas Computacionales — 2SS

---

## Descripcion

Ejercicios del curso de Programacion Orientada a Objetos en Python. Cada carpeta corresponde a una actividad del curso.

---

## Estructura

```
POO_RicardoGarcia/
├── Ejercicio1/        - Clase Estudiante (constructor, metodos, listas)
├── Ejercicio2/        - CuentaBancaria y MascotaVirtual (encapsulamiento)
├── Ejercicio3/        - Animal, Perro, Gato (herencia simple)
├── Ejercicio4/        - Platillo/Comida/Bebida/Postre + Aventureros (herencia multiple)
├── Ejercicio4b/       - Aventurero, Guerrero, Mago, Arquero, Elfo
├── Ejercicio5/        - Abstraccion con ABC (clases abstractas)
├── Ejercicio6A/       - Mobs de Minecraft (Mob abstracto + subclases)
├── Ejercicio6B/       - Herramientas de Minecraft (clase abstracta + polimorfismo)
├── Ejercicio7/        - Manejo de excepciones (try/except/else/finally)
├── Ejercicio8/        - Jugador, Competidor, Observador (herencia + polimorfismo)
└── Ejercicio9/        - Manejo de archivos (escritura, append, tamaño)
```

---

## Ejercicios

### Ejercicio 1 — Clase Estudiante
Clase con constructor, atributos y metodos. Se aprende a crear objetos y a usar listas dentro de una clase para guardar calificaciones y calcular promedios.

### Ejercicio 2 — CuentaBancaria y MascotaVirtual
Dos clases independientes. CuentaBancaria maneja depositos y retiros. MascotaVirtual tiene niveles de felicidad que cambian con alimentar() y jugar().

### Ejercicio 3 — Herencia con Animal
Clase padre Animal con subclases Perro y Gato. Cada una sobreescribe el metodo hablar() con su propio sonido.

### Ejercicio 4 — Herencia con restaurante y aventureros
Dos temas en un ejercicio. Platillo como clase padre con Comida, Bebida y Postre. Tambien Aventurero con subclases Guerrero, Mago, Arquero y Elfo.

### Ejercicio 5 — Abstraccion
Uso de ABC y @abstractmethod. Se crea una clase Animal abstracta que no se puede instanciar directamente; Perro y Gato la implementan.

### Ejercicio 6A — Mobs de Minecraft
Clase abstracta Mob con metodos abstractos hacer_sonido, comportamiento y moverse. Se implementan Vaca, Creeper, Enderman y Zombie.

### Ejercicio 6B — Herramientas de Minecraft
Clase abstracta Herramientas con tabla de daño por material. Pico, Espada y Pala la implementan. Se demuestra el desgaste hasta romper una herramienta.

### Ejercicio 7 — Manejo de excepciones
Cinco partes: division segura, acceso a listas, validacion con bucle, lectura de archivos y excepciones personalizadas (EdadInvalidaError, SaldoInsuficienteError).

### Ejercicio 8 — Jugador, Competidor, Observador
Clase Jugador base con herencia a Competidor (tiene equipo) y Observador (cuenta partidas vistas). Se usa super() para reutilizar mostrar_perfil().

### Ejercicio 9 — Archivos
Escritura y lectura de archivos de texto. Se crean funciones para escribir, agregar contenido y calcular el tamaño en KB/MB.

---

## Requisitos

- Python 3.10 o superior
- No requiere librerias externas

## Como correr un ejercicio

```bash
cd Ejercicio3
python main.py
```
