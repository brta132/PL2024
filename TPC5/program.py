from ply import lex
import json, re, sys
import datetime

def load_json() -> list:
    f = open("stock.json",'r')
    data = []

    if f != None:
        data = json.load(f)

    f.close()
    return data

def save_json(data) -> None:
    f = open("stock.json",'w')
    if(data != [] and data != None):
        json.dump(data,f)
    f.close()

def build_lexer() -> lex.Lexer:

    # List of token names.   This is always required
    tokens = (
       'COMANDO',
       'MOEDA',
       'ITEM_CODE',
       'ITEM_NAME',
       'FLOAT',
       'INT',
       'TERMINATOR'
    )


    # Regular expression rules for simple tokens
    t_COMANDO: str = 'LISTAR|SAIR|MOEDA|SELECIONAR|ADICIONAR|ALTERAR|HELP'

    def t_MOEDA(t: lex.LexToken):
        r'(1c|2c|5c|10c|20c|50c|1e|2e)'
        if(str(t.value).__contains__('c')):
            t.value = float(str(t.value)[:-1])/100
        else:
            t.value = float(str(t.value)[:-1])
        return t
    
    t_ITEM_CODE : str = '[A-Za-z]\d{2}'
    
    t_ITEM_NAME: str = '[0-9a-zA-Z ]+'

    def t_FLOAT(t: lex.LexToken):
        r'(\+|\-)?\d+\.\d+'
        t.value = float(t.value)
        return t
    
    def t_INT(t: lex.LexToken):
        r'(\+|\-)?\d+'
        t.value = int(t.value)
        return t
    
    
    t_TERMINATOR: str = '\.|\n'

    Flags = re.IGNORECASE
       
    t_ignore = ' |\t|,'
    
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
    
    
    # Build the lexer
    lexer = lex.lex(reflags=int(Flags))
    return lexer

def list_stock(stock_data: dict) -> None:
    cabecalho: str = 'cod | nome | quantidade |  preço'
    separator: str = '--------------------------------------------'
    
    print(cabecalho)
    
    for item in stock_data['stock']:
        print(separator)
        codigo = item['cod']
        nome = item['nome']
        quant = item['quant']
        preco = item['preco']
        print(f'{codigo} | {nome} | {quant} | {preco} euros')

    return

def print_help() -> None:
    print('''Available COMANDS:\n
            \tLISTAR: lista todos os items em stock\n
            \t(não implementada) ADICIONAR \{Código do item\} \{Nome do Item\} \{Quantidade\} \{Preço\}: adiciona um novo item ao stock\n
            \t(não implementada) ALTERAR \{Código do item\} \{Nome do parametro\} \{Valor\}: altera o valor do item selecionado para o desejado\n
            \tHELP: lista os comandos disponíveis\n
            \tSAIR: termina a execução do programa\n
            \tMOEDA {moeda 1, moeda 2, ..., moeda n .}: acrescenta moedas ao saldo. As moedas aceites são: 1c, 2c, 5c, 10c, 20c, 50c, 1e e 2e. Cada Moeda tem de ser separada por ','. Para terminar a inserção das moedas acrescentar '.' no final.\n
            \tSELECIONAR \{Código do item\}: seleciona o item desejado.\n
          ''')
    return

def adicionar_stock() -> None:
    print('Funcionalidade não implementada.')
    return

def update_saldo(lexer: lex.Lexer, saldo_atual: float) -> None:
    saldo_final: float = saldo_atual
    for tok in lexer:
        if(tok.type == 'MOEDA'):
            saldo_final += float(tok.value)
        elif (tok.type != 'TERMINATOR'):
            print('Erro: Moeda não reconhecida')
    return saldo_final

def destrocar(saldo: float) -> None:
    lista_moedas = ['2e','1e','50c','20c','10c','5c','2c','1c']
    str_final = ''
    if saldo > 0:
        str_final = 'Pode retirar o troco: '
        for moeda in lista_moedas:
            moeda_valor: float = float(moeda[:-1])
            add_virgula = False

            if moeda.__contains__('c'):
                moeda_valor = moeda_valor / 100
                r: float = saldo // moeda_valor
                if (r > 0):
                    saldo = saldo - r*moeda_valor
                    str_final = ''.join([str_final,f'{r}x {moeda}'])
                    add_virgula = True
            else:
                r: float = saldo // moeda_valor
                if r > 0:
                    saldo = saldo - r*moeda_valor
                    str_final = ''.join([str_final,f'{r}x {moeda}'])
                    add_virgula = True

            if moeda == lista_moedas[len(lista_moedas)-1]:
                str_final = ''.join([str_final,'.'])
                print(str_final)
            elif add_virgula:
                str_final = ''.join([str_final,','])

    return

def selecionar(lexer, saldo: float, stock_data) -> None:
    for tok in lexer:
        if(tok.type == 'ITEM_CODE'):
            for item in stock_data['stock']:
                if item['cod'].casefold() == str(tok.value).casefold():
                    preco: float = float(item['preco'])
                    if(saldo >= preco):
                        qt: int = int(item['quant'])
                        if(qt > 0):
                            item['quant'] = item['quant'] - 1
                            saldo -= preco
                            print('Pode retirar o produto dispensado: ', item['nome'])
                        else:
                            print('O artigo selecionado não se encontra atualmente em stock.')
                    else:
                        print(f'Saldo insuficiente. Saldo atual: {saldo}\nPreço do artigo: {preco}')
    return saldo, stock_data

def add_item() -> None:
    print('Funcionalidade não implementada.')
    return

def update_item() -> None:
    print('Funcionalidade não implementada.')
    return

def main() -> None:
    stock_data = load_json()
    saldo: float = 0.0
    exit = False

    #Building the lexer
    lexer = build_lexer()

    #Print the first lines:
    if stock_data != []:
        date = datetime.datetime.now()
        print(f'{date.year}-{date.month}-{date.day}, Stock carregado, Estado atualizado.')
        print('Bom dia. Estou disponível para atender o seu pedido.')

        while exit == False:
            #Getting the data
            input_data = sys.stdin.readline()

            lexer.input(input_data)

            for tok in lexer:
                tok = str(tok.value).casefold()
                if tok == 'LISTAR'.casefold():
                    list_stock(stock_data)

                elif tok == 'SAIR'.casefold():
                    #tratar do troco
                    destrocar(saldo)
                    print('Até à próxima')
                    save_json(stock_data)
                    exit = True

                elif tok == 'HELP'.casefold():
                    print_help()

                elif tok == 'MOEDA'.casefold():
                    saldo = update_saldo(lexer,saldo)
                    print('Saldo = ', saldo)

                elif tok == 'SELECIONAR'.casefold():
                    saldo, stock_data = selecionar(lexer, saldo, stock_data)
                    print("Saldo = ",saldo)

                elif tok == 'ADICIONAR'.casefold():
                    add_item()

                elif tok == 'ALTERAR'.casefold():
                    update_item()
            
            print('')
    return

if __name__ == '__main__':
    main()