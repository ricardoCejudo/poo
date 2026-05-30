# Ejercicio 4 — Restaurante (Herencia con Platillo)

**Alumno:** Ricardo Garcia Cejudo  
**Carrera:** Ingenieria en Sistemas Computacionales  
**Semestre:** 2SS

---

## Descripcion

Se modela un menu de restaurante usando herencia. La clase padre `Platillo` tiene nombre y precio. Las clases hijas `Comida`, `Bebida` y `Postre` agregan atributos propios y sobreescriben el metodo `mostrarInformacion()`.

## Conceptos que se practican

- Herencia con multiples clases hijas
- Sobreescritura de metodos
- Uso de `super()` para llamar al metodo del padre
- Polimorfismo basico

## Archivos

- `Platillo.py` — clase padre
- `Comida.py` — clase hija con atributo categoria
- `Bebida.py` — clase hija con atributo temperatura
- `Postre.py` — clase hija con atributo es_con_gluten
- `main.py` — prueba de todas las clases

## Como correr

```bash
python main.py
```
