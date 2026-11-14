# 08_funciones.py
# Funciones con parámetros, retorno y docstring.

def calcular_promedio(notas):
    """Devuelve el promedio de una lista de notas."""
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)


def clasificar_nota(nota):
    if nota < 5:
        return "Suspenso"
    if nota < 7:
        return "Bien"
    if nota < 9:
        return "Notable"
    return "Sobresaliente"


notas = [7, 8, 6, 9]
promedio = calcular_promedio(notas)
print("Promedio:", promedio)
print("Clasificación:", clasificar_nota(promedio))
