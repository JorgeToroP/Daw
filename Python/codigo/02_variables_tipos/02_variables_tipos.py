# 02_variables_tipos.py
# Variables, tipos básicos y type().

nombre = "Ana"
edad = 25
altura = 1.75
es_estudiante = True
sin_valor = None

print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Estudiante?:", es_estudiante)
print("Sin valor:", sin_valor)

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(es_estudiante))
print(type(sin_valor))


nombre1 = "laura"
print(nombre1)
edad1 = 30
print(edad1)
print(f"Hola mi nombre es {nombre1} y tengo {edad1} años")

mensaje1 ="Hola mi nombre es {} y tengo {} años".format(nombre1,edad1)
print(mensaje1)


numero_texto ="100"
numero =int(numero_texto)
print(numero + 25)

nombre_compuesta = """
Jorge
Toro
Pineda
"""
print (nombre_compuesta*3)


mensaje="esto es un mensaje de prueba"


for i in range(2, 10, 2):
    print(i)

contador = 0
print ("////////////////////////////////")
while contador < 5:
    print(contador)
    contador += 1 # Es crucial modificar la variable de control
print ("////////////////////////////////")
contador2 = 0

# Crear lista de cuadrados
cuadrados = [x**2 for x in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Comprensión anidada
matriz = [[i*j for j in range(1, 4)] for i in range(1, 4)]
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# enumerate() - obtiene índice y valor
for indice, valor in enumerate(["a", "b", "c"]):
    print(f"Índice {indice}: {valor}")

    # zip() - combina iterables
nombres = ["Ana", "Carlos", "Eva"]
edades = [25, 30, 22]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

    # Expresión generadora (similar a comprensión, pero con paréntesis)
suma = sum(x**2 for x in range(1000000)) # Más eficiente que crear una lista

datos = [10, 20, 0, 30, 0, 40]
resultado = []
for valor in datos:
    if valor == 0:
        continue # Salta los ceros
    if len(resultado) >= 3:
        break # Limita a 3 elementos
    resultado.append(100 / valor)
print(resultado) # [10.0, 5.0, 3.3333...]