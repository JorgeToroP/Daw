# 06_bucles.py
# for, while, break y continue.

print("Cuenta con for:")
for i in range(1, 6):
    print(i)

print("Números impares hasta 10:")
for numero in range(1, 11):
    if numero % 2 == 0:
        continue
    print(numero)

print("Menú simple con while:")
opcion = ""
while opcion != "salir":
    opcion = input("Escribe 'salir' para terminar: ").lower()
    if opcion == "salir":
        break
    print("Has escrito:", opcion)
