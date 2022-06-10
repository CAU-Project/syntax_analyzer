from lex import lexical
import argparse

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
    
    return convert_token_list

def syntax_analyze(token_list) -> bool:
    # 문법을 검사해서 틀리면 false, 맞으면 true로 끝낸다.

def main() -> None:
    print("\033[32m[!] Syntax analyzer for tokenizing simple java code.\n\033[0m")
    parser = argparse.ArgumentParser(description='Lexical Analyzer')
    parser.add_argument('input',
                    metavar='filename',
                    type=str,
                    help='Enter file name')
    
#    args = parser.parse_args()
#    filename = 'test_code/' + args.input

#    args.input = 'test.txt'    
    
    ###
    filename = 'test_code/test.txt'
    ###
    with open(filename,"r") as fr:
        text = fr.read()
    
    # Store Lexical Anlyzer result
    token_list = []
    try:
        token_list = lexical(text)
    except Exception as e:
        print('\033[31m' + str(e) + '\033[0m')
        exit(0)
    


    # lex_output_filename = '[lex] ' + args.input + '_output.txt'
    # print("\033[32m[+] Finish Lexical analyzr")
    # print("[+] Save Result in {}\033[0m".format(lex_output_filename))
    
    # # save lexical analyzer result
    # with open(lex_output_filename,"w") as fw:
    #     fw.write
    #     for token in token_list:
    #         fw.write('%-20s |\t %s\n'%(token['token'],token['lexeme']))

    # syntax analyzer test
    token_list = convert_token_name(token_list)
    print(token_list)

    syntax_analyze(token_list)
    


if __name__ == "__main__":
    main()