import mysql.connector

conexion = mysql.connector.connect(        # 1. CONECTAR
    host="localhost", user="root",
    password="admin", database="tienda"
)
cursor = conexion.cursor()                 # 2. CREAR EL CURSOR
cursor.execute("SELECT * FROM productos WHERE id = %s", (2,))   # 3. EJECUTAR
fila = cursor.fetchone()                   # 4. RECOGER los resultados (en un SELECT)
conexion.commit()                          # 5. CONFIRMAR (solo en INSERT, UPDATE o DELETE)
cursor.close(); conexion.close()           # 6. CERRAR



#id |   nombre	     |   stock	|categoria_id
#1  |   Smartphone	 |   20	    |    1
#2  |   Laptop  	 |   10	    |    1
#3  |	Camiseta	 |   100	|    2