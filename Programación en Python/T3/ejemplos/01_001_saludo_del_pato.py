# ejemplo de comentario normal

class Pato:
    """Docstring el pato saluda"""
    def saludar(self):
        return "¡Cuac! Soy un objeto con plumas y metodos."

""" Docstring Ejecuta este bloque solamente si este archivo se ha iniciado directamente"""

if __name__ == "__main__":
    paco = Pato()
    print(paco.saludar())
    """Docstring aqui lo imprimimos"""
