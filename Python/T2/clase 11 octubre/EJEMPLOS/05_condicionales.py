# 05_condicionales.py
# if, elif, else y operador ternario.

nota = float(input("Introduce una nota de 0 a 10: "))

if nota < 0 or nota > 10:
    calificacion = "Nota no válida"
elif nota < 5:
    calificacion = "Suspenso"
elif nota < 7:
    calificacion = "Bien"
elif nota < 9:
    calificacion = "Notable"
else:
    calificacion = "Sobresaliente"

estado = "aprobado" if nota >= 5 and nota <= 10 else "no aprobado"

print("Calificación:", calificacion)
print("Estado:", estado)
