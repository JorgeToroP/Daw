# 09_excepciones.py
# Manejo básico de excepciones.

try:
    numero = int(input("Introduce un número entero: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ValueError:
    print("Error: debes introducir un número entero")
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero")
finally:
    print("Fin del programa")
