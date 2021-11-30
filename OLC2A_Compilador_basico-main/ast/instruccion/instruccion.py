
from ast.ast import Ast

class Instruccion(Ast):
    def __init__(self):
        super().__init__()
    
    def genC3D(self, ent):
        pass

    def genC3DLsent(self, lsent, ent):
        for sent in lsent:
            sent.genC3D(ent)

    def genParseTree(self):
        pass
