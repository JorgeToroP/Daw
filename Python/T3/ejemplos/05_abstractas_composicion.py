from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base, self.altura = base, altura

    def area(self):
        return self.base * self.altura

class Etiqueta:
    def __init__(self, texto):
        self.texto = texto

class FiguraEtiquetada:
    def __init__(self, figura, texto):
        self.figura = figura  # tiene una Figura: composicion
        self.etiqueta = Etiqueta(texto)

    def describir(self):
        return f"{self.etiqueta.texto}: area {self.figura.area()}"

if __name__ == "__main__":
    print(FiguraEtiquetada(Rectangulo(4, 3), "Mesa").describir())
