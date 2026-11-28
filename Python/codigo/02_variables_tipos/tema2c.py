
# F
t = (5)
print(type(t))
t2 = (5,)
print(type(t2))

# G
x = {}
print(type(x))

def saludar(nombre):          # def + nombre + (parámetros) + :
    return f"Hola {nombre}"

                # se llama con el nombre y paréntesis

def Velocidad (velocidad):
    return f"estas corriendo a {velocidad} km/h"

Velocidad(10)
print(saludar("Ana,"), Velocidad(10))

def doble(x):
    print(x * 2)      # imprime, pero NO devuelve nada
r = doble(5)          # se imprime 10
print(r)              # None


try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"Tienes {edad} años")
finally:
    print("Fin del programa")