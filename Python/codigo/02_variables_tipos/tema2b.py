# Bloque A  ← trampa de orden
nota = 7
if nota >= 9:
    print("Sobresaliente")
elif nota >= 5:
    print("Aprobado")
elif nota >= 7:
    print("Notable")
else:
    print("Suspenso")

# Bloque B
for i in range(1, 10, 3):
    print(i)

# Bloque C  ← sigue el valor vuelta a vuelta
contador = 5
while contador > 0:
    contador -= 2
print("c = ",contador)

# Bloque D  ← break + continue juntos
for n in range(6):
    if n == 4:
        break
    if n % 2 == 0:
        continue
    print("d = ", n)

# Bloque E
lista = []
if lista:
    print("Tiene datos")
else:
    print("Vacía")

# Bloque F
print([x * 2 for x in range(5) if x > 1])

# Bloque G
edad = 16
print("adulto" if edad >= 18 else "menor")