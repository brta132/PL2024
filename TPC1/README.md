# TPC1 - Análise do Dataset de Exames Médicos Desportivos
Autor: Beatriz Ribeiro Terra Almeida (a93210)

<br/>

## Objectivos:

Ler o dataset, processá-lo e criar os seguintes resultados:

- Lista ordenada alfabeticamente das modalidades desportivas;
- Percentagens de atletas aptos e inaptos para a prática desportiva;
- Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...

<br/>

## Desenvolvimento:

Previamente a começar o desenvolvimento do programa, foi necessário analisar o ficheiro *'emd.csv'* fornecido, de modo a fazer um planeamento mental do que iria ter de ser desenvolvido (quais as colunas relevantes, funções que iriam ser precisas, etc...).
Daqui foi retirado que apenas eram precisos os valores contidos nas colunas 5 (idade), 8(modalidade) e 12(resultados). Daí o *parsing* do ficheiro limitar-se a extrair estas colunas, em específico, e não o ficheiro por inteiro.


Devido a um mal entendimento sobre os métodos que estávamos autorizados a utilizar na solução final, acabaram por ser desenvolvidos dois programas (*program_v1.py* e *program_v2.py*), sendo que a maior diferença entre estes é o método utilizado para efetuar o *parsing* do ficheiro .csv. No *program_v1* isto é feito através de uma expressão regular:

     '(?:.*?,){5}(.*?),(?:.*?,){2}(.*?),(?:.*?,){3}(.*?)\n'

Enquanto que no *program_v2* isto é feito utilizando a função .split(',') para separar as linhas.

Notam-se ainda algumas alterações entre os dois programas devido à experiência ganha na realização do primeiro, que provou ser bastante útil no desenvolvimento do segundo.

Para todos os efeitos de avaliação, o trabalho final a ser considerado é o *program_v2*.

<br/>

## Utilização do Programa:

Atualmente apenas é necessário correr o programa com o comando:
    
     python3 program_v2.py