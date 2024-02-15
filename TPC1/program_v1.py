import sys, re
from collections import Counter

#colunas importantes
idade = []
modalidades = []
resultados = []

#abrir ficheiro e ler todo o conteudo
f_csv =  open('emd.csv','rt')
content = f_csv.read()
f_csv.close()

# se houver conteudo
if(content != None):
    #procurar as colunas necessárias (modalidade-> coluna 8, idade -> coluna 5, result -> coluna 12)
    matches = re.findall('(?:.*?,){5}(.*?),(?:.*?,){2}(.*?),(?:.*?,){3}(.*?)\n',content)
    matches.pop(0)
    if(len(matches) > 0):
        for match in matches:
            idade.append(match[0])
            modalidades.append(match[1])
            resultados.append(match[2])
            
    #get lista de modalidades ordenada
    modalidades_list = list(Counter(modalidades).keys())
    modalidades_list.sort(key=str.casefold)
    print(modalidades_list)

    # percentagem de atletas aptos e inaptos
    total_atletas = len(resultados)
    count_true = resultados.count('true')
    count_false = resultados.count('false')
    print(f'Inaptos (%): {(count_false/total_atletas)*100}\nAptos (%): {(count_true/total_atletas)*100}')

    #atletas por escalão etário [0-4]...[95-99]
    inicial = 20 # olhei pro min do csv
    intervalo = 5
    i = 0
    sum = 0

    faixa_etaria = {}

    idade_count = Counter(idade)
    #print(idade_count)
    
    n_element_max = len(idade_count)
    #print(f'n_elem_max: {n_element_max}')
    n_element_counted = 0
    while(n_element_counted <= n_element_max):
        #reset values
        #print(i)
        if(i == intervalo):
            #print(sum)
            faixa_etaria.update({f'[{inicial}-{inicial+intervalo-1}]': sum})
            sum = 0
            i = 0
            inicial = inicial + intervalo

            #Para o caso do ultimo elemento ser o primeiro elemento do intervalo seguinte
            if(n_element_counted == n_element_max):
                n_element_counted = n_element_counted + 1
            

        key = inicial + i
        idade_value = idade_count.get(f'{key}')
        #print(f'id_val: {idade_value}')

        if(idade_value != None):
            #print(f'id_val: {idade_value}')
            sum = sum + idade_value
            n_element_counted = n_element_counted + 1
        
        i = i+1        

    print(faixa_etaria)
        