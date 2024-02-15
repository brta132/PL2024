import sys
from collections import Counter


def parse_csv(column_list, file_path):

    f_csv =  open(file_path,'rt')

    #read first line to get dic keys
    res_column_data_list = {}

    lines = f_csv.readlines()
    is_first_line = True
    header = []

    for line in lines:
        line_splt = line.split(',')
        line_splt[-1] = line_splt[-1].rstrip('\n')
        if is_first_line:
            header = line_splt
            for n in column_list:
                res_column_data_list[line_splt[n]] = []
            is_first_line = False

        else:
            for n in column_list:
                elem = line_splt[n]
                res_column_data_list[header[n]].append(elem)
    
    #close file
    f_csv.close()
    return res_column_data_list

def modalidades_list_sorted(list_data):
    mod_list = list(set(list_data))
    mod_list = sorted(mod_list,key=str.casefold)
    return mod_list
   
#devolve a percentagem de atletas aptos
def results_aptitude_percentage(list_data):
    count = Counter(list_data)
    total = len(list_data)
    true_percent = (count.get('true')/total)*100
    return true_percent

#devolve um dicionário (intervalo, soma)
def intervals_count(interval,list_data):
    min_n = int(min(list_data))
    max_n = int(max(list_data))

    start_idade_interval = min_n - min_n%interval
    end_idade_interval = max_n - max_n%interval
    current_interval = start_idade_interval

    count = Counter(list_data)

    interval_dict = {}
    while current_interval <= end_idade_interval:

        interval_str = f'[{current_interval}-{current_interval+interval-1}]'
        
        sum = 0
        for i in range(interval):
            add = count.get(f'{current_interval+i}')
            if(add != None):
                sum = sum + add

        interval_dict[interval_str] = sum
        current_interval = current_interval + interval
    
    return interval_dict



def main():
    column_list = [5,8,12]
    res_column_data = parse_csv(column_list,'emd.csv')
    
    #Treat data
    modalidades_list = modalidades_list_sorted(res_column_data['modalidade'])
    aptitude_percentage = results_aptitude_percentage(res_column_data['resultado'])
    intervals_list = intervals_count(5,res_column_data['idade'])
    
    #Print everything to the screen
    print('\nLista ordenada alfabeticamente das modalidades desportivas:\n')
    print(f'    {modalidades_list}')

    print('\n')
    print('Percentagens de atletas aptos e inaptos para a prática desportiva:')
    print(f'    Inaptos (%):{(100 - aptitude_percentage)}\n    Aptos (%):{aptitude_percentage}')
          

    print('\n')
    print('Distribuição de atletas por escalão etário:')
    for key in intervals_list.keys():
        print(f'    {key}: {intervals_list.get(key)}')



if __name__ == "__main__":
    main()
