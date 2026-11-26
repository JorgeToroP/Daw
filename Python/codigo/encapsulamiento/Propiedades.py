class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius
        
    @property
    def celsius(self):
        """Temperatura en grados Celsius"""
        return self._celsius
    
    
    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor
        
    @property
    def fahrenheit(self):
        """Temperatura en grados Fahrenheit"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, valor):
        self.celsius = (valor - 32) * 5/9
        
        
temp = Temperatura()
temp.celsius = 25             # Usa el setter
print(temp.celsius)           # Usa el getter: 25
print(temp.fahrenheit)      # Usa el getter: 77.0
temp.fahrenheit = 68       # Usa el setter
print(temp.celsius)          # Aproximadamente 20.0