class Aritmetica:
    def __init__(self,operando1,operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    
    def sumar(self):
        return self.operando1 + self.operando2
    
    def restar(self):
        return self.operando1 - self.operando2
    
    def multiplicar(self):
        return self.operando1 * self.operando2
    
    def dividir(self):
        return self.operando1 / self.operando2
    
aritmetica1 = Aritmetica(10,2)
aritmetica2 = Aritmetica(100,5)

print("Aritmetica1 sumar: ",aritmetica1.sumar())
print("Aritmetica1 resta: ",aritmetica1.restar())
print("Aritmetica1 multi: ",aritmetica1.multiplicar())
print("Aritmetica1 divid: ",aritmetica1.dividir())

print("\nAritmetica2 sumar: ",aritmetica2.sumar())
print("Aritmetica2 resta: ",aritmetica2.restar())
print("Aritmetica2 multi: ",aritmetica2.multiplicar())
print("Aritmetica2 divid: ",aritmetica2.dividir())