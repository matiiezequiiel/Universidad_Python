from monitor import Monitor
from teclado import Teclado
from raton import Raton
class Computadora:
    contador_computadoras = 0
    
    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
        
    def __str__(self):
        return (f''' Id: {self._id_computadora} ,Nombre: {self._nombre}  
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}''')

if __name__ == '__main__':
    monitor1 = Monitor("HP","20 pulgadas")
    teclado1 = Teclado("Logitech", "USB-C")
    raton1 = Raton("Logitech", "USB-C")
    compu = Computadora("Terreneitor 2000", monitor1,teclado1,raton1)
    print(compu)
    
    monitor2 = Monitor("Asus","20 pulgadas")
    teclado2 = Teclado("Logitech", "Bluethoot")
    raton2 = Raton("HP", "USB-C")
    compu = Computadora("Terreneitor 3000", monitor2,teclado2,raton2)
    print(compu)