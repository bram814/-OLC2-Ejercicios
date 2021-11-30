from ast.ast import Ast

class Expresion(Ast):
    def __init__(self):
        super().__init__()
        # utilizada para reutilización de temporales
        self.num = 0

    def getTipo(self, ent):
        pass

    def genC3D(self, ent):
        pass

    def genParseTree(self):
        pass
