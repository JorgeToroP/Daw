class Alumno:
    centro = "IES Python"
    total = 0

    def __init__(self, nombre, nota=5):
        self.nombre = nombre
        self.nota = nota
        Alumno.total += 1

    def aprobar(self):
        return self.nota >= 5

    def subir_nota(self, puntos):
        self.nota += puntos
        return self.nota

    def __str__(self):
        return f"{self.nombre} ({self.nota})"

# A
a1 = Alumno("Ana", 4)
a2 = Alumno("Luis")
print(a1.nombre, a1.nota)
print(a2.nota)

# B
print(a1.aprobar())
print(a1.subir_nota(2))
print(a1.aprobar())

# C
print(a2)

# D
print(Alumno.total)
print(a1.centro)

# E  ← el más difícil (enlaza con el Tema 2)
a3 = Alumno("Eva", 8)
a4 = Alumno("Eva", 8)
print(a3 == a4)
a5 = a3
a5.nota = 10
print(a3.nota)
print(Alumno.total)