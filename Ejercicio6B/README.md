# Ejercicio 6B — Herramientas de Minecraft

**Alumno:** Ricardo Garcia Cejudo  
**Carrera:** Ingenieria en Sistemas Computacionales  
**Semestre:** 2SS

---

## Descripcion

Se modela el sistema de herramientas de Minecraft usando una clase abstracta `Herramientas`. Cada herramienta tiene un material y durabilidad. El daño depende del material segun una tabla predefinida. Las herramientas se desgastan con cada uso hasta romperse.

## Conceptos que se practican

- Clase abstracta con propiedad abstracta (`@property`)
- Atributos protegidos con guion bajo (`_material`, `_durabilidad`)
- Metodos concretos compartidos por todas las subclases
- Simulacion de desgaste con bucle while

## Archivos

- `Herramientas.py` — clase abstracta con tabla de daño por material
- `Pico.py` — mina bloques
- `Espada.py` — ataca enemigos
- `Pala.py` — excava tierra
- `main.py` — prueba de herramientas y desgaste

## Como correr

```bash
python main.py
```
