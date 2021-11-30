from ast.expresion.expresion import Expresion

# Clase litera son los valores int, string, bool, etc
class Literal(Expresion):

    def __init__(self, tipo, valor, linea):
        super().__init__()
        self.tipo = tipo
        self.valor = valor
        self.linea = linea

    def genC3D(self, ent):
        return self.valor

    def genParseTree(self):
        ptr1 = self.crearHoja(self.valor)
        return self.crearNodo("expresion", [ptr1])
