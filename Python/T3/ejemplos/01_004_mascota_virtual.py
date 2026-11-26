class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 5
        self.hambre = 5

    def jugar(self):
        if self.energia < 2:
            return f"{self.nombre} está agotado. Se hace el dormido."

        self.energia -= 2
        self.hambre += 1
        return f"{self.nombre} persigue un calcetín invisible."

    def alimentar(self):
        if self.hambre == 0:
            return f"{self.nombre} mira la comida y juzga tus decisiones."
        self.energia += 1
        self.hambre -= 1
        return f"{self.nombre} devora una croqueta digital."

    def dormir(self):
        self.energia = 5
        return f"{self.nombre} duerme y ronca en código binario."

    def estado(self):
        return f"{self.nombre}: energía={self.energia}, hambre={self.hambre}"


if __name__ == "__main__":
    pixel = MascotaVirtual("Pixel")

    print(pixel.estado())
    print(pixel.jugar())
    print(pixel.jugar())
    print(pixel.jugar())
    print(pixel.alimentar())
    print(pixel.dormir())
    print(pixel.estado())

