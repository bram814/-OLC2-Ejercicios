from abc import ABC, ABCMeta

class Ast(ABC):
    nodos = 0
    temp = 0
    eti = 0

    def __init__(self):
        __metaclass__ = ABCMeta

    # Metodos para crear temporales y etiquetas
    def newTemp(self):
        Ast.temp = Ast.temp + 1
        return f"t{Ast.temp}"

    def getTemp(self):
        return f"t{Ast.temp}"

    def newEti(self):
        Ast.eti = Ast.eti + 1
        return f"L{Ast.eti}"

    def getEti(self):
        return f"L{Ast.eti}"

    # Metodos para crear el arbol de analisis de sintaxis
    def newNodo(self):
        Ast.nodos = Ast.nodos + 1
        return f"n{Ast.nodos}"
        
    def crearHoja(self, valor):
        ptr = self.newNodo()
        print(f"{ptr} [label=\"{valor}\", color=lightblue2, style=filled]")
        return ptr

    def crearNodo(self, name, ptrs=[]):
        ptr = self.newNodo()
        cad = ""

        print(f"{ptr} [label=\"{name}\", color=lightblue2, style=filled]")
        for i in ptrs:
            cad += f" -> {i}"
            print(f"{ptr} -> {i}")

        ptrrank = self.newNodo()
        print(f"{ptrrank} [style=invisible];")
        print(f"{{rank=same; {ptrrank + cad} [style=invis];}}")

        return ptr