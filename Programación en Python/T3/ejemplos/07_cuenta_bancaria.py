class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        if not titular.strip():
            raise ValueError("Titular obligatorio")
        if saldo < 0:
            raise ValueError("Saldo inicial negativo")
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Cantidad positiva requerida")
        self._saldo += cantidad
        return self._saldo

    def retirar(self, cantidad):
        if cantidad <= 0 or cantidad > self._saldo:
            raise ValueError("Retirada no permitida")
        self._saldo -= cantidad
        return self._saldo

if __name__ == "__main__":
    cuenta = CuentaBancaria("Ana", 100)
    print(cuenta.depositar(50))
    print(cuenta.retirar(20))
    print("Saldo:", cuenta.saldo)
