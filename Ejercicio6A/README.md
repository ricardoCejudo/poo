# Ejercicio 6A — Mobs de Minecraft

**Alumno:** Ricardo Garcia Cejudo  
**Carrera:** Ingenieria en Sistemas Computacionales  
**Semestre:** 2SS

---

## Descripcion

Se modela el sistema de mobs de Minecraft usando una clase abstracta `Mob`. Cada mob debe implementar tres metodos: `hacer_sonido()`, `comportamiento()` y `moverse()`. Se demuestra que intentar crear un Mob directamente lanza un error.

## Conceptos que se practican

- Clase abstracta con multiples metodos abstractos
- Polimorfismo — cada mob se comporta diferente
- Manejo de `TypeError` al intentar instanciar una clase abstracta
- Recorrer una lista de objetos con un bucle

## Archivos

- `Mob.py` — clase abstracta base
- `Vaca.py` — mob pasivo
- `Creeper.py` — mob agresivo
- `Enderman.py` — mob neutral
- `Zombie.py` — mob agresivo lento
- `main.py` — simulador de mobs

## Como correr

```bash
python main.py
```
