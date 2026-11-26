class Carrito:
    def __init__(self, productos=None):
        self.productos = list(productos) if productos is not None else []

    def agregar(self, producto):
        self.productos.append(producto)

    def __len__(self):
        return len(self.productos)

    def __getitem__(self, posicion):
        return self.productos[posicion]

    def __eq__(self, otro):
        if not isinstance(otro, Carrito):
            return NotImplemented
        return self.productos == otro.productos

    def __str__(self):
        return ", ".join(self.productos) or "Carrito vacio"

    def __repr__(self):
        return f"Carrito({self.productos!r})"

if __name__ == "__main__":
    c = Carrito(["Libro", "Lapiz"])
    print(str(c), repr(c), len(c), c[0], sep="\n")
    print("Mismo contenido:", c == Carrito(["Libro", "Lapiz"]))
