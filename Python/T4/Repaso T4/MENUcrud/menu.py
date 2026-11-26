from getpass import getpass
import mysql.connector
from db import conectar


def login():
    """Pide usuario y contraseña (3 intentos). Si MySQL acepta, devuelve la conexión."""
    for intento in range(3):
        usuario = input("Usuario: ")
        clave = getpass("Contraseña: ")
        try:
            return conectar(usuario, clave)
        except mysql.connector.Error:
            print(f"Acceso denegado ({2 - intento} intentos restantes)\n")
    return None


def listar(con, cur):
    cur.execute("""SELECT p.id, p.nombre, p.precio, p.stock, c.nombre
                   FROM productos p LEFT JOIN categorias c ON p.categoria_id = c.id
                   ORDER BY p.id""")
    print(f"\n{'ID':>3}  {'NOMBRE':<15}{'PRECIO':>8}{'STOCK':>7}  CATEGORÍA")
    for id_, nombre, precio, stock, categoria in cur.fetchall():
        print(f"{id_:>3}  {nombre:<15}{precio:>8.2f}{stock:>7}  {categoria or '-'}")


def insertar(con, cur):
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))
    categoria = int(input("Categoría (1 Papelería, 2 Hogar): "))
    cur.execute("INSERT INTO productos (nombre, precio, stock, categoria_id) "
                "VALUES (%s, %s, %s, %s)", (nombre, precio, stock, categoria))
    con.commit()
    print("Producto añadido con id", cur.lastrowid)


def actualizar(con, cur):
    id_ = int(input("ID del producto: "))
    precio = float(input("Nuevo precio: "))
    cur.execute("UPDATE productos SET precio = %s WHERE id = %s", (precio, id_))
    con.commit()
    print("Precio actualizado." if cur.rowcount else "No hay cambios (¿existe ese ID?).")


def eliminar(con, cur):
    id_ = int(input("ID a eliminar: "))
    if input("¿Seguro? (s/n): ").lower() != "s":
        return
    cur.execute("DELETE FROM productos WHERE id = %s", (id_,))
    con.commit()
    print("Producto eliminado." if cur.rowcount else "No existe ese ID.")


OPCIONES = {
    "1": ("Ver productos", listar),
    "2": ("Añadir producto", insertar),
    "3": ("Cambiar precio", actualizar),
    "4": ("Eliminar producto", eliminar),
}


def main():
    con = login()
    if con is None:
        print("Demasiados intentos. Adiós.")
        return
    cur = con.cursor()
    while True:
        print("\n===== TIENDA AULA =====")
        for tecla, (texto, _) in OPCIONES.items():
            print(f" {tecla}. {texto}")
        print(" 0. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "0":
            break
        if opcion not in OPCIONES:
            print("Opción no válida.")
            continue
        try:
            OPCIONES[opcion][1](con, cur)
        except ValueError:
            print("Dato no válido: escribe un número.")
        except mysql.connector.Error as e:
            con.rollback()
            print("Error de MySQL:", e.msg)
    cur.close()
    con.close()
    print("Hasta luego.")


if __name__ == "__main__":
    main()
