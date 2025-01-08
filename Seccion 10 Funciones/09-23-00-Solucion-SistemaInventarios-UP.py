import os 
import platform
def limpiar_consola(): 
    if platform.system() == "Windows": 
        os.system("cls") 
    else: 
        os.system("clear")
        
print("*** Sistema de inventarios (con funciones) ***\n")

lista_productos = []

def mostrar_inventario():
    print("\n--- Inventario detallado actualizado ---")
    for producto in lista_productos:
        id,nombre,precio,cantidad = producto.values()
        print(f'''Id: {id}
        Nombre: {nombre}
        Precio: {precio}
        Cantidad: {cantidad}\n''')

def agregar_producto():
    aux_dict = {}
    print("\nProporciona los valores del producto ")
    aux_dict['id'] = int(input("Id: "))
    aux_dict['nombre'] = input("Nombre: ")
    aux_dict['precio'] = float(input("Precio: "))
    aux_dict['cantidad'] = int(input("Cantidad: "))
    lista_productos.append(aux_dict)
    limpiar_consola()

def buscar_productos(id_producto_buscar):
    encontre_producto = False
    for producto in lista_productos:
        id,nombre,precio,cantidad = producto.values()
        if(id == id_producto_buscar):
            print("Informacion del producto encontrado:")
            print(f'''Id: {id}
            Nombre: {nombre}
            Precio: {precio}
            Cantidad: {cantidad}\n''')
            encontre_producto = True
            break
    
    if(not encontre_producto):
        print("\n No se encontro el producto")
    
salir = False
while not salir:
    print(f'''Menu:
    1. Mostrar inventario
    2. Agregar nuevo producto
    3. Buscar producto por ID
    4. Salir''')
    opcion = int(input('Escoje una opción: '))
    if opcion == 1:
        mostrar_inventario()
    elif opcion == 2:
        agregar_producto()
    elif opcion == 3:
        id_producto_buscar = int(input("\nIngrese el id del producto a buscar: "))
        buscar_productos(id_producto_buscar)
    elif opcion == 4:
        print('Saliendo del sistema. Hasta luego!\n')
        salir = True
    else:
        print('Opción inválida, proporciona otra opción...\n')
else:
    print('Terminando el sistema de inventarios (con funciones)')
    
    
    


