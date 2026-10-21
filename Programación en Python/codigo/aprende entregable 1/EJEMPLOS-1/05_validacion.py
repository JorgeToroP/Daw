# 05 - Validación de entradas con try / except

# Problema: si el usuario escribe "abc", float("abc") lanza ValueError
# y el programa se cierra con un error.

# Solución 1: capturar el error
try:
    precio = float(input("Precio: "))
    print("Precio válido:", precio)
except ValueError:
    print("Error: el precio debe ser un número, por ejemplo 12.5")


# Solución 2: repetir hasta que el dato sea correcto (patrón muy útil)
def pedir_float(mensaje):
    while True:
        texto = input(mensaje)
        try:
            valor = float(texto)
            if valor < 0:
                print("Error: no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Error: introduce un número válido (usa punto decimal).")


def pedir_entero(mensaje):
    while True:
        texto = input(mensaje)
        try:
            valor = int(texto)
            if valor < 0:
                print("Error: no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Error: introduce un número entero.")


precio = pedir_float("Precio: ")
cantidad = pedir_entero("Cantidad: ")
print("Datos correctos:", precio, cantidad)

# Nombre no vacío
nombre = ""
while nombre.strip() == "":
    nombre = input("Nombre: ")
    if nombre.strip() == "":
        print("Error: el nombre no puede estar vacío.")
print("Nombre:", nombre.strip())
