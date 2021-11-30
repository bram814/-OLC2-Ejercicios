from ast.instruccion.instruccion import Instruccion

class If(Instruccion):
    def __init__(self, cond, lsent1, lsent2, linea):
        super().__init__()
        self.cond = cond
        self.lsent1 = lsent1
        self.lsent2 = lsent2
        self.linea = linea

    def genC3D(self, ent):
        if self.lsent2 == None:
            #     <cod 3d cond>
            # cond.EV:
            #     <cod 3d Lsent>
            # cond.EF:

            # cod 3d cond
            self.cond.genC3D(ent)
            # cond.EV
            self.cond.soltar(self.cond.lv)
            # cod 3d Lsent
            self.genC3DLsent(self.lsent1, ent)
            # cond.EF
            self.cond.soltar(self.cond.lf)
        else:
            #     <cod 3d cond>
            # cond.EV:
            #     <cod 3d LsentV>
            #     goto Lsalida
            # cond.EF:
            #     <cod 3d LsentF>
            # Lsalida:

            # cod 3d cond
            self.cond.genC3D(ent)
            # cond.EV
            self.cond.soltar(self.cond.lv)
            # cod 3d LsentV
            self.genC3DLsent(self.lsent1, ent)
            # goto Lsalida
            lsalida = self.newEti()
            print(f"goto {lsalida}")
            # cond.EF
            self.cond.soltar(self.cond.lf)
            # cod 3d LsentF
            self.genC3DLsent(self.lsent2, ent)
            # Lsalida:
            print(f"{lsalida}:")

    def genParseTree(self):
        if self.lsent2 == None:
            ptr1 = self.crearHoja("if")
            ptr2 = self.cond.genParseTree()
            ptr3 = self.crearHoja("then")
            ptrs1 = []
            for sent in self.lsent1:
                ptrs1.append(sent.genParseTree())
            ptr4 = self.crearNodo("Lsent", ptrs1)
            ptrs = []
            ptrs.append(ptr1)
            ptrs.append(ptr2)
            ptrs.append(ptr3)
            ptrs.append(ptr4)

            return self.crearNodo("If", ptrs)
        else:
            ptr1 = self.crearHoja("if")
            ptr2 = self.cond.genParseTree()
            ptr3 = self.crearHoja("then")
            
            ptrs1 = []
            for sent in self.lsent1:
                ptrs1.append(sent.genParseTree())

            ptr4 = self.crearNodo("LsentV", ptrs1)
            ptr5 = self.crearHoja("else")
            
            ptrs1 = []
            for sent in self.lsent2:
                ptrs1.append(sent.genParseTree())
            
            ptr6 = self.crearNodo("LsentF", ptrs1)
            ptrs = []
            ptrs.append(ptr1)
            ptrs.append(ptr2)
            ptrs.append(ptr3)
            ptrs.append(ptr4)
            ptrs.append(ptr5)
            ptrs.append(ptr6)

            return self.crearNodo("If", ptrs)