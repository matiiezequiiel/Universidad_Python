from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho
    
    def __str__(self):
        # return (f"Cuadrado: Alto: {self._alto} Ancho: {self._ancho} Color: {self._color} Area: {self.calcular_area()}")
        return (FiguraGeometrica.__str__(self) + " " + Color.__str__(self))

if __name__ == '__main__':
    cuadrado1 = Cuadrado(lado = 6, color= "Verde")
    cuadrado2 = Cuadrado(30,"Naranja")
    print(cuadrado1)
    print(cuadrado2)