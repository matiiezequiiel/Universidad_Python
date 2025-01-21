from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0
    
    def __init__(self, marca, entrada):
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(marca, entrada)
    
    def __str__(self):
        return (f''' Id: {self._id_raton}, Marca: {self._marca} ,Tipo entrada: {self._tipo_entrada}''')

if __name__ == '__main__':
    raton1 = Raton("HP", "USB")
    raton2 = Raton("Logitech", "USB-C")
    print(raton1)
    print(raton2)