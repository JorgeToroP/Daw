#pauta 1 clase y atributos

class Producto:
    id_global=1
           
    def __init__(self,nombre,precio,cantidad):
        
        self.id = Producto.id_global
        Producto.id_global+=1
        
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
  
#pauta 2 crear lista    
lista_productos = []

def menu():
    try:
        while True:
            print(" 1 - Crear producto")
            print(" 2 - Imprimir lista")
            print(" 3 - Modificar producto")
            print(" 4 - Eliminar producto")
            print(" 5 - Salir")
    

            opcion = int(input("Elige una de las opciones: "))
        
            if opcion == 1:
                crear_producto()
                #continue
            if opcion == 2:
                imprimir_lista()
                #continue
            if opcion == 3:
                actualizar_lista()
                #continue
            if opcion == 4:
                eliminarProductos()
                #continue
            if opcion == 5:
                print("Fin del Programa.....")
                break
    except (ValueError,TypeError):
        print("Elige solamente las opciones del 1 al 5.")
         
#pauta 3 implemetar funciones

#crear productos       
def crear_producto():
    try:
        print("------ Creando un nuevo producto => ")
        #id_producto = int(input("Introduce el ID producto = "))
        nombre_producto = input("Introduce el nombre del producto = ")
        while True: 
                precio_producto = float(input("introduce el precio del producto = "))
                
                cantidad_producto = int(input("Introduce la cantidad de productos = "))
                break           
        nuevo_producto = Producto(nombre_producto,precio_producto,cantidad_producto)         
        lista_productos.append(nuevo_producto)        
        print(f"Nuevo producto creado. =  {nombre_producto}")
    except ValueError:
            print("Error debe ser un numero.")
            
            
#imprimir lista   
def imprimir_lista():
    print("---- Listas de productos ----")
    print(" ")
    encontrado=False
    for lista in lista_productos:
            print(f"Imprimiendo datos del producto {lista.nombre} id = {lista.id} precio = {lista.precio} cantidades = {lista.cantidad}")
        
 
#Actualizar, modificar Productos  (origen de mi calvicie)  
def actualizar_lista():
    
    try:
        id_buscar = int(input("Introduce el id a actualizar = "))

        encontrado = False
        for identi in lista_productos:
            if identi.id == id_buscar:
                encontrado = True
                
                while True:      
                    #print(" 1 - Modificar id producto. {mortal (|8)}")
                    print(" 1 - Modificar el nombre del producto")
                    print(" 2 - Modificar el precio del producto")
                    print(" 3 - Modificar la cantidad")
                    print(" 4 - salir")
                    try:
                        opcion = int(input("Elige una opcion : "))
                    except (ValueError,TypeError,IndexError):    
                        print("Elige solamente las opciones del 1 al 4.")
                        continue
                                    
                    if opcion == 1:
                        #for li in lista_productos:
                            print(f"Modificando el nombre del producto : {identi.nombre}")
                            identi.nombre= input("Introduce el nuevo nombre del producto : ")
                            print(f"Cambio realizado con exito nuevo nombre del producto  = {identi.nombre}")
                            #break
                    if opcion ==2:
                        #for li in lista_productos:
                            identi.precio = float(input(f"Introduce el nuevo precio del producto {identi.nombre} = " ))
                            print(f"Cambio realizado con exito nuevo precio = {identi.precio}")
                            #break
                    if opcion ==3:
                        #for li in lista_productos:
                            identi.cantidad = int(input(f"Nueva cantidad del producto {identi.nombre} = "))
                            print(f"Cambio realizado con exito nueva cantidad = {identi.cantidad}")
                        # break
                    if opcion==4:
                        print("saliendo del modificador. ")
                        break                
        if not encontrado:
            print("Producto no encontrado.")
        
    except ValueError:
        print("Error : dato no valido, solo numeros enteros.")
        return
                        
def eliminarProductos(): #extra;e java 
    try:
        id_buscado = int(input("Introduce el id del producto a eliminar = "))
    except ValueError:
        print("dato incorrecto. Debes introducir un numero entero.")
        return
           
    for li in lista_productos:
        if li.id == id_buscado:
            print(f"eliminando {li.nombre}")
            lista_productos.remove(li)
            print("Producto eliminado con exito")#;
            break#;
        
menu()