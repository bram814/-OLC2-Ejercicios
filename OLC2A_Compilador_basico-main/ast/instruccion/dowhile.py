from ast.instruccion.instruccion import Instruccion

class DoWhile(Instruccion):
    def __init__(self, lsent, cond, linea):
        super().__init__()
        self.cond = cond
        self.lsent = lsent
        self.linea = linea

    def genC3D(self, ent):
        # Linicio:
        #     <cod 3d Lsent>
        #     <cod 3d cond>
        # cond.EV:
        #     goto Linicio
        # cond.EF:

        # Linicio:
        linicio = self.newEti()
        print(f"{linicio}:")
        # cod 3d Lsent
        self.genC3DLsent(self.lsent, ent)
        # cod 3d cond
        self.cond.genC3D(ent)
        # cond.EV
        self.cond.soltar(self.cond.lv)
        # goto Linicio
        print(f"goto {linicio}")
        # cond.EV
        self.cond.soltar(self.cond.lf)

    def genParseTree(self):
        ptr1 = self.crearHoja("do")
        
        ptrs1 = []
        for sent in self.lsent:
            ptrs1.append(sent.genParseTree())

        ptr2 = self.crearNodo("Lsent", ptrs1)
        ptr3 = self.crearHoja("while")
        ptr4 = self.cond.genParseTree()
        
        ptrs = []
        ptrs.append(ptr1)
        ptrs.append(ptr2)
        ptrs.append(ptr3)
        ptrs.append(ptr4)

        return self.crearNodo("DoWhile", ptrs)