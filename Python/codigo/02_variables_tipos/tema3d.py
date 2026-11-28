class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        return "..."
    def presentarse(self):
        return f"Soy {self.nombre} y digo {self.hablar()}"

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color
    def hablar(self):
        return "Miau"

class Pez(Animal):
    pass

# A
p = Perro("Toby")
print(p.nombre)
print(p.hablar())

# B  ← Pez no escribe nada propio
print(Pez("Nemo").hablar())

# C  ← trampa: presentarse está en Animal, pero ¿qué hablar() usa?
g = Gato("Luna", "negro")
print(g.presentarse())
print(g.color)

# D  ← polimorfismo
for a in [Animal("X"), Perro("Rex"), Gato("Kit", "gris")]:
    print(a.hablar())

# E
print(isinstance(p, Animal))
print(isinstance(Animal("Y"), Perro))

# F  ← encapsulación
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo
    def ver_saldo(self):
        return self.__saldo
c = Cuenta(100)
print(c.ver_saldo())
try:
    print(c.__saldo)
except AttributeError:
    print("Error")