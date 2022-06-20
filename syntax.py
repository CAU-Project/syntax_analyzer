from lex import lexical
import argparse
from table import SLR_table, Reduce_table
import time

'''
CODE -> VDECL CODE
CODE -> FDECL CODE
CODE -> CDECL CODE
CODE -> ''
VDECL -> vtype id semi
VDECL -> vtype ASSIGN semi
ASSIGN -> id assign RHS
RHS -> EXPR
RHS -> literal
RHS -> character
RHS -> boolstr
EXPR -> EXPR addsub EXPR
EXPR -> EXPR multdiv EXPR
EXPR -> lparen EXPR rparen
EXPR -> id
EXPR -> num
FDECL -> vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace
ARG -> vtype id MOREARGS
ARG -> '' 
MOREARGS -> comma vtype id MOREARGS 
MOREARGS -> ''
BLOCK -> STMT BLOCK
BLOCK -> ''
STMT -> VDECL
STMT -> ASSIGN semi
STMT -> if lparen COND rparen lbrace BLOCK rbrace ELSE
STMT -> while lparen COND rparen lbrace BLOCK rbrace
COND -> COND comp COND
COND -> boolstr
ELSE -> else lbrace BLOCK rbrace
ELSE -> ''
RETURN -> return RHS semi
CDECL -> class id lbrace ODECL rbrace
ODECL -> VDECL ODECL
ODECL -> FDECL ODECL
ODECL -> ''

'''

def convert_token_name(token_list) -> list:
    convert_token_list = []
    convert_table = {
        'Type' : 'vtype',
        'Integer' : 'num',
        'Char' : 'character',
        'Bool' : 'boolstr',
        'String' : 'literal',
        'Id' : 'id',
        'Assign' : 'assign',
        'Compare' : 'comp',
        'SCOLON' : 'semi',
        'COMMA' : 'comma',
        'LPAREN' : 'lparen',
        'RPAREN' : 'rparen',
        'LBRACE' : 'lbrace',
        'RBRACE' : 'rbrace',
        'LBRAKET' : 'lbraket',
        'RBRAKET' : 'rbraket'
    }
    # 키워드 : if,else,while,return,class  분리
    # Arith : addsub, multdiv 분리


    for token in token_list:
        if(token['token'] in ['Keyword','ArithmeticOperator']):
            if token['lexeme'] == "+":
                convert_token_list.append({'token' : 'addsub','lexeme' : token['lexeme']})
                continue    
            if token['lexeme'] == "-":
                convert_token_list.append({'token' : 'addsub','lexeme' : token['lexeme']})
                continue    
            if token['lexeme'] == "*":
                convert_token_list.append({'token' : 'multdiv','lexeme' : token['lexeme']})
                continue    
            if token['lexeme'] == "/":
                convert_token_list.append({'token' : 'multdiv','lexeme' : token['lexeme']})    
                continue
            if token['lexeme'] == "if":
                convert_token_list.append({'token' : 'if','lexeme' : token['lexeme']})    
                continue
            if token['lexeme'] == "else":
                convert_token_list.append({'token' : 'else','lexeme' : token['lexeme']})    
                continue
            if token['lexeme'] == "while":
                convert_token_list.append({'token' : 'while','lexeme' : token['lexeme']})    
                continue
            if token['lexeme'] == "return":
                convert_token_list.append({'token' : 'return','lexeme' : token['lexeme']})    
                continue
            if token['lexeme'] == "class":
                convert_token_list.append({'token' : 'class','lexeme' : token['lexeme']})    
                continue
        else:
            convert_token_list.append({'token' : convert_table[token['token']],'lexeme' : token['lexeme']})
    
    input_token = []
    for token in convert_token_list:
        input_token.append(token['token'])
    
    input_token.append('$')
    return input_token

def main() -> None:
    print("\033[32m[!] Syntax analyzer for tokenizing simple java code.\n\033[0m")
    parser = argparse.ArgumentParser(description='Lexical Analyzer')
    parser.add_argument('input',
                    metavar='filename',
                    type=str,
                    help='Enter file name')
    parser.add_argument('--debug',help='debug',action='store_true')
    
    args = parser.parse_args()
    filename = 'syntax_code/' + args.input

#    args.input = 'test.txt'    
    debug = args.debug
    with open(filename,"r") as fr:
        text = fr.read()
    
    if debug:
        print("============================= Input Code =============================")
        print(text)
        

    # Store Lexical Anlyzer result
    lexical_token_list = []
    try:
        lexical_token_list = lexical(text)
    except Exception as e:
        print('\033[31m' + str(e) + '\033[0m')
        exit(0)
    
    # syntax analyzer test
    token_list = convert_token_name(lexical_token_list)
    if debug:
        print("=========================== Lexical Analyze ===========================")
        print(token_list)
        

    state_stack = []
    accept_token = []
    state_stack.append(0) 
    token_idx = 0

    if debug:
        print()
        print("=========================== Syntax Analyze ===========================")

    while(True):
        try:
            next_input_symbol = token_list[0]
            current_state = state_stack[-1]         
            next_step = SLR_table[current_state][next_input_symbol]
        
            if(next_step[0] == 's'):
                # shift and goto
                state_stack.append(int(next_step[1:]))
                accept_token.append(token_list.pop(0))
                token_idx+=1
                if debug : print("\033[34m[Stack] :" + str(accept_token) + '\033[0m')

            elif(next_step[0] == 'r'):
                # Reduce 
                # RHS 갯수만큼 스택 pop
                reduce_table_idx = int(next_step[1:])
                reduce_LHS = Reduce_table[reduce_table_idx]['LHS']
                reduce_RHS = Reduce_table[reduce_table_idx]['RHS']
                for i in range(len(reduce_RHS)):
                    state_stack.pop()
                    accept_token.pop()
                if debug : print('\033[33m[Reduce] : ' + str(reduce_RHS) +' -> ' + str(reduce_LHS)+'\033[0m')
                # GOTO(current state,LHS) into the stack
                current_state = int(state_stack[-1])
                next_GOTO = reduce_LHS
                next_step = SLR_table[current_state][next_GOTO]
                
                state_stack.append(int(next_step[1:]))
                accept_token.append(reduce_LHS)
                if debug : print("\033[34m[Stack] :" + str(accept_token) + '\033[0m')        
            
            if(next_step == 'acc'):
                print("success")
                break   

    
#            print('[state_stack] : ' + str(state_stack))
#            print('[next_input_symbol] : ' + str(next_input_symbol))
        except Exception as e:
            print("Error Occur at line number {}\n".format(lexical_token_list[token_idx]['line_num']-1))
            i=0
            with open(filename,"r") as fr:
                for i in range(lexical_token_list[token_idx]['line_num']-1):
                    text = fr.readline()
                    print(str(i+1) +" : " +text,end='')
                text = fr.readline()
                print("\033[31m"+str(i+2) + " : " + text )
            print("current Stack for syntax analyzer : " +  str(accept_token))
            print("next token : "  + str(lexical_token_list[token_idx])+ "\033[0m")            
            exit(0)
    #       debug()





    


if __name__ == "__main__":
    main()