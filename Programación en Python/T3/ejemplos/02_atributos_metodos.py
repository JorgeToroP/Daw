class Producto:
    iva = 0.21
    creados = 0

    def __init__(self, nombre, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.nombre = nombre
        self.precio = precio
        type(self).creados += 1

    def precio_final(self):
        return round(self.precio * (1 + self.iva), 2)

    @classmethod
    def desde_texto(cls, texto):
        nombre, precio = texto.split(";")
        return cls(nombre, float(precio))

    @staticmethod
    def precio_valido(precio):
        return precio >= 0

if __name__ == "__main__":
    p = Producto.desde_texto("Cuaderno;10")
    p2 = Producto.desde_texto("Cuaderno2;15")
    print(p.nombre, p.precio_final())
    print("IVA compartido:", Producto.iva)
    print("Creados:", Producto.creados)
    print("Precio valido:", Producto.precio_valido(10))
