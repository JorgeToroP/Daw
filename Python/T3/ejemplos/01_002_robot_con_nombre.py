class Robot:
    def __init__(self, nombre, trabajo):
        self.nombre = nombre
        self.trabajo = trabajo

    def presentarse(self):
        return f"Soy {self.nombre} y mi trabajo es {self.trabajo}. Bip, bop."


if __name__ == "__main__":
    r2 = Robot("R2-Tostadas", "vigilar la tostadora")
    c3 = Robot("C3-Puré", "traducir recetas de la abuela")

    print(r2.presentarse())
    print(c3.presentarse())

