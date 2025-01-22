from servicio.CatalogoPeliculas import CatalogoPeliculas
from dominio.Pelicula import Pelicula

print('*** Sistema de Catalogo de peliculas ***')

salir = False
while not salir:
    print(f'''Menu:
    1. Agregar pelicula
    2. Listar peliculas
    3. Eliminar catalogo
    4. Salir''')
    opcion = int(input('Escoje una opción: '))
    if opcion == 1:
        nombre_pelicula = input("Ingrese nombre de la pelicula: ")
        peli = Pelicula(nombre_pelicula)
        CatalogoPeliculas.agregar_pelicula(peli)
        
    elif opcion == 2:
        CatalogoPeliculas.listar_peliculas()
    elif opcion == 3:
        CatalogoPeliculas.eliminar()
    elif opcion == 4:
        print('Saliendo del sistema. Hasta pronto!\n')
        salir = True
    else:
        print('Opción inválida, proporciona otra opción...\n')
else:
    print('Terminando el sistema de Catalogo de peliculas')