from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0
    
    def __init__(self, marca, entrada):
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(marca, entrada)
            
    def __str__(self):
        return (f''' Id: {self._id_teclado}, Marca: {self._marca} ,Tipo entrada: {self._tipo_entrada}''')
    
    

if __name__ == '__main__':
    teclado1 = Teclado("HP", "USB")
    teclado2 = Teclado("Logitech", "USB-C")
    print(teclado1)
    print(teclado2)