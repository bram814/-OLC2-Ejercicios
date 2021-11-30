from ast.expresion.expresion import Expresion
from ast.enums import Tipo

class Nothing(Expresion):

    def __init__(self):
        pass

    def getValor(self):
        return "null"
