class Orden:
    contador_ordenes = 0 
    
    def __init__(self):
        Orden.contador_ordenes += 1 
        self._id_ordenes = Orden.contador_ordenes
        self._computadoras = []
    
    def agregar_computadora(self,computadora):
        self._computadoras.append(computadora)
    
    def __str__(self):
        listado = ""
        for computadora in self._computadoras:
            listado += "\n" + computadora.__str__()
        
        return (f''' Orden: {self._id_ordenes}
        Computadoras: {listado}''')
