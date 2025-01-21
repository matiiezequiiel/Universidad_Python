from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto,ancho, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho
    
    def __str__(self):
        return (f"Rectangulo: Alto: {self._alto} Ancho: {self._ancho} Color: {self._color} Area: {self.calcular_area()}")


if __name__ == '__main__':
    rectangulo1 = Rectangulo(10,20,"Lila")
    rectangulo2 = Rectangulo(20,25,"Celeste")
    print(rectangulo1)
    print(rectangulo2)