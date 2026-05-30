# Ejercicio 4B — Taberna de Aventureros

**Alumno:** Ricardo García Cejudo  
**Carrera:** Ingenieria en Sistemas Computacionales  
**Semestre:** 2SS

---

## Descripcion

Se modela un sistema de personajes de fantasia usando herencia. La clase padre `Aventurero` tiene nombre y nivel. Las clases hijas `Guerrero`, `Mago`, `Arquero` y `Elfo` heredan de ella y cada una implementa su propia habilidad especial.

## Conceptos que se practican

- Herencia con multiples clases hijas
- Polimorfismo — cada personaje usa `usar_habilidad()` a su manera
- Atributos especificos por subclase (arma, hechizo, flechas)

## Archivos

- `Aventurero.py` — clase padre
- `Guerrero.py` — ataca con arma
- `Mago.py` — lanza hechizos
- `Arquero.py` — dispara flechas (con contador)
- `Elfo.py` — lanza hechizos elficos
- `main.py` — prueba de todos los personajes


