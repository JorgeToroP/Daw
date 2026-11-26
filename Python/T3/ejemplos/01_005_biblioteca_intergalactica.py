class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def prestar(self):
        if self.prestado:
            return f'"{self.titulo}" no esta disponible. Lo tiene un marciano.'

        self.prestado = True
        return f'Prestamo realizado: "{self.titulo}" despega de la biblioteca.'

    def devolver(self):
        if not self.prestado:
            return f'"{self.titulo}" ya estaba en la biblioteca. Caso cerrado.'

        self.prestado = False
        return f'Libro devuelto: "{self.titulo}" ha aterrizado sano y salvo.'

    def __str__(self):
        estado = "prestado" if self.prestado else "disponible"
        return f"{self.titulo} - {self.autor} ({estado})"


if __name__ == "__main__":
    
    a = Libro("Python para terricolas", "Ana Andromeda")
    b = Libro("POO sin perder la cabeza", "Luis Lunar")

    print(a, b, sep="\n")
    print(a.prestar())
    print(a.prestar())
    print(a.devolver())
    print(a)
    print("Son instancias distintas?", a is not b)

