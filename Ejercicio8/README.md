# Ejercicio 8 — Jugador, Competidor y Observador

**Alumno:** Ricardo García Cejudo  
**Carrera:** Ingenieria en Sistemas Computacionales  
**Semestre:** 2SS

---

## Descripcion

Se modela un sistema de jugadores para un torneo. La clase base `Jugador` tiene nombre, numero de control, nivel y puntos. `Competidor` hereda de Jugador y agrega el equipo al que pertenece. `Observador` hereda de Jugador y lleva un conteo de partidas vistas.

## Conceptos que se practican

- Herencia con `super()`
- Sobreescritura de metodos manteniendo el comportamiento del padre
- Polimorfismo en `mostrar_perfil()`
- Metodos que modifican el estado del objeto

## Archivos

- `Jugador.py` — clase base
- `Competidor.py` — hereda de Jugador, agrega equipo
- `Observador.py` — hereda de Jugador, cuenta partidas vistas
- `main.py` — creacion de objetos y prueba de metodos


