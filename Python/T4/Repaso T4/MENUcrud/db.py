import os
import mysql.connector

def conectar(usuario, clave):
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=usuario, password=clave,
        database="tema4_aula", autocommit=False, connection_timeout=10)
