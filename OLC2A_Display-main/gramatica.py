# Definir palabras reservads
reserved = {
    'while': 'while',
    'do': 'do',
    'loop': 'loop',
    'continue': 'continue',
    'break': 'break'
}

# Definir tokens
tokens = [
    'igual',
    'pyc',
    'llai',
    'llad',
    'mas',
    'mayque',
    'menque',
    'entero',
    'id',
] + list(reserved.values())

# Tokens
t_igual             = r'='
t_pyc               = r';'
t_llai              = r'\{'
t_llad              = r'\}'
t_mas               = r'\+'
t_mayque            = r'>'
t_menque            = r'<'

def t_entero(t):
    r'\d+'
    try:
        t.value = (t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_id(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(),'id')    # Check for reserved words
    return t

# Comentario de múltiples líneas /* .. */
def t_comentario_multilinea(t):
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_comentario_simple(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
import Interprete.ply.lex as lex
lexer = lex.lex()

# Asociación de operadores y precedenciaz
precedence = (
    ('right', 'igual'),
    ('nonassoc', 'mayque', 'menque'),
    ('left','mas'),
    )

# Definición de la gramática
ptr = 0
tmp = 0
eti = 0

def newTmp():
    global tmp
    tmp = tmp + 1
    return f"t{tmp}"

def newEtq():
    global eti
    eti = eti + 1
    return f"t{eti + 1}"

class Nodo():
    dir = 0
    Lv = []
    Lf = []

def p_init(t):
    'init   :   sentencias'

# ------------------- Lsent -------------------
def p_sentencias(t):
    '''sentencias   :   sentencias sent
                    |   sent'''

def p_sent_while(t):
    'sent   :   while condicion do llai sentencias llad'

def p_sent_loop(t):
    'sent   :   loop llai sentencias llad'

def p_sent_break(t):
    'sent   :   break pyc'

def p_sent_continue(t):
    'sent   :   continue pyc'

def p_sent_asignacion(t):
    'sent  :   id igual expresion pyc'
    print(f"{t[1]} = {t[3].dir}")

# -------------------- condiciones --------------------
def p_condicion(t):
    '''condicion    :   expresion mayque expresion
                    |   expresion menque expresion'''
    t[0] = Nodo()
    t[0].Lv.append(newEtq())
    t[0].Lf.append(newEtq())
    print(f"if {t[1].dir} {t[2]} {t[3].dir} then goto {t[0].Lv[0]}")
    print(f"goto {t[0].Lf[0]}")

# -------------------- expresiones --------------------

def p_expresion(t):
    'expresion  :   expresion mas expresion'
    t[0] = Nodo()
    t[0].dir = newTmp()
    print(f"{t[0].dir} = {t[1].dir} + {t[3].dir}")

def p_expresion_entero(t):
    'expresion  :   entero'
    t[0] = Nodo()
    t[0].dir = t[1]

def p_expresion_id(t):
    'expresion  :   id'
    t[0] = Nodo()
    t[0].dir = t[1]

# ----------------- produccion error ------------------

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)
    
import ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)

f = open("./entrada.txt", "r")
input = f.read()
parse(input)
