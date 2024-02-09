def G(n): # Adiciona 1 a contagem da lista global
    global count_calls
    count_calls += 1
    return count_calls

def F(n):
    global count_calls
    if n == 1: # Caso base, adiciona G(n) - quantidade de chamados - a lista
        list_range_calls.append(G(n))
        count_calls = 0 # Retorna a contagem para 0
        return 1
    elif n%2 == 0:
        G(n)
        return F(n/2)
    G(n)
    return F(3*n+1)

tests = int(input())
range_limits = [[int(i) for i in input().split()] for i in range(tests)]

list_range_calls = []
count_calls = 0

for index, line in enumerate(range_limits):
    for i in range(line[0], line[1]):
        F(i)
    list_range_calls.sort() # Ordena a lista do menor para o maior
    print(f'Caso {index+1}: {list_range_calls[-1]}') # Mostra o maior numero de chamados recursivos do intervalo
    list_range_calls = []