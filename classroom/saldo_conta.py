# def ordena_fatia(valor_saldo, index): # implementacao do bouble sort para ordenação
#     lista = [int(i) for i in valor_saldo] # transforma a string em lista
#     valor_ordenado = ''
    
#     for i in range(len(lista)):
#         for j in range(len(lista)):
#             if lista[i] < lista[j]: #se o elemento N for menor que o N+1, eles trocam de posicao
#                 lista[i], lista[j] = lista[j], lista[i]

#     for i in lista:
#         valor_ordenado += str(i)

#     return valor_ordenado[index:]

# while True:
#     saldo_info = [int(i) for i in input().split()]
#     if saldo_info == []:
#         break

#     valor_saldo = str(input())
#     saldo_ordenado_fatiado = ordena_fatia(valor_saldo, saldo_info[1])
#     saldo_real = ''

#     for i in valor_saldo:   # Verifica se o elementos do valor do saldo digitado está na lista dos maiores valores
#         for j in saldo_ordenado_fatiado:
#             if i == j:      # Se estiver, ele adiciona na string e printa
#                 saldo_real += i

#     print(saldo_real)
def maior(lista, inicio, fim):
    maior_idx = inicio
    maior = lista[maior_idx]

    for i in range(inicio + 1, fim):
        if lista[i] > maior:
            maior = lista[i]
            maior_idx = i
    return maior_idx

def main():
    n_digitos, n_removidos = [int(i) for i in input().split()]
    lista = [int(i) for i in input().split()]
    n_saldo = n_digitos - n_removidos
    tamanho = len(lista)
    inicio = 0

    for i in range(n_saldo):
        fim = tamanho - (n_saldo - i) + 1
        maior_idx = maior(lista, inicio, fim)
        inicio = maior_idx + 1
        print(lista[maior_idx], end='')

main()
