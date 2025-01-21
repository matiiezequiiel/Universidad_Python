from monitor import Monitor
from teclado import Teclado
from raton import Raton
from computadora import Computadora
from orden import Orden

monitor1 = Monitor("HP","20 pulgadas")
teclado1 = Teclado("Logitech", "USB-C")
raton1 = Raton("Logitech", "USB-C")
compu1 = Computadora("Terreneitor 2000", monitor1,teclado1,raton1)

monitor2 = Monitor("Asus","20 pulgadas")
teclado2 = Teclado("Logitech", "Bluethoot")
raton2 = Raton("HP", "USB-C")
compu2 = Computadora("Terreneitor 3000", monitor2,teclado2,raton2)

orden1 = Orden()
orden2 = Orden()
orden1.agregar_computadora(compu1)
orden2.agregar_computadora(compu2)

print(orden1)
print(orden2)