import os
from dominio.Pelicula import Pelicula

class CatalogoPeliculas:
    ruta_archivo = "peliculas.txt"
    
    @classmethod
    def agregar_pelicula(cls,pelicula):
        with open(cls.ruta_archivo,"a",encoding="utf8") as catalogo:
            catalogo.write(pelicula.__str__() + "\n")
            print("Pelicula agregada al catalogo")
            
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo,"r",encoding="utf8") as catalogo:
            print(catalogo.read())
    
    @classmethod
    def eliminar(cls):
        os.remove(cls.ruta_archivo)
        print("Archivo eliminado: " ,cls.ruta_archivo)