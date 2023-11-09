def pessoa_restante(lista_pessoas, passos):
    qtd_pessoas = len(lista_pessoas)
    remove_index = 0
    
    while qtd_pessoas > 1:
        remove_index = (passos + remove_index - 1) % qtd_pessoas  # NÂO eh o valor que será removido, é o index.
        lista_pessoas.pop(remove_index)                           # Passo acumulativo, pega a quantidade que já andou, soma com a quantidade do prox passo e
        qtd_pessoas -= 1                                          # Subtrai 1 pois a lista começa no index 0
        print(lista_pessoas)
        print(remove_index)
    return lista_pessoas[0]


def cria_lista_pessoas(qtd_pessoas):
    lista = []
    for i in range(1, qtd_pessoas + 1):
        lista.append(i)
    return lista


num_testes = int(input())
pessoas_passos = [[int(i) for i in input().split()] for i in range(num_testes)]

for i in pessoas_passos:
    lista_pessoas = cria_lista_pessoas(i[0])
    resultado = pessoa_restante(lista_pessoas, i[1])
    print(f"Case {pessoas_passos.index(i) + 1}: {resultado}")
