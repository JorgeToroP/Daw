class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def prestar(self):
        if self.prestado:
            return "No disponible"
        self.prestado = True
        return "Prestamo realizado"

    def devolver(self):
        self.prestado = False
        return "Libro devuelto"

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

if __name__ == "__main__":
    a = Libro("Python facil", "Ana")
    b = Libro("POO en practica", "Luis")
    print(a, b, sep="\n")
    print(a.prestar(), a.prestar(), a.devolver(), sep="\n")
    print("Instancias distintas:", a is not b)
