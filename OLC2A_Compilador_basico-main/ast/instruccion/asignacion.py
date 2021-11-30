from ast.instruccion.instruccion import Instruccion

class Asignacion(Instruccion):
    def __init__(self, id, exp, linea):
        super().__init__()
        self.id = id
        self.exp = exp
        self.linea = linea

    def genC3D(self, ent):
        # reducir expresion
        dir = self.exp.genC3D(ent)
        print(f"{self.id} = {dir}")

    def genParseTree(self):
        ptr1 = self.crearHoja(self.id)
        ptr2 = self.crearHoja("=")
        ptr3 = self.exp.genParseTree()
        return self.crearNodo("asign", [ptr1, ptr2, ptr3])
