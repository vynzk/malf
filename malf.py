import ply.lex as lex
import ply.yacc as yacc
global variables
variables = {}
global errores
errores = 0
def gramatica(codigo):
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
        r'\+|\-|\*|\/|<=|>=|<|>|==|!='
        return t

    # Definición de errores léxicos
    def t_error(t):
        print(f"Error léxico: Carácter inesperado '{t.value[0]}'")
        global errores
        errores += 1
        t.lexer.skip(1)

    # Definición de reglas sintácticas
    def p_statement_list(p):
        '''
        statement_list : statement_list statement ENTER
                    | statement ENTER
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
        pass

    def p_read_statement(p):
        'read_statement : read ID SEMICOLON'
        pass

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
        pass

    def p_while_statement(p):
        '''
        while_statement : while parentesis_izq condition parentesis_der do ENTER statement_list wend SEMICOLON
                        | while parentesis_izq operando_statement parentesis_der do ENTER statement_list wend SEMICOLON
        '''
        pass

    def p_write_statement(p):
        'write_statement : write expression SEMICOLON'

    def p_expression(p):
        '''
        expression : ID
                | NUM
                | operando_statement
        '''
        pass

    def p_operando_statement(p):
        '''
        operando_statement : expression OPERATOR expression
                            | expression OPERATOR ID    
        '''
        pass


    # Definición de errores sintácticos
    def p_error(p):
        global errores
        if p:
            print(f"Error sintáctico: Token inesperado '{p.value}' en la línea {p.lineno}")
            errores += 1
        else:
            print("Error sintáctico: Fin de archivo inesperado")
            errores += 1

    # Construcción del analizador léxico
    lexer = lex.lex()
    parser = yacc.yacc()
    lexer = lex.lex()
    parser.parse(codigo, lexer=lexer)
    return 

# ejecutar codigo
def ejecutar(codigo):
    
    

codigo = """write 1;
read $a;
if ($a != $b) then
    write 1;
    $a = 1;
    $b = 2;
    $a = $a + $b;
else
    write 0;
endif;"""

if (errores == 0):
    print("---- El código es correcto ----")
    ejecutar(codigo)

