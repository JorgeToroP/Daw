class Caja:
    def __init__(self, n):
        self.n = n
    def doble(self):
        self.n = self.n * 2
        return self.n

c1 = Caja(3)
c2 = c1
c2.doble()
print(c1.n)        # 1
print(c1.doble())  # 2
c3 = Caja(3)
print(c3.n)        # 3



class Contador:
    def __init__(self):
        self.valor = 0
    def sumar(self):
        self.valor += 1

a = Contador()
b = a
c = Contador()
a.sumar()
b.sumar()
c.sumar()
print(a.valor, b.valor, c.valor)
print(id(a), id(b), id(c))