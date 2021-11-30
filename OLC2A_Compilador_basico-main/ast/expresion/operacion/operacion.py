from ast.expresion.expresion import Expresion

class Operacion(Expresion):
    def __init__(self, op, izq, der, linea):
        super().__init__()
        self.op = op
        self.izq = izq
        self.der = der
        self.linea = linea

    def esOperacionUnaria(self):
        return self.der == None
