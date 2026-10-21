# 03 - Clases: la clase Producto

class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        # self es el objeto que se está creando
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        # Se usa cuando hacemos print(producto)
        return (f"[{self.id}] {self.nombre} | "
                f"{self.precio:.2f} EUR | "
                f"stock: {self.cantidad}")


# Crear objetos (instancias)
p1 = Producto(1, "Teclado", 24.99, 10)
p2 = Producto(2, "Monitor", 149.5, 3)

# Acceder y modificar atributos
print(p1.nombre)        # Teclado
p1.precio = 19.99
print(p1)               # usa __str__

# Los objetos se pueden guardar en una lista
productos = [p1, p2]
for p in productos:
    print(p)

# Buscar un objeto por un atributo
for p in productos:
    if p.id == 2:
        print("Encontrado:", p.nombre)
