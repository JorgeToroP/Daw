# 07_estructuras_datos.py
# Listas, tuplas, conjuntos y diccionarios.

notas = [7, 5, 9, 6, 7]
notas.append(8)
print("Notas:", notas)
print("Primera nota:", notas[0])
print("Promedio:", sum(notas) / len(notas))

coordenada = (10, 20)
print("Coordenada:", coordenada)

unicas = set(notas)
print("Notas sin repetir:", unicas)

alumno = {
    "nombre": "Ana",
    "curso": "2º DAM",
    "notas": notas
}
print("Alumno:", alumno["nombre"])
print("Curso:", alumno.get("curso", "No indicado"))
