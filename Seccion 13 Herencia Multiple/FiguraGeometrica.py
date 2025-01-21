class FiguraGeometrica:
    def __init__(self, ancho, alto):
        # Consideramos que un valor valido es entre 0 y 10.
        if self._validar_valor(ancho):  
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f"Valor erroneo ancho: {self._ancho}")
                        
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f"Valor erroneo alto: {self._alto}")

        

    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self,ancho):
        self._ancho = ancho
        
    @property
    def alto(self):
        return self._alto
    
    @ancho.setter
    def alto(self,alto):
        self._alto = alto
    
    def __str__(self):
        return (f"Alto: {self._alto} Ancho: {self._ancho}")
    
    def _validar_valor(self,valor):
        return True if 0 < valor < 10 else False