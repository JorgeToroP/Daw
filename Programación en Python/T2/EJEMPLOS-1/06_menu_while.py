# 06 - Menú por consola con bucle while

def mostrar_menu():
    print()
    print("===== GESTIÓN DE PRODUCTOS =====")
    print("1. Crear producto")
    print("2. Listar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")


while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")   # siempre es un string

    if opcion == "1":
        print(">> (aquí llamaremos a crear_producto)")
    elif opcion == "2":
        print(">> (aquí llamaremos a listar_productos)")
    elif opcion == "3":
        print(">> (aquí llamaremos a actualizar_producto)")
    elif opcion == "4":
        print(">> (aquí llamaremos a eliminar_producto)")
    elif opcion == "5":
        print("Hasta pronto.")
        break
    else:
        print("Opción no válida, elige un número del 1 al 5.")
