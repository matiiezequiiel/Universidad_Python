from libro import Libro
class Biblioteca:

    def __init__(self,nombre):
        self._nombre = nombre
        self._libros = []
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
        
    @property
    def libros(self):
        return self._libros
    
    @libros.setter
    def libros(self,libros):
        self._libros = libros
    

    def agregar_libro(self,titulo,autor,genero):
        libro = Libro(titulo,autor,genero)
        self._libros.append(libro)
        
    def buscar_libros_por_autor(self,autor):
        print(f"\n Libros del autor : {autor}")
        for libro in self._libros:
            if libro.autor == autor:
                print(f''' Titulo: {libro.titulo}, Autor: {libro.autor} ,Genero: {libro.genero}''')
               
    
    def buscar_libros_por_genero(self,genero):
        print(f"\n Libros del genero : {genero}")
        for libro in self._libros:
            if libro.genero == genero:
                print(f''' Titulo: {libro.titulo}, Autor: {libro.autor} ,Genero: {libro.genero}''')
    
    def mostrar_todos_los_libros(self):
        print(f"\n Total de libros de la biblioteca {self._nombre}")
        for libro in self._libros:
            print(f''' Titulo: {libro.titulo}, Autor: {libro.autor} ,Genero: {libro.genero}''')
    
    def mostrar_libro(self,titulo):
        for libro in self._libros:
            if libro.titulo == titulo:
                print(f''' Titulo: {libro.titulo}, Autor: {libro.autor} ,Genero: {libro.genero}''')
                break