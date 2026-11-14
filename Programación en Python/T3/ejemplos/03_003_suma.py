class Bolsa:
    def __init__(self, galletas):
        self.galletas = galletas

    def __add__(self, otra):
        return self.galletas + otra.galletas

a = Bolsa(3)
b = Bolsa(2)
print(a + b)
