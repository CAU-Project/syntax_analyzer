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


