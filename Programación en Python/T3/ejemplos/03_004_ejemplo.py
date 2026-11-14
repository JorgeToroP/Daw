class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector2D(
            self.x + otro.x,
            self.y + otro.y
        )

    def __eq__(self, otro):
        return (
            isinstance(otro, Vector2D)
            and self.x == otro.x
            and self.y == otro.y
        )

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"


# Creamos dos vectores
vector_a = Vector2D(2, 3)
vector_b = Vector2D(1, 4)

# __add__ permite utilizar el operador +
resultado = vector_a + vector_b

print(vector_a)
print(vector_b)
print(resultado)

# __eq__ permite utilizar el operador ==
vector_esperado = Vector2D(3, 7)

print("El resultado es el esperado?")
print(resultado == vector_esperado)