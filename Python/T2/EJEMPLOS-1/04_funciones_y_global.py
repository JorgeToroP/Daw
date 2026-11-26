# 04 - Funciones, variables globales y id automático

class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return (f"[{self.id}] {self.nombre} | "
                f"{self.precio:.2f} EUR | "
                f"stock: {self.cantidad}")

productos = []      # lista global
siguiente_id = 1    # contador global de ids

def crear_producto(nombre, precio, cantidad):
    # Sin "global", Python crearía una variable local nueva
    # y el contador global no se incrementaría.
    global siguiente_id
    producto = Producto(siguiente_id, nombre, precio, cantidad)
    productos.append(producto)   # append modifica la lista, no hace falta global
    siguiente_id += 1

def listar_productos():
    if len(productos) == 0:
        print("No hay productos.")
        return
    for p in productos:
        print(p)

crear_producto("Teclado", 24.99, 10)
crear_producto("Ratón", 12.5, 25)
crear_producto("Monitor", 149.5, 3)
listar_productos()
# Los ids se asignan solos: 1, 2 y 3
