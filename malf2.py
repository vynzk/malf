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
    'ENTER',
    'parentesis_izq',
    'parentesis_der',
    'EQUALS'
)

# Expresiones regulares para tokens simples
t_SEMICOLON = r';'
t_ignore = ' \t'
t_parentesis_izq = r'\('
t_parentesis_der = r'\)'
t_ENTER = r'\n'
t_EQUALS = r'='  # Expresión regular para la asignación
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
    statement_list : statement_list statement ENTER
                   | statement ENTER
                   | continue_if_statement
                   | statement_list statement
                   | statement
    '''
    pass

def p_statement(p):
    '''
    statement : read_statement
              | if_statement
              | while_statement
              | write_statement
              | assignment_statement
    '''
    pass

def p_assignment_statement(p):
    'assignment_statement : ID EQUALS expression SEMICOLON'
    variables[p[1]] = p[3]
    p[0] = f"Assignment to : {p[1]} = {p[3]}"
    print(p[0])

def p_read_statement(p):
    'read_statement : read ID SEMICOLON'
    variable_name = p[2]
    user_input = input(f"Enter value for {variable_name}: ")
    try:
        variables[variable_name] = int(user_input)
        print(f"{variable_name} set to {user_input}")
    except ValueError:
        print(f"Error: {user_input} is not a valid integer.")

def p_if_statement(p):
    '''
    if_statement : if parentesis_izq condition parentesis_der then ENTER statement_list endif SEMICOLON
                | if parentesis_izq condition parentesis_der then ENTER statement_list else ENTER statement_list endif SEMICOLON
                | if parentesis_izq operando_statement parentesis_der then ENTER statement_list endif SEMICOLON
                | if parentesis_izq operando_statement parentesis_der then ENTER statement_list else ENTER statement_list endif SEMICOLON
    '''
    pass

def p_condition(p):
    'condition : BOOL'
    print(f"Condition: {p[1]}")

def p_while_statement(p):
    '''
    while_statement : while parentesis_izq condition parentesis_der do ENTER statement_list wend SEMICOLON
                    | while parentesis_izq operando_statement parentesis_der do ENTER statement_list wend SEMICOLON
    '''
    pass

def p_write_statement(p):
    'write_statement : write expression SEMICOLON'
    print(p[2])

def p_expression(p):
    '''
    expression : ID
               | NUM
               | operando_statement
    '''
    p[0] = p[1]
    pass

def p_operando_statement(p):
    '''
    operando_statement : expression OPERATOR expression
                        | expression OPERATOR ID    
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] != 0:
            p[0] = p[1] / p[3]
        else:
            print("Error: Division by zero")
            p[0] = None
    elif p[2] == '%':
        if isinstance(p[1], int) and isinstance(p[3], int):
            p[0] = p[1] % p[3]
        else:
            print("Error: Modulo operation requires integer operands")
            p[0] = None
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]

# Regla para manejar la entrada continua después del "if"
def p_continue_if_statement(p):
    '''
    continue_if_statement : if ENTER statement_list endif SEMICOLON
                         | if ENTER statement_list else ENTER statement_list endif SEMICOLON
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
parser = yacc.yacc()

while True:
    try:
        # Lee una línea de entrada del usuario
        line = input(">>> ")
        # Si la línea no está vacía, agrégala al código y procesa
        if line.strip():
            codigo = line
            try:
                result = parser.parse(codigo, lexer=lexer)
            except SyntaxError:
                print("Error de sintaxis. Continuación esperada.")
                # Lee más líneas hasta que se complete la estructura
                while True:
                    try:
                        next_line = input("... ")
                        codigo += "\n" + next_line
                        # Reinicia el parser para limpiar el estado anterior
                        parser.restart()
                        result = parser.parse(codigo, lexer=lexer)
                        break
                    except SyntaxError:
                        continue
    except EOFError:
        break
print("Variables después de la ejecución:", variables)
