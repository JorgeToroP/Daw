class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        self.saldo += cantidad
        return self.saldo

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")

        self.saldo -= cantidad
        return self.saldo

    def consultar_saldo(self):
        return self.saldo

    def __str__(self):
        return f"Titular: {self.titular} | Saldo: {self.saldo:.2f} €"


# Creamos un objeto de la clase Cuenta
cuenta_ana = Cuenta("Ana", 1000)

print(cuenta_ana)

# Depositamos dinero
nuevo_saldo = cuenta_ana.depositar(500)
print(f"Saldo después del depósito: {nuevo_saldo:.2f} €")

# Retiramos dinero
nuevo_saldo = cuenta_ana.retirar(200)
print(f"Saldo después de la retirada: {nuevo_saldo:.2f} €")

# Consultamos el saldo
print(f"Saldo actual: {cuenta_ana.consultar_saldo():.2f} €")