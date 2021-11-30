from ast.expresion.operacion.operacion import Operacion
from ast.enums import OpeAritmetica
from ast.ast import Ast

class Aritmetica(Operacion):
    def __init__(self, op, izq, der, linea):
        super().__init__(op, izq, der, linea)

    def genC3D(self, ent):
        if self.esOperacionUnaria():
            return self.reducirUnaria(ent)
        return self.reducirBinario(ent)

    def reducirUnaria(self, ent):
        # expresion: - expresion {acciones}
        # reducir exp
        t1 = self.izq.genC3D(ent)
        # acciones
        tn = self.newTemp()
        print(f"{tn} = - {t1}")
        return tn

    def reducirBinario(self, ent):
        # expresion: expresion ope expresion {acciones}
        # reducir izq
        t1 = self.izq.genC3D(ent)
        # reducir der
        t2 = self.der.genC3D(ent)
        # {acciones}
        tn = self.newTemp()
        print(f"{tn} = {t1} {self.getOperador()} {t2}")

        # # reutilizacion de temporales
        # # Generar un nuevo temporal
        # Ast.temp = Ast.temp + 1
        # # Ahora restar temporales el num de temporales del lado derecho
        # Ast.temp = Ast.temp - self.izq.num - self.der.num
        # tn = self.getTemp()
        # self.num = 1
        # print(f"{tn} = {t1} {self.getOperador()} {t2}")

        return tn

    def genParseTree(self):
        if self.der == None:
            # expresion: ope expresion {acciones}
            # reducir izq
            ptr1 = self.izq.genParseTree()
            # {acciones}
            ptr2 = self.crearHoja("-");
            ptr = self.crearNodo("expresion", [ptr2, ptr1])

            return ptr
        else:
            # expresion: expresion ope expresion {acciones}
            # reducir izq
            ptr1 = self.izq.genParseTree()
            # reducir der
            ptr2 = self.der.genParseTree()
            # {acciones}
            ptr3 = self.crearHoja(self.getOperador());
            ptr = self.crearNodo("expresion", [ptr1, ptr3, ptr2])
            return ptr

    def getOperador(self):
        if self.op == OpeAritmetica.SUMA:
            return "+"
        elif self.op == OpeAritmetica.RESTA:
            return "-"
        elif self.op == OpeAritmetica.MULTIPLICACION:
            return "*"
        elif self.op == OpeAritmetica.DIVISION:
            return "/"
        elif self.op == OpeAritmetica.MODULO:
            return "%"
        else:
            return "^"
