# TPC 3: Somador on/off

Autor: Beatriz Ribeiro Terra Almeida (a93210)

## Objetivos do Programa

Os objetivos deste programa, como dados pelo enunciado, são os seguintes:

1. Pretende-se desenvolver um programa que some todas as sequências de dígitos que encontre num texto;

2. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;

3. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;

4. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

## Funcionamento do Programa

Primeiro, vamos entender o que o programa quer dizer com os objetivos acima.

O ponto **1.** é entende-se por si só. Dada uma sequência de números, o objetivo é somar todos os seus dígitos.

Por exemplo:

    1234567890 ==> 1+2+3+4+5+6+7+8+9+0 ==> Soma = 45

Os pontos **2.** e **3.**, significam que entre as sequências de dígitos podem aparecer as palavras **On** ou **Off**, em diversos tipos de mistura de letras maiúsculas ou minúsculas (Tanto **On**, como **on**, como **oN**, etc... são registos válidos para **On**). No contexto deste trabalho, estas palavras funcionam como comandos para sinalizar ao programa quando é que começa a somar os dígitos (**On**) e quando para (**Off**).

Isto significa que num ficheiro, vamos ter várias sequências de dígitos interrompidas por variantes de **On** ou **Off**.

    1234On5678ofF90 ==> 12345 On 5+6+7+8 Off 90 ==> Soma = 26

O ponto final (**4.**), indica quando a soma tem de ser enviada para o standard output, que no meu caso, em específico, será o terminal do Ubuntu.

Isto quer dizer que apenas podemos imprimir o resultado da soma quando o programa identifica um **'='**. Por exemplo:
    
    12on34off567on8ofF90= ==>12 on 3+4 off 567 on +8 off 90 = ==> Soma = 3+4+8 = 15

Assim, mesmo que o programa não esteja a atualmente a somar (off90=), ele tem de esperar pelo **'='** para poder imprimir o resultado.

Até agora temos feito a demonstração prática destes elementos do programa apenas com uma linha de exemplo, mas o programa não é obrigado a terminar a sua execução mal chegue ao primeiro **'='**, isto quer dizer que um ficheiro de input como:

        12on34off567on8ofF90=On923847OFF8798=oFf9877987897on889off=

Também é válido e a sua execução só termina quando chegar ao fim do ficheiro.

Por fim, a última coisa que temos de ter em consideração é que, para o caso do exemplo acima, onde existem mais do que um **'='** as somas não são cumulativas. Ou seja, quando uma soma é impressa para o terminal, o total volta a 0 e continua-se a partir daí.

Como um último exemplo da funcionação normal do programa, vamos ver qual seria o resultado do exemplo anterior:

    12on34off567on8ofF90=On923847OFF8798=oFf9877987897on889off= ==>
    12 on 3+4 off 567 on +8 ofF 90 = On 9+2+3+8+4+7 OFF 8798 = oFf 9877987897 on 8+8+9 = ==>
    3+4+8 = | 9+2+3+8+4+7 = | 8+8+9 = ==>
    Soma = 15 | Soma = 33 | Soma = 25

Nota: no caso de haver um input como **(...)12off3=880989808=** o programa vai imprimir **'Soma = 0'** aquando do segundo **'='**, uma vez que a funcionalidade foi desativada na sequencia anterior. 

## Desenvolvimento do Programa

Para implementar as funcionalidades desejadas, foi necessário desenvolver as seguintes expressões regulares:

1. '(.*?)=' : para isolar todas as sequências que, potencialmente, terão de ser somadas. Isto permite terminar a execução do programa sem ter de processar o ficheiro todo, caso haja digitos após o último **'='**;

2. '(\d+|\D+)' : utilizada para separar os 2 tipos de dados que podemos ter sentro das sequências anteriores, sequências de dígitos (\d+) ou comandos de controlo da soma (\D+).

Os grupos derivados da expressão **2.** são posteriormente processados utilizando funções do python de modo a obter os resultados desejados.

## Como utilizar

O programa pode ser corrido utilizando o comando:

     python3 program.py < numbers.txt

Onde numbers.txt é o ficheiro de input com os dígitos a somar.