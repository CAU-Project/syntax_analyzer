import argparse
import string
from table import *

# Define
Digit = [x for x in string.digits] # [0-9]
NZeroDigit = Digit[1:] # [1-9]
Letter = [x for x in string.ascii_letters] # [a-z,A-Z]
Alphabet = [x for x in string.printable.replace('\'','')]

Type = [
    'int',
    'char',
    'boolean',
    'string'
]

Bool = [
    'true',
    'false'
]


Keyword =[
    'if',
    'else',
    'while',
    'class',
    'return'
]

ERR_STATE = [x for x in range(len(State_table)) if State_table[x] == 'ERR']


# Functions
def state_change(state,ch) -> int:
    if ch == '\0': return -1
    if ch in NZeroDigit : ch = 'NZDigit'
    if ch in Letter : ch = 'Letter'
    ch = str(ch)
    try:
        next_state = Transition_table[state][ch]    # check next_state is exist
    except:
        try:
            next_state = Transition_table[state]['Alphabet']    # check Alphabet is possible
        except:
            return 0    # set next_state = 0
    return next_state

def report_error(state,lexeme,line_num) -> None:
    if(state == 8):
        raise Exception("Line[{}] Wrong value after ! \nLexeme : {} ".format(line_num,lexeme))
    if(state == 20):
        raise Exception("Line[{}] Single quote is not Closed. \nLexeme : {} ".format(line_num,lexeme))
    if(state == 21):
        raise Exception("Line[{}] Double quote is not Closed. \nLexeme : {} ".format(line_num,lexeme))
    if(state == 31):
        raise Exception("Line[{}] Only 1 symbol is permitted in single quote. \nLexeme : {}".format(line_num,lexeme))
    if(state == 34):
        raise Exception("Line[{}] Blank is not permitted in Single quote. \nLexeme : {} ".format(line_num,lexeme))
    if(state == 35):
        raise Exception("Line[{}] Integer Start with 0 is not permitted. \nLexeme : {}".format(line_num,lexeme))
    if(state == 36):
        raise Exception("Line[{}] Invalid Input. \nLexeme : {} ".format(line_num,lexeme))
    

def lexical(text) -> list:
    text = text + '\0'
    i=0
    token_result = []
    line_num = 1
    state = 0
    lexeme = ''

    while True:
        ch = text[i]
        next_state = state_change(state,ch) # state change based on current state, input character

        # next_state == 0 : Search next token
        # next_state == -1 : EOF
        if next_state == 0 or next_state == -1:
            if state in ERR_STATE:
                report_error(state,lexeme,line_num)

            token = State_table[state]

            if token == 'Id':   # if token is 'Id' then check whether it is in Type,Keyword,Bool 
                if lexeme in Type:
                    token = 'Type'
                if lexeme in Keyword:
                    token = 'Keyword'
                if lexeme in Bool:
                    token = 'Bool'
                    
            if token != 'WHITESPACE': # WHITESPACE Token is ommitted in result. i
                token_result.append({'token' : token ,'lexeme' : lexeme})

            if token == 'WHITESPACE' and lexeme == '\n':    # for report error save line_num
                line_num += 1

            state = 0
            lexeme = ''

            if next_state == -1:
                break
        else:
            state = next_state
            lexeme += ch
            i += 1

    return token_result
            


def main() -> None:
    print("\033[32m[!] lexical analyzer for tokenizing simple java code.\n\033[0m")
    parser = argparse.ArgumentParser(description='Lexical Analyzer')
    parser.add_argument('input',
                    metavar='filename',
                    type=str,
                    help='Enter file name')

    args = parser.parse_args()
    filename = 'test_code/' + args.input
    
    text = []
    with open(filename,"r") as fr:
        text = fr.read()
    
    # Store Lexical Anlyzer result
    token_list = []
    try:
        token_list = lexical(text)
    except Exception as e:
        print('\033[31m' + str(e) + '\033[0m')
        exit(0)
    
    output_filename = args.input + '_output.txt'
    print("\033[32m[+] Finish Lexical analyzr")
    print("[+] Save Result in {}\033[0m".format(output_filename))
    

    with open(output_filename,"w") as fw:
        fw.write
        for token in token_list:
            fw.write('%-20s |\t %s\n'%(token['token'],token['lexeme']))

    
if __name__ == "__main__":
    main()