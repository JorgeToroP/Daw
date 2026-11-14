
productos = []          # lista vacía
print(len(productos))   # 0

# Añadir elementos
productos.append("Teclado")
productos.append("Ratón")
productos.append("Monitor")
print(productos)        # ['Teclado', 'Ratón', 'Monitor']

# Recorrer la lista con un for
for p in productos:
    print("-", p)

# Acceder por posición (empieza en 0)
print(productos[0])     # Teclado

# Eliminar un elemento
productos.remove("Ratón")
print(productos)        # ['Teclado', 'Monitor']

# Buscar: ¿está en la lista?
if "Monitor" in productos:
    print("Monitor encontrado")

# Buscar con un bucle y una variable "encontrado"
buscado = "Webcam"
encontrado = None
for p in productos:
    if p == buscado:
        encontrado = p
        break

if encontrado is None:
    print("No existe:", buscado)
