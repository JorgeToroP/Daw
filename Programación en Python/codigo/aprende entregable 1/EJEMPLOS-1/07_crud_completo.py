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


# Memoria del programa
productos = []
siguiente_id = 1


# ---------- Utilidades de validación ----------

def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error: no puede estar vacío.")


def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Error: no puede ser negativo.")
            else:
                return valor
        except ValueError:
            print("Error: introduce un número válido (usa punto decimal).")


def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: no puede ser negativo.")
            else:
                return valor
        except ValueError:
            print("Error: introduce un número entero.")


def buscar_por_id(id_buscado):
    for p in productos:
        if p.id == id_buscado:
            return p
    return None


# ---------- Operaciones CRUD ----------

def crear_producto():
    global siguiente_id
    nombre = pedir_texto("Nombre: ")
    precio = pedir_float("Precio: ")
    cantidad = pedir_entero("Cantidad: ")
    producto = Producto(siguiente_id, nombre, precio, cantidad)
    productos.append(producto)
    print(f"Producto creado con id {siguiente_id}.")
    siguiente_id += 1


def listar_productos():
    if len(productos) == 0:
        print("No hay productos registrados.")
        return
    for p in productos:
        print(p)


def actualizar_producto():
    id_buscado = pedir_entero("Id del producto a actualizar: ")
    producto = buscar_por_id(id_buscado)
    if producto is None:
        print(f"No existe ningún producto con id {id_buscado}.")
        return

    print("Producto actual:", producto)
    print("Deja vacío un campo para mantener su valor actual.")

    nombre = input("Nuevo nombre: ").strip()
    if nombre != "":
        producto.nombre = nombre

    texto_precio = input("Nuevo precio: ").strip()
    if texto_precio != "":
        try:
            nuevo_precio = float(texto_precio)
            if nuevo_precio < 0:
                print("Precio no válido, se mantiene el anterior.")
            else:
                producto.precio = nuevo_precio
        except ValueError:
            print("Precio no válido, se mantiene el anterior.")

    texto_cantidad = input("Nueva cantidad: ").strip()
    if texto_cantidad != "":
        try:
            nueva_cantidad = int(texto_cantidad)
            if nueva_cantidad < 0:
                print("Cantidad no válida, se mantiene la anterior.")
            else:
                producto.cantidad = nueva_cantidad
        except ValueError:
            print("Cantidad no válida, se mantiene la anterior.")

    print("Producto actualizado:", producto)


def eliminar_producto():
    id_buscado = pedir_entero("Id del producto a eliminar: ")
    producto = buscar_por_id(id_buscado)
    if producto is None:
        print(f"No existe ningún producto con id {id_buscado}.")
        return
    productos.remove(producto)
    print("Producto eliminado.")


# ---------- Menú principal ----------

def mostrar_menu():
    print()
    print("===== GESTIÓN DE PRODUCTOS =====")
    print("1. Crear producto")
    print("2. Listar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            crear_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("Hasta pronto.")
            break
        else:
            print("Opción no válida, elige un número del 1 al 5.")


if __name__ == "__main__":
    main()
