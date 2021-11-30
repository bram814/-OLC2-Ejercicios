from ast.expresion.operacion.operacion import Operacion
from ast.enums import OpeLogica

class Condicion(Operacion):
    def __init__(self, op, izq, der, linea):
        super().__init__(op, izq, der, linea)
        self.cad = ""
        self.lv = []
        self.lf = []
        self.true = ""
        self.false = ""

    def soltar(self, lista):
        # L1:
        for i in lista:
            print(f"{i}:")
