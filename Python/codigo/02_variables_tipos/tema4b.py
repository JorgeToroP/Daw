import sqlite3

conexion = sqlite3.connect(":memory:")   # base de datos temporal en memoria
cursor = conexion.cursor()

cursor.execute("CREATE TABLE productos (id INTEGER PRIMARY KEY, nombre TEXT, stock INT, categoria_id INT)")
cursor.executemany("INSERT INTO productos VALUES (?, ?, ?, ?)", [
    (1, "Smartphone", 20, 1),
    (2, "Laptop", 10, 1),
    (3, "Camiseta", 100, 2),
])
conexion.commit()

cursor.execute("SELECT nombre, stock FROM productos WHERE id = ?", (1,))
print(cursor.fetchone())

cursor.execute("SELECT nombre FROM productos")
print(cursor.fetchall())

cursor.execute("SELECT * FROM productos WHERE id = ?", (99,))
print(cursor.fetchone())

conexion.close()

#id |   nombre	     |   stock	|categoria_id
#1  |   Smartphone	 |   20	    |    1
#2  |   Laptop  	 |   10	    |    1
#3  |	Camiseta	 |   100	|    2