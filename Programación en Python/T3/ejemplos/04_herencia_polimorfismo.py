class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        return "..."

class Perro(Animal):
    def sonido(self):
        return "Guau"

class Gato(Animal):
    def sonido(self):
        return "Miau"

class Robot:
    def sonido(self):
        return "Bip"

def escuchar(objeto):
    return objeto.sonido()

if __name__ == "__main__":
    for objeto in [Perro("Toby"), Gato("Misi"), Robot()]:
        print(escuchar(objeto))
    print("Perro es Animal:", isinstance(Perro("Toby"), Animal))
