# 10_modulos.py
# Importar funciones desde un módulo propio.

from modulos.utilidades import convertir_a_float, calcular_promedio

entradas = ["7,5", "8", "6,5"]
notas = []

for entrada in entradas:
    notas.append(convertir_a_float(entrada))

print("Notas:", notas)
print("Promedio:", calcular_promedio(notas))
