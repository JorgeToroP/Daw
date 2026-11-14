class Caja:
    def __init__(self):
        self.objetos = []

    def guardar(self, objeto):
        self.objetos.append(objeto)

    def __len__(self):
        return len(self.objetos)

caja = Caja()
caja.guardar("pato")
print(len(caja))
