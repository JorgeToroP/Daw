class Pato:
    def __init__(self, nombre):
        self.nombre = nombre

    def __eq__(self, otro):
        return self.nombre == otro.nombre

a = Pato("Paco")
b = Pato("Paco")
print(a == b)
