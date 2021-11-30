from ast.ast import Ast
from entorno.entorno import Entorno

class Arbol(Ast):
    def __init__(self, lsent):
        super().__init__()
        self.lsent = lsent

    def genC3D(self):
        ent = Entorno(None)
        for sent in self.lsent:
            sent.genC3D(ent)

    def genParseTree(self):
        ptrs = []
        for sent in self.lsent:
            ptrs.append(sent.genParseTree())
        ptrRoot = self.crearNodo("Init", ptrs)
        return ptrRoot