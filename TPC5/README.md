# TPC5 - Máquina de Vending
---------------------------------------------
Autor: Beatriz Ribeiro Terra Almeida (a93210)

## Objetivos do Programa

O principal objetivo deste programa é simular a funcionalidade de uma máquina de vendas automáticas (*vending machine*).

Para ser possível manter o estado da máquina entre sessões deve ser utilizado um ficheiro json com o a lista dos items em stock (isto inclui items que possam estar atualmente fora de stock, mas que já estiveram, a qualquer altura a ser vendidos).

A interação com a máquina será efetuada através da linha de comando usando comandos pré-definidos, listados a seguir:

- **LISTAR**: lista todos os items em stock;
- **SAIR**: termina a execução do programa;
- **MOEDA**: acrescenta moedas ao saldo. As moedas aceites são: 1c, 2c, 5c, 10c, 20c, 50c, 1e e 2e. Cada Moeda tem de ser separada por ','. Para terminar a inserção das moedas acrescentar '.' no final.
- **SELECIONAR**: seleciona o item desejado;
- **ADICIONAR (Não implementado)**: adiciona um novo item ao stock;
- **ALTERAR (Não implementado)**: altera o valor do item selecionado para o desejado;
- **HELP**: lista os comandos disponíveis.


## Desenvolvimento do Programa

Primeiramente, foram devididas as tarefas de acordo com o enunciado. Isto implica que as tarefas foram:

- **Tratar do ficheiro json (hard-coded)**: inclui ler e guardar o estado aquando do término da sessão. O ficheiro em questão é o **stock.json**, disponibilizado no repositório;

- **Criar o Lexer**: para poder para fazer o *parsing* dos comandos de interação com a máquina. Isto inclui definir os comandos que terão de ser implementados (ver secção anterior) e tipos de dados como INT, FLOAT, ITEM_CODE, etc...

- **Implementar a lógica do programa**: implementar as funcionalidades, assim como a resolução de conflitos (*error handling*) e a parte interativa do programa.

Para fazer as operações sob o ficheiro **json** e de forma a facilitar a implementação desta funcionalidade, foi utilizada a biblioteca json nativa ao python. Foram também utilizadas as bibliotecas **ply.lex** (para construir o lexer), **re** (para escrever as expressões regulares necessárias) e **sys** (para ser possível retirar o input do utilizador da linha de comando).

Houve funcionalidades que embora planeadas (como os comandos de adicionar e alterar o stock) não foram implementadas por falta de tempo e capacidade.


## Problemas com o código

De momento o programa tem uma falha fatal, que penso ser nas conversões dos tokens de *strings* para *floats* ou *ints* e vice-versa, que faz com que o saldo que deveria ser um número até 2 casas decimais esteja a ser exibido com o máximo de casas possíveis o que causa erros quando é preciso atualizar os valores dos saldos.

Até agora só sei de duas situações onde isto acontece:

- Quando usamos o comando **MOEDA** para adicionar ao saldo, por exemplo se correr o comando **MOEDA 1e 2e 5c 5c** isto devolve o valor de **3.0999999999999996** em vez do esperado **3.10**.

- Quando escolhemos sair do programa e o troco é calculado.

Este problema não foi resolvido até à data.

## Como Utilizar o Programa

Para utilizar o programa basta correr o comando:

        python3 program.py

A partir daí caso haja dúvidas de como sair do programa ou de quais comandos estão disponíveis, basta escrever **HELP** no input para aparecer a lista de comandos disponíveis.