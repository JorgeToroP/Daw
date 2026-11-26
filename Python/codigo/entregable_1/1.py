def imprimir(texto):
    print(texto)
    print("---")

for numero in range(1, 11):
    imprimir("1 blablabla")
    imprimir("2 blablabla")
    imprimir("3 blablabla")
    imprimir("4 blablabla")
    imprimir("5 salir")
    opcion = int(input("elige una opcion: "))

    if opcion == 1:
        imprimir("elegiste opcion 1")
        continue

    if opcion == 2:
        imprimir("elegiste opcion 2")
        continue

    if opcion == 3:
        imprimir("elegiste opcion 3")
        continue

    if opcion == 4:
        imprimir("elegiste opcion 4")
        continue

    if opcion >=5:
        break

imprimir("termine")