import ply.lex as lex
import ply.yacc as yacc

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
    'parentesis_izq',
    'parentesis_der'
)

# Expresiones regulares para tokens simples
t_SEMICOLON = r';'
t_ignore = ' \t'
t_parentesis_izq = r'\('
t_parentesis_der = r'\)'
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
    print(f"Read: {p[2]}")

def p_if_statement(p):
    '''
    if_statement : if parentesis_izq condition parentesis_der then statement_list endif SEMICOLON
                | if condition then statement_list else_statement endif SEMICOLON
    '''
    pass

def p_else_statement(p):
    '''
    else_statement : else statement_list
            | 
    '''
    pass
def p_condition(p):
    'condition : BOOL'
    print(f"Condition: {p[1]}")

def p_while_statement(p):
    'while_statement : while condition do statement_list wend SEMICOLON'
    pass

def p_write_statement(p):
    'write_statement : write expression SEMICOLON'
    pass

def p_expression(p):
    '''
    expression : ID
               | NUM
               | expression OPERATOR expression
    '''
    pass

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
# Ejemplo de entrada sin saltos de línea al principio y al final
# Construcción del analizador léxico
lexer = lex.lex()

# Ejemplo de entrada
#codigo = """write 1 + 2;
#write 3 * 4;"""

# Ejecución del analizador léxico
#lexer.input(codigo)
#for token in lexer:
#    print(token)

codigo = """if (true) then write 1; endif;"""

# Ejecución del analizador sintáctico
#parser.parse(codigo)
result = parser.parse(codigo, lexer=lexer)



