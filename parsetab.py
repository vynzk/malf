
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOL ENTER ID NUM OPERATOR SEMICOLON do else endif if parentesis_der parentesis_izq read then wend while write\n    statement_list : statement_list statement\n                   | statement\n    \n    statement : read_statement\n              | if_statement\n              | while_statement\n              | write_statement\n    read_statement : read ID SEMICOLON\n    if_statement : if parentesis_izq condition parentesis_der then ENTER statement_list ENTER endif SEMICOLON\n                | if parentesis_izq condition parentesis_der then ENTER statement_list ENTER else ENTER statement_list ENTER endif SEMICOLON\n                | if parentesis_izq operando_statement parentesis_der then ENTER statement_list ENTER endif SEMICOLON\n                | if parentesis_izq operando_statement parentesis_der then ENTER statement_list ENTER else ENTER statement_list ENTER endif SEMICOLON\n    condition : BOOL\n    while_statement : while parentesis_izq condition parentesis_der do ENTER statement_list ENTER wend SEMICOLON\n                    | while parentesis_izq operando_statement parentesis_der do ENTER statement_list ENTER wend SEMICOLON\n    write_statement : write expression SEMICOLON\n    expression : ID\n               | NUM\n               | operando_statement\n    \n    operando_statement : expression OPERATOR expression    \n    '
    
_lr_action_items = {'read':([0,1,2,3,4,5,6,11,19,26,37,38,39,40,41,42,43,44,55,56,57,58,59,60,61,62,67,68,],[7,7,-2,-3,-4,-5,-6,-1,-7,-15,7,7,7,7,7,7,7,7,-8,7,-10,7,-13,-14,7,7,-9,-11,]),'if':([0,1,2,3,4,5,6,11,19,26,37,38,39,40,41,42,43,44,55,56,57,58,59,60,61,62,67,68,],[8,8,-2,-3,-4,-5,-6,-1,-7,-15,8,8,8,8,8,8,8,8,-8,8,-10,8,-13,-14,8,8,-9,-11,]),'while':([0,1,2,3,4,5,6,11,19,26,37,38,39,40,41,42,43,44,55,56,57,58,59,60,61,62,67,68,],[9,9,-2,-3,-4,-5,-6,-1,-7,-15,9,9,9,9,9,9,9,9,-8,9,-10,9,-13,-14,9,9,-9,-11,]),'write':([0,1,2,3,4,5,6,11,19,26,37,38,39,40,41,42,43,44,55,56,57,58,59,60,61,62,67,68,],[10,10,-2,-3,-4,-5,-6,-1,-7,-15,10,10,10,10,10,10,10,10,-8,10,-10,10,-13,-14,10,10,-9,-11,]),'$end':([1,2,3,4,5,6,11,19,26,55,57,59,60,67,68,],[0,-2,-3,-4,-5,-6,-1,-7,-15,-8,-10,-13,-14,-9,-11,]),'ENTER':([2,3,4,5,6,11,19,26,33,34,35,36,41,42,43,44,50,52,55,57,59,60,61,62,67,68,],[-2,-3,-4,-5,-6,-1,-7,-15,37,38,39,40,45,46,47,48,56,58,-8,-10,-13,-14,63,64,-9,-11,]),'ID':([7,10,13,14,27,],[12,16,16,16,16,]),'parentesis_izq':([8,9,],[13,14,]),'NUM':([10,13,14,27,],[17,17,17,17,]),'SEMICOLON':([12,15,16,17,18,32,49,51,53,54,65,66,],[19,26,-16,-17,-18,-19,55,57,59,60,67,68,]),'BOOL':([13,14,],[22,22,]),'OPERATOR':([15,16,17,18,21,23,25,32,],[27,-16,-17,-18,-18,27,-18,27,]),'parentesis_der':([16,17,18,20,21,22,24,25,32,],[-16,-17,-18,28,29,-12,30,31,-19,]),'then':([28,29,],[33,34,]),'do':([30,31,],[35,36,]),'endif':([45,46,63,64,],[49,51,65,66,]),'else':([45,46,],[50,52,]),'wend':([47,48,],[53,54,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement_list':([0,37,38,39,40,56,58,],[1,41,42,43,44,61,62,]),'statement':([0,1,37,38,39,40,41,42,43,44,56,58,61,62,],[2,11,2,2,2,2,11,11,11,11,2,2,11,11,]),'read_statement':([0,1,37,38,39,40,41,42,43,44,56,58,61,62,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'if_statement':([0,1,37,38,39,40,41,42,43,44,56,58,61,62,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'while_statement':([0,1,37,38,39,40,41,42,43,44,56,58,61,62,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'write_statement':([0,1,37,38,39,40,41,42,43,44,56,58,61,62,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'expression':([10,13,14,27,],[15,23,23,32,]),'operando_statement':([10,13,14,27,],[18,21,25,18,]),'condition':([13,14,],[20,24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement_list","S'",1,None,None,None),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','malf.py',68),
  ('statement_list -> statement','statement_list',1,'p_statement_list','malf.py',69),
  ('statement -> read_statement','statement',1,'p_statement','malf.py',75),
  ('statement -> if_statement','statement',1,'p_statement','malf.py',76),
  ('statement -> while_statement','statement',1,'p_statement','malf.py',77),
  ('statement -> write_statement','statement',1,'p_statement','malf.py',78),
  ('read_statement -> read ID SEMICOLON','read_statement',3,'p_read_statement','malf.py',83),
  ('if_statement -> if parentesis_izq condition parentesis_der then ENTER statement_list ENTER endif SEMICOLON','if_statement',10,'p_if_statement','malf.py',88),
  ('if_statement -> if parentesis_izq condition parentesis_der then ENTER statement_list ENTER else ENTER statement_list ENTER endif SEMICOLON','if_statement',14,'p_if_statement','malf.py',89),
  ('if_statement -> if parentesis_izq operando_statement parentesis_der then ENTER statement_list ENTER endif SEMICOLON','if_statement',10,'p_if_statement','malf.py',90),
  ('if_statement -> if parentesis_izq operando_statement parentesis_der then ENTER statement_list ENTER else ENTER statement_list ENTER endif SEMICOLON','if_statement',14,'p_if_statement','malf.py',91),
  ('condition -> BOOL','condition',1,'p_condition','malf.py',101),
  ('while_statement -> while parentesis_izq condition parentesis_der do ENTER statement_list ENTER wend SEMICOLON','while_statement',10,'p_while_statement','malf.py',106),
  ('while_statement -> while parentesis_izq operando_statement parentesis_der do ENTER statement_list ENTER wend SEMICOLON','while_statement',10,'p_while_statement','malf.py',107),
  ('write_statement -> write expression SEMICOLON','write_statement',3,'p_write_statement','malf.py',112),
  ('expression -> ID','expression',1,'p_expression','malf.py',117),
  ('expression -> NUM','expression',1,'p_expression','malf.py',118),
  ('expression -> operando_statement','expression',1,'p_expression','malf.py',119),
  ('operando_statement -> expression OPERATOR expression','operando_statement',3,'p_operando_statement','malf.py',124),
]
