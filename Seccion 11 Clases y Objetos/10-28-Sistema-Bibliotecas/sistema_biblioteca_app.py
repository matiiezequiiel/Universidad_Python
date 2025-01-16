from biblioteca import Biblioteca
from libro import Libro

biblioteca_1 = Biblioteca("Biblioteca Nacional")

biblioteca_1.agregar_libro("Libro 1" , "Matias" , "Ficcion")
biblioteca_1.agregar_libro("Libro 2" , "Matias" , "Terror")
biblioteca_1.agregar_libro("Libro 3" , "Juan" , "Drama")
biblioteca_1.agregar_libro("Libro 4" , "Claudia" , "Fantasia")
biblioteca_1.agregar_libro("Libro 5" , "Pedro" , "Ficcion")
biblioteca_1.agregar_libro("Libro 6" , "Pedro" , "Fantasia")

biblioteca_1.buscar_libros_por_autor("Matias")
biblioteca_1.buscar_libros_por_genero("Fantasia")
biblioteca_1.mostrar_todos_los_libros()
biblioteca_1.mostrar_libro("Libro 3")

