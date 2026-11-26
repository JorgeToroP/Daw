class Circulo:
    def __init__(self, radio):
        self._radio = radio
        
        
    @property
    def radio(self):
        return self._radio
    
    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError("El radio debe ser positivo")
        self._radio = valor
        
    @property
    def area(self):
        """Área del círculo (solo lectura)"""
        import math
        return math.pi * self._radio ** 2
    
    @property
    def perimetro(self):
        """Perímetro del círculo (solo lectura)"""
        import math
        return 2 * math.pi * self._radio
    


c = Circulo(5)
print(c.area)       # ~78.54
c.radio = 10        # Permitido, usa el setter
print(c.area)       # ~314.16

# c.area = 100      # Esto daría error: AttributeError: can't set attribute