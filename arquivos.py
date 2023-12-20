def cal_paste(file_data):
    size_list = files_data[1]
    folder_capacity = files_data[0][1]
    folder_amount = 0

    for file_size in size_list:
        if file_size < folder_capacity: # Se o tamanho do item for menor que a capacidade da pasta,
            for j in size_list:         # ele procura um outro item que somado a ele também caiba na pasta.
                if file_size + j <= folder_capacity:
                    size_list.remove(j) # Achando esse item, ele o remove da lista e soma 1 ao contador de pastas.
                    break
            folder_amount += 1
        else:
            folder_amount += 1          # Se o item for do tamanho da capacidade maxima, soma 1 ao contador de pastas e o remove da lista
            size_list.remove(file_size)
    
    print(folder_amount)

files_data = [[int(i) for i in input().split()] for i in range(2)]
cal_paste(files_data)