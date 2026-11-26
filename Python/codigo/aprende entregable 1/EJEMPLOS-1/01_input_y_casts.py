# 01 - input() y conversión de tipos (cast)
# input() SIEMPRE devuelve un string, aunque el usuario escriba un número.

nombre = input("Nombre del producto: ")
precio_texto = input("Precio: ")
cantidad_texto = input("Cantidad: ")

print(type(precio_texto))  # <class 'str'>

# Convertimos el texto al tipo que necesitamos
precio = float(precio_texto)
cantidad = int(cantidad_texto)

print(type(precio))    # <class 'float'>
print(type(cantidad))  # <class 'int'>

# Ahora sí podemos operar con los números
total = precio * cantidad
print("Valor total en inventario:", total)

# Se puede hacer todo en una línea:
# precio = float(input("Precio: "))
