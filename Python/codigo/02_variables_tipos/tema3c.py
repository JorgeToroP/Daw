class Animal:                      # clase PADRE (superclase o clase base)
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        return "..."

class Perro(Animal):               # clase HIJA: hereda de Animal
    def hablar(self):              # SOBRESCRIBE el método del padre
        return "Guau"
    
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)   # el padre se encarga de crear self.nombre
        self.color = color         # el hijo añade lo suyo
        
for a in [Perro("Rex"), Gato("Kit", "gris")]:
    print(a.hablar())     # Guau / Miau: la misma llamada da resultados distintos
    
    
class Temperatura:
    def __init__(self, c):
        self._celsius = c
    @property
    def celsius(self):            # getter: se usa como un atributo → t.celsius
        return self._celsius
    @celsius.setter
    def celsius(self, valor):     # setter: t.celsius = 30, y aquí puedes validar
        if valor < -273:
            raise ValueError("Imposible")
        self._celsius = valor