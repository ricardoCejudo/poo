import os

ruta = "test.txt"
size = os.path.getsize(ruta)
kb = size / 1024
mb = size / (1024 * 1024)

print(f"Tamaño: {kb:.2f} KB")
print(f"Tamaño: {mb:.4f} MB")
