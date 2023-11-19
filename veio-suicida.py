def pessoa_restante(lista_pessoas, passos):
    qtd_pessoas = len(lista_pessoas)
    remove_index = 0
    
    while qtd_pessoas > 1:
        remove_index = (passos + remove_index - 1) % qtd_pessoas
        lista_pessoas.pop(remove_index)
        qtd_pessoas -= 1
        
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