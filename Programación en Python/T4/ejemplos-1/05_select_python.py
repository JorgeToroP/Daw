# Muestra las tres filas en Python usando execute y fetchall.
from db import conectar

with conectar() as cn:
    with cn.cursor() as cur:
        cur.execute("SELECT nombre, stock FROM productos ORDER BY id")
        filas = cur.fetchall()
        for fila in filas:
            print(fila)
