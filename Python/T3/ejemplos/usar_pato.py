#ejemplo de uso de pato
import importlib

# Importamos el archivo 01_001_saludo_del_pato.py
modulo_pato = importlib.import_module("01_001_saludo_del_pato")

# Obtenemos la clase Pato del módulo
Pato = modulo_pato.Pato

# Creamos y utilizamos un objeto
donald = Pato()
print(donald.saludar())