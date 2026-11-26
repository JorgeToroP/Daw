class Temperatura:
    def __init__(self, celsius=0):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Por debajo del cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

if __name__ == "__main__":
    t = Temperatura(25)
    print(t.celsius, t.fahrenheit)
    try:
        t.celsius = -300
    except ValueError as error:
        print("Validacion:", error)
