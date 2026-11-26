# 11_archivos.py
# Escritura y lectura de archivos de texto.

ruta = "notas.txt"

with open(ruta, "w", encoding="utf-8") as archivo:
    archivo.write("Ana;7\n")
    archivo.write("Carlos;8\n")
    archivo.write("Eva;9\n")

with open(ruta, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, nota = linea.strip().split(";")
        print(f"{nombre} tiene un {nota}")
