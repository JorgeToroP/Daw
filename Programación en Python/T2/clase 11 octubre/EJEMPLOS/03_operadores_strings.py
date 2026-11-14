# 03_operadores_strings.py
# Operadores y cadenas de texto.

a = 10
b = 3

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Resto:", a % b)
print("Potencia:", a ** b)

nombre = "Ana"
edad = 25
mensaje = f"Me llamo {nombre} y tengo {edad} años"
print(mensaje)

texto = "  Python es genial  "
print(texto.upper())
print(texto.lower())
print(texto.strip())
print(texto.replace("genial", "útil"))
