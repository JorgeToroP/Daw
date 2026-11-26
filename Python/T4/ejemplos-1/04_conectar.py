# Ejecuta este programa. Comprueba que la conexión se abre y se cierra.
from db import conectar

with conectar() as conexion:
    print(conexion.is_connected())
print("Conexión cerrada")
