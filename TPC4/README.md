# TPC4: Analisador Léxico

Autor: Beatriz Ribeiro Terra Almeida (a93210)

## Objectivos do Programa

Para este programa o único objetivo foi desenvolver um analisador léxico para uma linguagem de query semelhante ao SQL, mas simplificado.

Um dos exemplos que nos foi dado, para melhor visualizar esta linguagem hipotética foi:
    
    Select id, nome, salario From empregados Where salario >= 820

## Desenvolvimento do Programa

Pela secção anterior podemos ver que a linguagem que queríamos está dividida em vários tipos de objetos como nomes de colunas/tabelas, palavras chave como 'select','from' e 'where' e vários tipos de dados como int.

Primeiro foram identificados os diferentes tipos que queríamos implementar, usando linguagens como o SQL como inspiração para quaisquer adições:

-  **KEYWORDS**: palavras como 'select', 'from', 'where' e ,embora não estejam incluídas no exemplo, 'and','or','not';

- **Nomes de Variáveis**: nomes de colunas, como 'salario', 'id', etc... ou nomes de tabelas como 'empregados';

- **Operadores**: inclui ==, >=, <, >, etc...;

- **Tipos de dados**: os únicos tipos de dados incluídos são **FLOAT** e **INT**;

- **Caracteres especiais**: isto inclui ',' como separadores no caso de enumerar várias colunas para selecionar, '*' para selecionar todas as colunas de uma tabela e ';' para indicar que a linha terminou;

- **Caracteres a ingorar**: inclui espaços e *tabs*.

Após esta análise do problema, foi preenchido um template que nos foi dado pelos professores de modo a adaptar para o problema.


## Como Utilizar

Para utilizar o programa basta corrê-lo com o seguinte comando:

    python3 lexer.py < ficheiro_com_strings.txt

Neste caso, este **ficheiro_com_strings** seria o ficheiro **test.txt**, que está no repositório como um exemplo.
