import re,sys
import ply.lex as lex

def main() -> None:
    # List of token names.   This is always required
    tokens = (
       'FLOAT',
       'INT',
       'PUNCTUATION',
       'VAR',
       'ALL_COLS',
       'KEYWORD',
       'OPERATOR',
       'TERMINATOR'
    )


    # Regular expression rules for simple tokens
    t_PUNCTUATION: str = ','
    t_VAR: str = '\w+'
    t_ALL_COLS: str = '\*'
    t_KEYWORD: str = '(select|from|where|and|or|not)'
    t_OPERATOR: str = '(==|>=|<=|<|>)'
    t_TERMINATOR: str = ';'

    Flags = re.IGNORECASE
    
    def t_FLOAT(t):
        r'(\+|\-)?\d+\.\d+'
        t.value = float(t.value)
        return t
    
    def t_INT(t):
        r'(\+|\-)?\d+'
        t.value = int(t.value)
        return t
     
    t_ignore = ' |\t'
    
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)
    
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
    
    
    # Build the lexer
    lexer = lex.lex(reflags=int(Flags))


    
    #data = '	Select * From empregados Where salario == 0;'
    data = sys.stdin.readlines()
    data = ''.join(data)
    
    lexer.input(data)

    for tok in lexer:
        print(tok.type, tok.value)
       
    return

if __name__ == "__main__":
    main()