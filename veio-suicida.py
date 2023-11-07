def pessoa_restante(lista_pessoas, passos):
    lista = lista_pessoas
    valor_retirar = len(lista) % passos

    if len(lista) == 1:
        return print(lista[0])

    if valor_retirar >= 1:
        if len(lista) == passos + 1:
            lista.pop(0)
            print(lista)
        lista.pop(valor_retirar)
        print(lista)


    elif valor_retirar == 0:
        lista.pop(passos)
        print(lista)


    return pessoa_restante(lista, passos)

def cria_lista_pessoas(qtd_pessoas):
    lista = []
    for i in range(1, qtd_pessoas + 1):
        lista.append(i)
    return lista

num_testes = int(input())
pessoas_passos = [[int(i) for i in input().split()] for i in range(num_testes)]

for i in pessoas_passos:
    lista_pessoas = cria_lista_pessoas(i[0])
    pessoa_restante(lista_pessoas, i[1])