import os
from getpass import getpass
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER", "aula_python"),
        password=os.getenv("MYSQL_PASSWORD") or getpass("Contraseña MySQL: "),
        database="tema4_aula", autocommit=False, connection_timeout=10)
