# 04_input_calculadora.py
# Entrada por teclado y conversión de tipos.
# -*- coding: utf-8 -*-

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

print("Suma:", numero1 + numero2)
print("Resta:", numero1 - numero2)
print("Multiplicación:", numero1 * numero2)

if numero2 != 0:
    print("División:", numero1 / numero2)
else:
    print("No se puede dividir entre cero")
