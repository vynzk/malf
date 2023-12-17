
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOL ENTER EQUALS ID NUM OPERATOR SEMICOLON do else endif if parentesis_der parentesis_izq read then wend while write\n        statement_list : statement_list statement ENTER\n                    | statement ENTER\n                    | statement_list statement\n                    | statement\n        \n        statement : read_statement\n                | if_statement\n                | while_statement\n                | write_statement\n                | assignment_statement\n        assignment_statement : ID EQUALS expression SEMICOLONread_statement : read ID SEMICOLON\n        if_statement : if parentesis_izq condition parentesis_der then ENTER statement_list endif SEMICOLON\n                    | if parentesis_izq condition parentesis_der then ENTER statement_list else ENTER statement_list endif SEMICOLON\n                    | if parentesis_izq operando_statement parentesis_der then ENTER statement_list endif SEMICOLON\n                    | if parentesis_izq operando_statement parentesis_der then ENTER statement_list else ENTER statement_list endif SEMICOLON\n        condition : BOOL\n        while_statement : while parentesis_izq condition parentesis_der do ENTER statement_list wend SEMICOLON\n                        | while parentesis_izq operando_statement parentesis_der do ENTER statement_list wend SEMICOLON\n        write_statement : write expression SEMICOLON\n        expression : ID\n                | NUM\n                | operando_statement\n        \n        operando_statement : expression OPERATOR expression\n                            | expression OPERATOR ID    \n        '
    
_lr_action_items = {'read':([0,1,2,3,4,5,6,7,13,14,23,24,32,34,45,46,47,48,49,50,51,52,59,60,61,62,63,64,65,66,69,70,],[8,8,-4,-5,-6,-7,-8,-9,-3,-2,-1,-11,-19,-10,8,8,8,8,8,8,8,8,-12,8,-14,8,-17,-18,8,8,-13,-15,]),'if':([0,1,2,3,4,5,6,7,13,14,23,24,32,34,45,46,47,48,49,50,51,52,59,60,61,62,63,64,65,66,69,70,],[10,10,-4,-5,-6,-7,-8,-9,-3,-2,-1,-11,-19,-10,10,10,10,10,10,10,10,10,-12,10,-14,10,-17,-18,10,10,-13,-15,]),'while':([0,1,2,3,4,5,6,7,13,14,23,24,32,34,45,46,47,48,49,50,51,52,59,60,61,62,63,64,65,66,69,70,],[11,11,-4,-5,-6,-7,-8,-9,-3,-2,-1,-11,-19,-10,11,11,11,11,11,11,11,11,-12,11,-14,11,-17,-18,11,11,-13,-15,]),'write':([0,1,2,3,4,5,6,7,13,14,23,24,32,34,45,46,47,48,49,50,51,52,59,60,61,62,63,64,65,66,69,70,],[12,12,-4,-5,-6,-7,-8,-9,-3,-2,-1,-11,-19,-10,12,12,12,12,12,12,12,12,-12,12,-14,12,-17,-18,12,12,-13,-15,]),'ID':([0,1,2,3,4,5,6,7,8,12,13,14,16,17,18,23,24,32,33,34,45,46,47,48,49,50,51,52,59,60,61,62,63,64,65,66,69,70,],[9,9,-4,-5,-6,-7,-8,-9,15,20,-3,-2,20,20,20,-1,-11,-19,40,-10,9,9,9,9,9,9,9,9,-12,9,-14,9,-17,-18,9,9,-13,-15,]),'$end':([1,2,3,4,5,6,7,13,14,23,24,32,34,59,61,63,64,69,70,],[0,-4,-5,-6,-7,-8,-9,-3,-2,-1,-11,-19,-10,-12,-14,-17,-18,-13,-15,]),'ENTER':([2,3,4,5,6,7,13,24,32,34,41,42,43,44,54,56,59,61,63,64,69,70,],[14,-5,-6,-7,-8,-9,23,-11,-19,-10,45,46,47,48,60,62,-12,-14,-17,-18,-13,-15,]),'endif':([2,3,4,5,6,7,13,14,23,24,32,34,49,50,59,61,63,64,65,66,69,70,],[-4,-5,-6,-7,-8,-9,-3,-2,-1,-11,-19,-10,53,55,-12,-14,-17,-18,67,68,-13,-15,]),'else':([2,3,4,5,6,7,13,14,23,24,32,34,49,50,59,61,63,64,69,70,],[-4,-5,-6,-7,-8,-9,-3,-2,-1,-11,-19,-10,54,56,-12,-14,-17,-18,-13,-15,]),'wend':([2,3,4,5,6,7,13,14,23,24,32,34,51,52,59,61,63,64,69,70,],[-4,-5,-6,-7,-8,-9,-3,-2,-1,-11,-19,-10,57,58,-12,-14,-17,-18,-13,-15,]),'EQUALS':([9,],[16,]),'parentesis_izq':([10,11,],[17,18,]),'NUM':([12,16,17,18,33,],[21,21,21,21,21,]),'SEMICOLON':([15,19,20,21,22,25,39,40,53,55,57,58,67,68,],[24,32,-20,-21,-22,34,-23,-20,59,61,63,64,69,70,]),'BOOL':([17,18,],[28,28,]),'OPERATOR':([19,20,21,22,25,27,29,31,39,40,],[33,-20,-21,-22,33,-22,33,-22,33,-20,]),'parentesis_der':([21,22,26,27,28,30,31,39,40,],[-21,-22,35,36,-16,37,38,-23,-20,]),'then':([35,36,],[41,42,]),'do':([37,38,],[43,44,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement_list':([0,45,46,47,48,60,62,],[1,49,50,51,52,65,66,]),'statement':([0,1,45,46,47,48,49,50,51,52,60,62,65,66,],[2,13,2,2,2,2,13,13,13,13,2,2,13,13,]),'read_statement':([0,1,45,46,47,48,49,50,51,52,60,62,65,66,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'if_statement':([0,1,45,46,47,48,49,50,51,52,60,62,65,66,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'while_statement':([0,1,45,46,47,48,49,50,51,52,60,62,65,66,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'write_statement':([0,1,45,46,47,48,49,50,51,52,60,62,65,66,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'assignment_statement':([0,1,45,46,47,48,49,50,51,52,60,62,65,66,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'expression':([12,16,17,18,33,],[19,25,29,29,39,]),'operando_statement':([12,16,17,18,33,],[22,22,27,31,22,]),'condition':([17,18,],[26,30,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement_list","S'",1,None,None,None),
  ('statement_list -> statement_list statement ENTER','statement_list',3,'p_statement_list','malf.py',71),
  ('statement_list -> statement ENTER','statement_list',2,'p_statement_list','malf.py',72),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','malf.py',73),
  ('statement_list -> statement','statement_list',1,'p_statement_list','malf.py',74),
  ('statement -> read_statement','statement',1,'p_statement','malf.py',80),
  ('statement -> if_statement','statement',1,'p_statement','malf.py',81),
  ('statement -> while_statement','statement',1,'p_statement','malf.py',82),
  ('statement -> write_statement','statement',1,'p_statement','malf.py',83),
  ('statement -> assignment_statement','statement',1,'p_statement','malf.py',84),
  ('assignment_statement -> ID EQUALS expression SEMICOLON','assignment_statement',4,'p_assignment_statement','malf.py',89),
  ('read_statement -> read ID SEMICOLON','read_statement',3,'p_read_statement','malf.py',93),
  ('if_statement -> if parentesis_izq condition parentesis_der then ENTER statement_list endif SEMICOLON','if_statement',9,'p_if_statement','malf.py',98),
  ('if_statement -> if parentesis_izq condition parentesis_der then ENTER statement_list else ENTER statement_list endif SEMICOLON','if_statement',12,'p_if_statement','malf.py',99),
  ('if_statement -> if parentesis_izq operando_statement parentesis_der then ENTER statement_list endif SEMICOLON','if_statement',9,'p_if_statement','malf.py',100),
  ('if_statement -> if parentesis_izq operando_statement parentesis_der then ENTER statement_list else ENTER statement_list endif SEMICOLON','if_statement',12,'p_if_statement','malf.py',101),
  ('condition -> BOOL','condition',1,'p_condition','malf.py',106),
  ('while_statement -> while parentesis_izq condition parentesis_der do ENTER statement_list wend SEMICOLON','while_statement',9,'p_while_statement','malf.py',111),
  ('while_statement -> while parentesis_izq operando_statement parentesis_der do ENTER statement_list wend SEMICOLON','while_statement',9,'p_while_statement','malf.py',112),
  ('write_statement -> write expression SEMICOLON','write_statement',3,'p_write_statement','malf.py',117),
  ('expression -> ID','expression',1,'p_expression','malf.py',121),
  ('expression -> NUM','expression',1,'p_expression','malf.py',122),
  ('expression -> operando_statement','expression',1,'p_expression','malf.py',123),
  ('operando_statement -> expression OPERATOR expression','operando_statement',3,'p_operando_statement','malf.py',129),
  ('operando_statement -> expression OPERATOR ID','operando_statement',3,'p_operando_statement','malf.py',130),
]
