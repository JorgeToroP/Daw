class Cuenta:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular       # Atributo público
        self._saldo = saldo_inicial # Atributo "protegido" (convención)
        self.__historial = []        # Atributo "privado" (name mangling)
        
# Name mangling       
cuenta = Cuenta("Ana López", 1000)
print(cuenta.titular)    # Acceso normal: "Ana López"
print(cuenta._saldo)     # Técnicamente permitido, pero desaconsejado: 1000


# El nombre real es _NombreClase__nombre
#print(cuenta._Cuenta__historial) # Funciona: []


class CuentaAhorro(Cuenta):
    def __init__(self, titular, saldo_inicial=0, tasa_interes=0.01):
        super().__init__(titular, saldo_inicial)
        self.__historial = ["Cuenta de ahorro creada"] # No colisiona con __historial de Cuenta
        self.tasa_interes = tasa_interes