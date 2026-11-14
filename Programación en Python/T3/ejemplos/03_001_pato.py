class Pato:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Pato: {self.nombre}"

paco = Pato("Paco")
print(paco)
