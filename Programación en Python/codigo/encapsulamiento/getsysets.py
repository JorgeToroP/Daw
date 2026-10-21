class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius
        
    def get_celsius(self):
        return self._celsius
    
    def set_celsius(self, valor):
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor
        
    def get_fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    def set_fahrenheit(self, valor):
        self.set_celsius((valor - 32) * 5/9)
        
temp = Temperatura()
temp.set_celsius(25)
print(temp.get_celsius())     # 25
print(temp.get_fahrenheit()) # 77.0