class MonstruoGalletas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.galletas_comidas = 0

    def comer(self):
        self.galletas_comidas += 1
        return f"{self.nombre}: ¡ÑAM! Ya llevo {self.galletas_comidas}."

    def informar(self):
        return f"{self.nombre} ha comido {self.galletas_comidas} galletas."


if __name__ == "__main__":
    tragon = MonstruoGalletas("Tragón")
    prudente = MonstruoGalletas("Prudente")

    print(tragon.comer())
    print(tragon.comer())
    print(prudente.comer())

    print(tragon.informar())
    print(prudente.informar())
    print("¿Son el mismo monstruo?", tragon is prudente)

