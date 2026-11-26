productos=["laptop", "smartphone", "tableta", "auriculares","monitor"]
print(productos)

precios_dict= {
    "laptop":800,
               "smartphone":500,
               "tableta":300,
               "auriculares":50,
               "monitor":200
            }
print(precios_dict)

productos_agotados={"tablet", "auriculares"}
print(productos_agotados)

producto_destacado = (productos[0], precios_dict[productos[0]])
print("5. producto destecado : ", producto_destacado)



#//////////////////////////////////////////////////////////////
precios_dict["impresora"]=100
print("Añadiendo impresora : ", precios_dict)

#eliminar tableta de productos
print("Eliminar tableta de productos")
productos.remove("tableta")
print(productos)

#crea un nuevo diccionario
productos_disponibles_dict={}
for producto in productos:
    if producto not in productos_agotados:
        productos_disponibles_dict[producto] = precios_dict[producto]
print("Crear un diccionario con los productos disponibles.")
print(productos_disponibles_dict)



#calcular el precio total de todos los productos disponibles
total_invetario=(sum(productos_disponibles_dict.values()))
print("total invetario : ",total_invetario)

#imprime todas las estructuras de datos 
