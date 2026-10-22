class Producto:
    # TODO 1: define __init__ con id, nombre, precio y cantidad
    # TODO 2: define __str__ para mostrar el producto en una línea
    pass

productos = []        # memoria del programa
siguiente_id = 1      # contador global de ids

def pedir_entero(mensaje):
    # TODO 3: repetir con while hasta que el usuario escriba un entero válido
    #         (usa try / except ValueError)ghghghgu
    pass

def pedir_float(mensaje):
    # TODO 4: igual que pedir_entero pero con float
    pass

def buscar_por_id(id_buscado):
    # TODO 5: recorre la lista y devuelve el producto con ese id, o None
    pass

def crear_producto():
    # TODO 6: pedir nombre, precio y cantidad; crear el Producto con
    #         siguiente_id; añadirlo a la lista; incrementar el contador
    #         (recuerda: global siguiente_id)
    pass

def listar_productos():
    # TODO 7: si la lista está vacía, avisa; si no, imprime cada producto
    pass

def actualizar_producto():
    # TODO 8: pedir id, buscar, y si existe pedir nuevos datos
    pass

def eliminar_producto():
    # TODO 9: pedir id, buscar, eliminar de la lista o avisar si no existe
    pass

def main():
    # TODO 10: menú con while True y if/elif sobre cadenas ("1", "2", ...)
    pass

if __name__ == "__main__":
    main()
