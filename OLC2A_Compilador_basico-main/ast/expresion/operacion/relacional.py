from ast.expresion.operacion.condicion import Condicion
from ast.enums import OpeRelacional

class Relacional(Condicion):
    def __init__(self, op, izq, der, linea):
        super().__init__(op, izq, der, linea)

    def genC3D(self, ent):
        # condicion:    expresion oprel expresion {acciones}
        # reducir cond1
        t1 = self.izq.genC3D(ent)
        # reducir cond2
        t2 = self.der.genC3D(ent)
        # acciones
        # creamos etiquetas verdaderas y falsas
        lv = self.newEti()
        lf = self.newEti()
        # agregamos a una lista
        self.lv.append(lv)
        self.lf.append(lf)
        # generamos codigo
        # a > b
        self.cad = f"{t1} {self.getOperador()} {t2}"
        print(f"if {self.cad} then goto {lv}")
        print(f"goto {lf}")

        # # condicion:    expresion oprel expresion
        # print(f"if {self.cad} then goto {self.true}")
        # print(f"goto {self.false}")


    def genParseTree(self):
        # condicion: expresion oprel expresion {acciones}
        # reducir izq
        ptr1 = self.izq.genParseTree()
        # reducir der
        ptr2 = self.der.genParseTree()
        # {acciones}
        ptr3 = self.crearHoja(self.getOperador())
        ptr = self.crearNodo("condicion", [ptr1, ptr3, ptr2])
        return ptr

    def getOperador(self):
        if self.op == OpeRelacional.MAYORQUE:
            return ">"
        elif self.op == OpeRelacional.MENORQUE:
            return "<"
        elif self.op == OpeRelacional.MAYORIGUAL:
            return ">="
        elif self.op == OpeRelacional.MENORIGUAL:
            return "<="
        elif self.op == OpeRelacional.IGUALQUE:
            return "=="
        else:
            return "!="
