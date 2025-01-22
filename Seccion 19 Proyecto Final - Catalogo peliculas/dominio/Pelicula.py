class Pelicula:
    
    def __init__(self,nombre):
        self._nombre = nombre
    
    def __str__(self):
        return (f"Pelicula: {self._nombre}")

if __name__ == "__main__":
    peli = Pelicula("batman")
    print(peli)