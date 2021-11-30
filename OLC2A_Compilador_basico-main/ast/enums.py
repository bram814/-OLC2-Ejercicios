from enum import Enum

class Tipo(Enum):
    NOTHING = 0
    INT64 = 1
    FLOAT64 = 2
    BOOL = 3
    CHAR = 4
    STRING = 5
    ARRAY = 6
    RANGE = 7
    
    ERROR = 8
    REPORTADO = 9

class OpeAritmetica(Enum):
    SUMA = 0
    RESTA = 1
    UNARIO_RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4
    MODULO = 5
    POTENCIA = 6

class OpeRelacional(Enum):
    MAYORQUE = 0
    MENORQUE = 1
    MAYORIGUAL = 2
    MENORIGUAL = 3
    IGUALQUE = 4
    DIFQUE = 5

class OpeLogica(Enum):
    AND = 0
    OR = 1
    NOT = 2
    XOR = 3
