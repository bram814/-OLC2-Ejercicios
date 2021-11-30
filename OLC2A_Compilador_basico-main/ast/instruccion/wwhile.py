from ast.instruccion.instruccion import Instruccion

class While(Instruccion):
    def __init__(self, cond, lsent, linea):
        super().__init__()
        self.cond = cond
        self.lsent = lsent
        self.linea = linea

    def genC3D(self, ent):
        # Linicio:
        #     <cod 3d cond>
        # cond.EV:
        #     <cod 3d Lsent>
        #     goto Linicio
        # cond.EF:

        # Linicio:
        linicio = self.newEti()
        print(f"{linicio}:")
        # cod 3d cond
        self.cond.genC3D(ent)
        # cond.EV
        self.cond.soltar(self.cond.lv)
        # cod 3d Lsent
        self.genC3DLsent(self.lsent, ent)
        # goto Linicio
        print(f"goto {linicio}")
        # cond.EF
        self.cond.soltar(self.cond.lf)
    
    def genParseTree(self):
        ptr1 = self.crearHoja("while")
        ptr2 = self.cond.genParseTree()
        ptr3 = self.crearHoja("do")
        
        ptrs1 = []
        for sent in self.lsent:
            ptrs1.append(sent.genParseTree())

        ptr4 = self.crearNodo("Lsent", ptrs1)
        
        ptrs = []
        ptrs.append(ptr1)
        ptrs.append(ptr2)
        ptrs.append(ptr3)
        ptrs.append(ptr4)

        return self.crearNodo("While", ptrs)