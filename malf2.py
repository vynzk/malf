import ply.lex as lex
import ply.yacc as yacc

variables = {}
# Definición de tokens
tokens = (
    'read',
    'write',
    'if',
    'else',
    'then',
    'endif',
    'while',
    'do',
    'wend',
    'ID',
    'NUM',
    'BOOL',
    'OPERATOR',
    'SEMICOLON',
)

# Expresiones regulares para tokens simples
t_SEMICOLON = r';'
t_ignore = ' \t'

# tokens simples
t_read = r'read'
t_write = r'write'
t_if = r'if'
t_then = r'then'
t_endif = r'endif'
t_while = r'while'
t_do = r'do'
t_wend = r'wend'
t_else = r'else'

# Reglas para tokens más complejos
def t_BOOL(t):
    r'true|false'
    t.value = True if t.value == 'true' else False
    return t

def t_ID(t):
    r'\$[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_OPERATOR(t):
    r'<|<=|>|>=|==|!=|\+|\-|\*|\/|\%'
    return t

# Definición de errores léxicos
def t_error(t):
    print(f"Error léxico: Carácter inesperado '{t.value[0]}'")
    t.lexer.skip(1)

# Definición de reglas sintácticas
def p_statement_list(p):
    '''
    statement_list : statement_list statement
                   | statement
    '''
    pass

def p_statement(p):
    '''
    statement : read_statement
              | if_statement
              | while_statement
              | write_statement
    '''
    pass

def p_read_statement(p):
    'read_statement : read ID SEMICOLON'
    variable_name = p[2]
    valor = int(input(f"Ingrese el valor de {variable_name}: "))
    variables[variable_name] = valor

def p_if_statement(p):
    '''
    if_statement : if condition then statement_list endif
                | if condition then statement_list else statement_list endif
    '''
    if p[1] == 'if':
        if p[2]:
            p[0] = p[4]
        else:
            p[0] = p[6]
def p_else_e(p):
    '''
    else_e : else statement_list
        | 
    '''
    pass


def p_condition(p):
    'condition : BOOL'
    p[0] = p[1]

def p_while_statement(p):
    'while_statement : while condition do statement_list wend'
    while p[2]:
        for statement in p[4]:
            if isinstance(statement, int):
                # Evaluar la expresión en el contexto actual
                print(statement)

def p_write_statement(p):
    'write_statement : write expression SEMICOLON'
    print(p[2])

def p_expression(p):
    '''
    expression : ID
               | NUM
               | expression OPERATOR expression
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = p[1] + p[3]

# Definición de errores sintácticos
def p_error(p):
    if p:
        print(f"Error sintáctico: Token inesperado '{p.value}' en la línea {p.lineno}")
    else:
        print("Error sintáctico: Fin de archivo inesperado")

# Construcción del analizador léxico
lexer = lex.lex()

# Construcción del analizador sintáctico
parser = yacc.yacc()

# Ejemplo de entrada
codigo = """read $n;
if ($n < 2) then
    write $n;
else
    $fib1 = 1;
    $fib2 = 0;
    $i = 2;
    while ($i <= $n) do
        $act = $fib1 + $fib2;
        $fib2 = $fib1;
        $fib1 = $act;
        $i = $i + 1;
    wend;
write $act;
endif;
"""

# Dividir el código en líneas y procesar línea por línea
lineas = codigo.split('\n')
lineas.pop(0)
lineas.pop(-1)

for linea in lineas:
    # Ejecución del analizador sintáctico para cada línea
    result = parser.parse(linea, lexer=lexer)
