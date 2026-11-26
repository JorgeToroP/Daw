frase = " Python es un lenguaje de programacion versatil "
mayuscula = frase.upper()
print(mayuscula)

minuscula = frase.lower()
print(minuscula)

contador_a = frase.count("a")
print(contador_a)

nueva_frase = frase.replace("versatil","poderoso")
print (nueva_frase)

palabras = frase.split()
print ("ejercicio 5 : ",palabras) 

comienza_con_python = frase.startswith("Python")
print(comienza_con_python)

posicion_lenguaje = frase.find("lenguaje")
print(posicion_lenguaje)

sin_espacion = frase.strip()
print(sin_espacion)
