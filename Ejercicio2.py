# Para un lenguaje que reconoce de matrices numéricas en el que, por ejemplo, la matriz de tres filas
# y tres columnas.
# [ 1, -3,  0 ]
# [-1,  0, -2 ]
# [ 4,  2,  0 ]
# Escriba un esquema de traducción que controle que todas las filas de la matriz tengan la misma cantidad 
# de elementos, de ser así mostrar un mensaje indicado que la definición es la correcta, de lo contrario 
# que indique la cantidad de filas con error

# GRAMATICA
# S ->  E
# E -> ( T )
# T -> T ; F
#   |  F
# F -> F , num
#   |  num

# definir reservadas
reservadas = {
    'int': 'INT',
    'char': 'CHAR',
}

# definir tokens
tokens = [
    'ENTERO',
] + list(reservadas.values())

# tokens


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# construyendo el analizador léxico
import Interprete.ply.lex as lex
lexer = lex.lex()

class Nodo():
    def __init__(self):
        self.cont = 0

def p_init(t):
    'S  :   E'
    t[0] = Nodo()
    t[0].cont = t[1].cont
    # print(t[0].cont)

def p_E(t):
    'E      :  ENTERO EE'
    t[0] = Nodo()
    t[0].cont = t[2].cont + 1
    print(t[0].cont)

def p_E1(t):
    'EE      :   ENTERO EE'
    t[0] = Nodo()
    t[0].cont = t[2].cont + 1


def p_EE(t):
    'EE      :  '
    t[0] = Nodo()
    t[0].cont = 0



def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import Interprete.ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)

parse("12322")
