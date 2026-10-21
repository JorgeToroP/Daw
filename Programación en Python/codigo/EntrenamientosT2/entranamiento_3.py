#Programa para determinar el tipo de triangulo segun sus lados

# Solicitar al usuario las longitudes de los tres lados
a = int(input("Ingrese la longitud del primer lado: "))
b = int(input("Ingrese la longitud del segundo lado: "))
c = int(input("Ingrese la longitud del tercer lado: "))

"""Desarrollo paso a paso. Escribe un programa que determine el tipo de triángulo según
 la longitud de sus lados. El programa debe solicitar al usuario que introduzca las
   longitudes de los tres lados (a, b, c) como números enteros positivos. 
   Luego debe determinar si el triángulo es equilátero (si los tres lados son iguales),
     isósceles (si dos lados son iguales y uno diferente) o escaleno 
     (si los tres lados son diferentes). Además, el programa debe verificar si los tres
       valores pueden formar un triángulo válido. Recuerda que para que tres longitudes 
       formen un triángulo, la suma de las longitudes de dos lados cualesquiera debe ser
         mayor que la longitud del tercer lado. Si los valores no pueden formar un 
         triángulo, el programa debe mostrar: «No es un triángulo válido». """

if a >=0 and b >=0 and c >=0 :
    if a == b == c:
        print("Equilatero : los tres lados son iguales : ", a , b ,c )
    elif a==b or a ==c or b==c:
        print("Isosceles : dos lados son iguales ", a, b ,c) 
    elif a  !=b and a != c and b !=a and b!=c  and c!=a and c!=b:
        print("Escaleno : los tres lados son diferentes : ")