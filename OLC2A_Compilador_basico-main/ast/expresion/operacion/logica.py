from ast.expresion.operacion.condicion import Condicion
from ast.enums import OpeLogica

class Logica(Condicion):
    def __init__(self, op, izq, der, linea):
        super().__init__(op, izq, der, linea)

    def unir(self, l1, l2):
        # cond: cond op cond
        listanueva = []
        for i in l1:
            listanueva.append(i)
        for i in l2:
            listanueva.append(i)
        return listanueva
        
    def genC3D(self, ent):
        if self.op == OpeLogica.OR:
            self.generarOr(ent)
        elif self.op == OpeLogica.XOR:
            self.generarXor(ent)
        elif self.op == OpeLogica.AND:
            self.generarAnd(ent)
        else:
            self.generarNot(ent)

    def generarOr(self, ent):
        # condicion:    condicion or {soltar} condicion {acciones}
        # reducir cond1
        self.izq.genC3D(ent)
        # {soltar}
        self.soltar(self.izq.lf)
        # reducir cond2
        self.der.genC3D(ent)
        # {acciones}
        self.lf = self.der.lf
        self.lv = self.unir(self.izq.lv, self.der.lv)

        # # heredar
        # self.izq.true = self.true
        # self.izq.false = self.newEti()
        # # reducir cond1
        # self.izq.genC3D(ent)
        # self.soltar([self.izq.false])
        # # heredar
        # self.der.true = self.true
        # self.der.false = self.false
        # # reducir cond2
        # self.der.genC3D(ent)

    def generarXor(self, ent):
        # condicion:    condicion xor {soltar} condicion {soltar acciones}
        # reducir cond1
        self.izq.genC3D(ent)
        # {soltar}
        self.soltar(self.izq.lf)
        # reducir cond2
        self.der.genC3D(ent)
        # {soltar}
        self.soltar(self.izq.lv)
        # {acciones}
        # a < b
        print(f"if {self.der.cad} then goto {self.der.lf[0]}")
        print(f"goto {self.der.lv[0]}")
        self.lv = self.der.lv
        self.lf = self.der.lf

        # # condicion:    condicion xor condicion
        # # heredar
        # self.izq.true = self.newEti()
        # self.izq.false = self.newEti()
        # # reducir cond1
        # self.izq.genC3D(ent)
        # self.soltar([self.izq.false])
        # # heredar
        # self.der.true = self.true
        # self.der.false = self.false
        # # reducir cond2
        # self.der.genC3D(ent)
        # # acciones
        # self.soltar([self.izq.true])
        # print(f"if {self.der.cad} then goto {self.der.false}")
        # print(f"goto {self.der.true}")

    def generarAnd(self, ent):
        # condicion:    condicion and {soltar} condicion {acciones}
        # reducir cond1
        self.izq.genC3D(ent)
        # {soltar}
        self.soltar(self.izq.lv)
        # reducir cond2
        self.der.genC3D(ent)
        # {acciones}
        self.lv = self.der.lv
        self.lf = self.unir(self.izq.lf, self.der.lf)

        # # heredar
        # self.izq.true = self.newEti()
        # self.izq.false = self.false
        # # reducir cond1
        # self.izq.genC3D(ent)
        # self.soltar([self.izq.true])
        # # heredar
        # self.der.true = self.true
        # self.der.false = self.false
        # # reducir cond2
        # self.der.genC3D(ent)

    def generarNot(self, ent):
        # condicion:    not condicion {acciones}
        # reducir cond
        self.izq.genC3D(ent)
        # {acciones}
        self.lv = self.izq.lf
        self.lf = self.izq.lv

        # # condicion:    not condicion
        # # heredar
        # self.izq.true = self.false
        # self.izq.false = self.true
        # # reducir cond1
        # self.izq.genC3D(ent)

    def genParseTree(self):
        if self.op == OpeLogica.NOT:
            # condicion: ope condicion {acciones}
            # reducir izq
            ptr1 = self.izq.genParseTree()
            # {acciones}
            ptr2 = self.crearHoja("not")
            ptr = self.crearNodo("condicion", [ptr2, ptr1])
            return ptr
        else:
            # condicion: condicion ope condicion {acciones}

            # reducir izq
            ptr1 = self.izq.genParseTree()
            # reducir der
            ptr2 = self.der.genParseTree()
            # {acciones}
            ptr3 = self.crearHoja(self.getOperador())
            ptr = self.crearNodo("condicion", [ptr1, ptr3, ptr2])
            return ptr

    def getOperador(self):
        if self.op == OpeLogica.AND:
            return "and"
        elif self.op == OpeLogica.OR:
            return "or"
        elif self.op == OpeLogica.XOR:
            return "xor"
        return "not"