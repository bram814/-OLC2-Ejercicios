from ast.instruccion.instruccion import Instruccion

class For(Instruccion):
    def __init__(self, id, exp1, exp2, lsent, linea):
        super().__init__()
        self.id = id
        self.exp1 = exp1
        self.exp2 = exp2
        self.lsent = lsent
        self.linea = linea

    def genC3D(self, ent):
        # cod 3d exp1
        dir1 = self.exp1.genC3D(ent)
        # id = E1.dir
        print(f"{self.id} = {dir1}")
        # cod 3d exp2
        dir2 = self.exp2.genC3D(ent)
        # Linicio:
        linicio = self.newEti()
        lsalida = self.newEti()
        print(f"{linicio}:")
        # if id > E2.dir then goto Lsalida
        print(f"if {self.id} > {dir2} then goto {lsalida}")
        # cod 3d Lsent
        self.genC3DLsent(self.lsent, ent)
        # id = id + 1
        print(f"{self.id} = {self.id} + 1")
        # goto Linicio
        print(f"goto {linicio}")
        # Lsalida:
        print(f"{lsalida}:")

    def genParseTree(self):
        ptr1 = self.crearHoja("For")
        ptr2 = self.crearHoja(self.id)
        ptr3 = self.crearHoja("=")
        ptr4 = self.exp1.genParseTree()
        ptr5 = self.crearHoja("to")
        ptr6 = self.exp2.genParseTree()
        ptr7 = self.crearHoja("do")
        ptrs1 = []
        for sent in self.lsent:
            ptrs1.append(sent.genParseTree())
        ptr8 = self.crearNodo("Lsent", ptrs1)
        
        ptrs = []
        ptrs.append(ptr1)
        ptrs.append(ptr2)
        ptrs.append(ptr3)
        ptrs.append(ptr4)
        ptrs.append(ptr5)
        ptrs.append(ptr6)
        ptrs.append(ptr7)
        ptrs.append(ptr8)
        
        return self.crearNodo("For", ptrs)