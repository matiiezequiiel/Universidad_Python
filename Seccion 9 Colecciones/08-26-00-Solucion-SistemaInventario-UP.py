print("*** Sistema de inventarios ***\n")

cantidad_productos = int(input("Cuantos productos deseas agregar al inventario? "))
lista_productos = []

for i in range(cantidad_productos):
    aux_dict = {}
    print("\nProporciona los valores del producto ", i+1)
    aux_dict['id'] = i
    aux_dict['nombre'] = input("Nombre: ")
    aux_dict['precio'] = float(input("Precio: "))
    aux_dict['cantidad'] = int(input("Cantidad: "))
    lista_productos.append(aux_dict)
#Otra forma de usar el auxiliar, guardando las variables.
#aux_dict = {'id' : i , 'nombre' : nombre, 'precio' : precio ,'cantidad' : cantidad} 

print(lista_productos)

id_producto_buscar = int(input("\nIngrese el id del producto a buscar: "))

for producto in lista_productos:
    id,nombre,precio,cantidad = producto.values()
    print(id,nombre,precio,cantidad)
    if(id == id_producto_buscar):
        print("Informacion del producto encontrado: \n")
        print(f'''Id: {id}
        Nombre: {nombre}
        Precio: {precio}
        Cantidad: {cantidad}\n''')
        break
    

print("--- Inventario detallado actualizado ---\n")
for producto in lista_productos:
    id,nombre,precio,cantidad = producto.values()
    print(f'''Id: {id}
    Nombre: {nombre}
    Precio: {precio}
    Cantidad: {cantidad}\n''')
    

    
    
    