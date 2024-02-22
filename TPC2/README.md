# TPC 2: Conversor de MD para HTML
---------------------------------------------
Autor: Beatriz Ribeiro Terra Almeida (a93210)

O procedimento deste tpc baseou-se em criar um regex que consegui-se capturar cada elemento especificado pelo enunciado (bols, itálico, listas, headings, imagens e links).

Para isso foi utilizado o regex101.com para facilitar a escrita do regex.

## Problemas com o código

O código atual encontra-se incompleto, sendo que durante o seu desenvolvimento, não foi possível usar a função re.sub(), por motivos que ainda não desvendei.

Devido a isso, o código teve de ser escrito de uma maneira não apropriada.

Outros problemas devem-se ao fator de haver partes do código que apenas funcionam segundo algumas circunstâncias e outras que simplesmente não funcionam (como é o caso de converter os links para html), estas são:

- nos cabeçalhos o regex só funciona se a linha começar com pelo menos 1 '#', sendo que não é capturado se não for seguido de um espaço em branco.

- a substituição dos bold e itálico não está a acontecer como seria esperado, sendo que por agora apenas um deles é registado. O itálico parece ter prioridade neste processo.

- as listas não suportam nesting e o identificador de lista ('1. ' ou '-') têm de estar no início para serem reconhecidos.

- há '<\ul>' extras a serem acrescentados dentro de listas quer sejam estas ordenadas ou não. 

- como mencionado acima, os links não funcionam.

## Como correr o programa

De momento o programa pode ser corrido utilizando o comando:

    python3 program.py < test.txt

Onde test.txt é o ficheiro a ser testado.

Os resultados estão a ser imprimidos para o std.out (ou seja, para o terminal). Não existem opções para guardar o ficheiro resultante num ficheiro separado.



