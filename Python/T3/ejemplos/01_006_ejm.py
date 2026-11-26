class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f'"{self.titulo}" por {self.autor}'

    def __repr__(self):
        return f"Libro({self.titulo!r}, {self.autor!r})"


# Creamos dos objetos
libro_1 = Libro("El Quijote", "Miguel de Cervantes")
libro_2 = Libro("1984", "George Orwell")


# print() utiliza __str__
print(libro_1)

# repr() utiliza __repr__
print(repr(libro_1))

# Las listas utilizan __repr__
biblioteca = [libro_1, libro_2]
print(biblioteca)