Transition_table = {
    0 : {
         '+' : 1 , 
         '-' : 2, 
         '*' : 3,
         '/' : 4,
         '=' : 5,
         '<' : 6,
         '>' : 7,
         '!' : 8,
         '(' : 9,
         ')' : 10,
         '{' : 11,
         '}' : 12,
         '[' : 13,
         ']' : 14,
         ';' : 15,
         ',' : 16,
         '\t' : 17,
         '\n' : 18,
         ' ' : 19,
         '\'' : 20,
         '\"' : 21,
         '_' : 22,
         '0' : 23,
         'NZDigit' : 24,
         'Letter' : 25,
         'Alphabet' : 36
        },
    1 : {},
    2 : {
        'NZDigit' : 26
    },
    3 : {},
    4 : {},
    5 : {
        '=' : 27,
    },
    6 : {
        '=' : 28,
    },
    7 : {
        '=' : 29,
    },
    8 : {
        '=' : 30
    },
    9 : {},
    10 : {},
    11 : {},
    12 : {},
    13 : {},
    14 : {},
    15 : {},
    16 : {},
    17 : {},
    18 : {},
    19 : {},
    
    20 : {
        '\'' : 34,
        'Alphabet' : 31
    },
    21 : {
        '"' : 33,
        'Alphabet' : 21
    },
    22 : {
        '_' : 22,
        '0' : 22,
        'NZDigit' : 22,
        'Letter' : 22
    },
    23 : {
        '0' : 35,
        'NZDigit' : 35
    },
    24 : {
        '0' : 24,
        'NZDigit' : 24
    },
    25 : {
        '_' : 25,
        '0' : 25,
        'NZDigit' : 25,
        'Letter' : 25
    },
    26 : {
        '0' : 26,
        'NZDigit' : 26
    },
    27 : {},
    28 : {},
    29 : {},
    30 : {},
    31 : {
        '\'' : 32
    },
    32 : {},
    33 : {},
    34 : {},
    35 : {
        '0' : 35,
        'NZDigit' : 35
    },
    36 : {}
}

State_table = [
    None,
    'ArithmeticOperator',  # +
    'ArithmeticOperator',  # -
    'ArithmeticOperator',  # *
    'ArithmeticOperator',  # /
    'Assign',              # =
    'Compare',             # <
    'Compare',             # >
    'ERR',                 # single !
    'LPAREN',              # (
    'RPAREN',              # )
    'LBRACE',              # {
    'RBRACE',              # }
    'LBRAKET',             # [
    'RBRAKET',             # ]
    'SCOLON',              # ;
    'COMMA',               # ,
    'WHITESPACE',          # \t
    'WHITESPACE',          # \n
    'WHITESPACE',          # 0x20
    'ERR',                 # finished with single quote
    'ERR',                 # finished with double quote
    'Id',                  # _(digit|letter|_)*
    'Integer',             # 0
    'Integer',             # [1-9][0-9]*
    'Id',                  # letter(digit|letter|_)*
    'Integer',             # -[1-9][0-9]*
    'Compare',             # ==
    'Compare',             # <=
    'Compare',             # >=
    'Compare',             # !=
    'ERR',                 # Only Single symbol in ''
    'Char',                # 'Alphabet'
    'String',              # "(Alphabet)*"
    'ERR',                 # '' is not allowed.need exactly one symbol in ''
    'ERR',                 # 00,001,0123 is not allowed
    'ERR'                  # Unavailabe Input Character
]

SLR_table = [
    {'vtype' : 's2','VDECL':'G1'},
    {'vtype' : 's6','class' : 's7','$' : 'r3','CODE':'G3','VDECL':'G1','FDECL':'G4','CDECL':'G5'},
    {'id' : 's8','ASSIGN':'G9'},
    {'$' : 'acc'},
    {'vtype' : 's6','class':'s7','$':'r3','CODE':'G10','VDECL':'G1','FDECL':'G4','CDECL':'G5'},
    {'vtype' : 's6','class':'s7','$':'r3','CODE':'G11','VDECL':'G1','FDECL':'G4','CDECL':'G5'},
    {'id':'s12','ASSIGN':'G9'},
    {'id':'s13'},
    {'semi':'s14','assign':'s15'},
    {'semi':'s16'},
    {'$':'r1'}, #10
    {'$':'r2'},
    {'semi':'s14','assign':'s15','lparen':'s17'},
    {'lbrace':'s18'},
    {'vtype':'r4','id':'r4','rbrace':'r4','if':'r4','while':'r4','return':'r4','class':'r4','$':'r4'},
    {'id':'s27','literal':'s21','character':'s22','boolstr':'s23','lparen':'s26','num':'s28','RHS':'G19','EXPR':'G20','TERM':'G24','FACTOR':'G25'},
    {'vtype':'r5','id':'r5','rbrace':'r5','if':'r5','while':'r5','return':'r5','class':'r5','$':'r5'},
    {'vtype':'s30','rparen':'r20','ARG':'G29'},
    {'vtype':'s6','rbrace':'r37','VDECL':'G32','FDECL':'G33','ODECL':'G31'},
    {'semi':'r6'},
    {'semi':'r7','addsub':'s34'}, #20
    {'semi':'r8'},
    {'semi':'r9'},
    {'semi':'r10'},
    {'semi':'r12','addsub':'r12','multdiv':'s35','rparen':'r12'},
    {'semi':'r14','addsub':'r14','multdiv':'r14','rparen':'r14'},
    {'id':'s27','lparen':'s26','num':'s28','EXPR':'G36','TERM':'G24','FACTOR':'G25'},
    {'semi':'r16','addsub':'r16','multdiv':'r16','rparen':'r16'},
    {'semi':'r17','addsub':'r17','multdiv':'r17','rparen':'r17'},
    {'rparen':'s37'},
    {'id':'s38'}, #30
    {'rbrace':'s39'},
    {'vtype':'s6','rbrace':'r37','VDECL':'G32','FDECL':'G33','ODECL':'G40'},
    {'vtype':'s6','rbrace':'r37','VDECL':'G32','FDECL':'G33','ODECL':'G41'},
    {'id':'s27','lparen':'s26','num':'s28','TERM':'G42','FACTOR':'G25'},
    {'id':'s27','lparen':'s26','num':'s28','FACTOR':'G43'},
    {'addsub':'s34','rparen':'s44'},
    {'lbrace':'s45'},
    {'rparen':'r22','comma':'s47','MOREARGS':'G46'},
    {'vtype':'r34','class':'r34','$':'r34'},
    {'rbrace':'r35'}, #40
    {'rbrace':'r36'},
    {'semi':'r11','addsub':'r11','multdiv':'s35','rparen':'r11'},
    {'semi':'r13','addsub':'r13','multdiv':'r13','rparen':'r13'},
    {'semi':'r15','addsub':'r15','multdiv':'r15','rparen':'r15'},
    {'vtype':'s2','id':'s54','rbrace':'r24','if':'s52','while':'s53','return':'r24','VDECL':'G50','ASSIGN':'G51','BLOCK':'G48','STMT':'G49'},
    {'rparen':'r19'},
    {'vtype':'s55'},
    {'return':'s57','RETURN':'G56'},
    {'vtype':'s2','id':'s54','rbrace':'r24','if':'s52','while':'s53','return':'r24','VDECL':'G50','ASSIGN':'G51','BLOCK':'G58','STMT':'G49'},
    {'vtype':'r25','id':'r25','rbrace':'r25','if':'r25','while':'r25','return':'r25'}, # 50
    {'semi':'s59'},
    {'lparen':'s60'},
    {'lparen':'s61'},
    {'assign':'s15'},
    {'id':'s62'},
    {'rbrace':'s63'},
    {'id':'s27','literal':'s21','character':'s22','boolstr':'s23','lparen':'s26','num':'s28','RHS':'G64','EXPR':'G20','TERM':'G24','FACTOR':'G25'},
    {'rbrace':'r23','return':'r23'},
    {'vtype':'r26','id':'r26','rbrace':'r26','if':'r26','while':'r26','return':'r26'},
    {'boolstr':'s66','COND':'G65'}, #60
    {'boolstr':'s66','COND':'G67'},
    {'rparen':'r22','comma':'s47','MOREARGS':'G68'},
    {'vtype':'r18','rbrace':'r18','class':'r18','$':'r18'},
    {'semi':'s69'},
    {'rparen':'s70','comp':'s71'},
    {'rparen':'r30','comp':'r30'},
    {'rparen':'s72','comp':'s71'},
    {'rparen':'r21'},
    {'rbrace':'r33'},
    {'lbrace':'s73'}, #70
    {'boolstr':'s66','COND':'G74'},
    {'lbrace':'s75'},
    {'vtype':'s2','id':'s54','rbrace':'r24','if':'s52','while':'s53','return':'r24','VDECL':'G50','ASSIGN':'G51','BLOCK':'G76','STMT':'G49'},
    {'rparen':'r29','comp':'s71'},
    {'vtype':'s2','id':'s54','rbrace':'r24','if':'s52','while':'s53','return':'r24','VDECL':'G50','ASSIGN':'G51','BLOCK':'G77','STMT':'G49'},
    {'rbrace':'s78'},
    {'rbrace':'s79'},
    {'vtype':'r32','id':'r32','rbrace':'r32','if':'r32','while':'r32','else':'s81','return':'r32','ELSE':'G80'},
    {'vtype':'r28','id':'r28','rbrace':'r28','if':'r28','while':'r28','return':'r28'},
    {'vtype':'r27','id':'r27','rbrace':'r27','if':'r27','while':'r27','return':'r27'}, #80
    {'lbrace':'s82'},
    {'vtype':'s2','id':'s54','rbrace':'r24','if':'s52','while':'s53','return':'r24','VDECL':'G50','ASSIGN':'G51','BLOCK':'G83','STMT':'G49'},
    {'rbrace':'s84'},
    {'vtype':'r31','id':'r31','rbrace':'r31','if':'r31','while':'r31','return':'r31'}    
]

Reduce_table=[
{'LHS' : 'CODE' , 'RHS' : ['VDECL','CODE']},
{'LHS' : 'CODE' , 'RHS' : ['FDECL','CODE']},
{'LHS' : 'CODE' , 'RHS' : ['CDECL','CODE']},
{'LHS' : 'CODE' , 'RHS' : []},
{'LHS' : 'VDECL' , 'RHS' : ['vtype','id','semi']},
{'LHS' : 'VDECL' , 'RHS' : ['vtype','ASSIGN','semi']},
{'LHS' : 'ASSIGN' , 'RHS' : ['id','assign','RHS']},
{'LHS' : 'RHS' , 'RHS' : ['EXPR']},
{'LHS' : 'RHS' , 'RHS' : ['literal']},
{'LHS' : 'RHS' , 'RHS' : ['character']},
{'LHS' : 'RHS' , 'RHS' : ['boolstr']}, # 10
{'LHS' : 'EXPR' , 'RHS' : ['EXPR','addsub','TERM']},
{'LHS' : 'EXPR' , 'RHS' : ['TERM']},
{'LHS' : 'TERM' , 'RHS' : ['TERM','multdiv','FACTOR']},
{'LHS' : 'TERM' , 'RHS' : ['FACTOR']},
{'LHS' : 'FACTOR' , 'RHS' : ['lparen','EXPR','rparen']},
{'LHS' : 'FACTOR' , 'RHS' : ['id']},
{'LHS' : 'FACTOR' , 'RHS' : ['num']},
{'LHS' : 'FDECL' , 'RHS' : ['vtype','id','lparen','ARG','rparen','lbrace','BLOCK','RETURN','rbrace']},
{'LHS' : 'ARG' , 'RHS' : ['vtype','id','MOREARGS']},
{'LHS' : 'ARG' , 'RHS' : []}, # 20
{'LHS' : 'MOREARGS' , 'RHS' : ['comma','vtype','id','MOREARGS']},
{'LHS' : 'MOREARGS' , 'RHS' : []},
{'LHS' : 'BLOCK' , 'RHS' : ['STMT','BLOCK']},
{'LHS' : 'BLOCK' , 'RHS' : []},
{'LHS' : 'STMT' , 'RHS' : ['VDECL']},
{'LHS' : 'STMT' , 'RHS' : ['ASSIGN','semi']},
{'LHS' : 'STMT' , 'RHS' : ['if','lparen','COND','rparen','lbrace','BLOCK','rbrace','ELSE']},
{'LHS' : 'STMT' , 'RHS' : ['while','lparen','COND','rparen','lbrace','BLOCK','rbrace']},
{'LHS' : 'COND' , 'RHS' : ['COND','comp','COND']},
{'LHS' : 'COND' , 'RHS' : ['boolstr']},
{'LHS' : 'ELSE' , 'RHS' : ['else','lbrace','BLOCK','rbrace']},  # 30
{'LHS' : 'ELSE' , 'RHS' : []},
{'LHS' : 'RETURN' , 'RHS' : ['return','RHS','semi']},
{'LHS' : 'CDECL' , 'RHS' : ['class','id','lbrace','ODECL','rbrace']},
{'LHS' : 'ODECL' , 'RHS' : ['VDECL','ODECL']},
{'LHS' : 'ODECL' , 'RHS' : ['FDECL','ODECL']},
{'LHS' : 'ODECL' , 'RHS' : []}
]