def imprimir(texto):
    print(texto)

def sumar(x,y):
    z = x + y
    return z
def restar(x,y):
    z = x - y
    return z


for numero in range(1, 11):
    imprimir("1 suma")
    imprimir("2 resta")
    imprimir("3 blablabla")
    imprimir("4 blablabla")
    imprimir("5 salir")
    opcion = int(input("elige una opcion: "))

    if opcion == 1:
        imprimir("vamos a sumar 3 y 4")
        r= sumar(3,4)
        print(r)
        continue
    if opcion == 2:
        imprimir("vamos a restar 6 y 4")
        r= restar(6,4)
        print(r)
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