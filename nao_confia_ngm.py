matrix_dimensoes = [int(i) for i in input().split()]
matrix_campo_batalha = [input() for _ in range(matrix_dimensoes[0])]
qtd_tiros = int(input())
tiros = [[int(i) for i in input().split()] for _ in range(qtd_tiros)] 

qtd_navios = 1
posicoes_navio = {}
navio_concatenados = []
navios_afundados = 0
"""
Mapeio dentro de um dicionario todas as posições dos navios presentes na matriz.
"""

for y in range(matrix_dimensoes[0]):    # Cria um dicionario com as posicoes dos navios
    for x in range(matrix_dimensoes[1]):
        if matrix_campo_batalha[y][x] != '.': # Se o elemento não for um '.' adiciona no dicionario a lista com uma tupla no dicionario
            posicoes_navio[qtd_navios] = [(y, x)]
            qtd_navios += 1

id_navio = posicoes_navio.keys()

"""
Percebi que para o navio ser concatenado com o outro, ele precisa estar na mesma linha(vertical ou horizontal) e uma casa a mais do que a outra.
Ou seja, se X == X e abs(Y - Y) == 1 ou vice versa, é um navio concatenado.
"""

for i in id_navio:
    for j in id_navio:
        
        if i == j:
            continue

        elif posicoes_navio[i][0][0] == posicoes_navio[j][0][0] and posicoes_navio[i][0][1] - posicoes_navio[j][0][1] == 1: # Verifica se os navios estao na mesma linha e se estao um do lado do outro
            posicoes_navio[i].extend(posicoes_navio[j])  # Adiciona os navios ques estão juntos em um dicionario
            navio_concatenados.append(j)

        elif posicoes_navio[i][0][1] == posicoes_navio[j][0][1] and posicoes_navio[i][0][0] - posicoes_navio[j][0][0] == 1:
            posicoes_navio[i].extend(posicoes_navio[j])
            navio_concatenados.append(j)

"""
Se a condição der verdadeira e o navio for concatenado, eu adiciono as cordenadas do navio dentro da sua respectiva lista no dicionario.
e retiro nas redundancias deletando o navio que foi concatenado que estava solto na lista geral.
"""

for i in navio_concatenados: # Remove os navios que foram concatenados da lista principal
    del posicoes_navio[i]

print(posicoes_navio)
"""
Verifica se o tiro se encaixa em alguma das posições que estão os navios no dicionario. Se sim, ele retira o navio da lista de concatenação do dicionario.
"""
for i in tiros:
    for id_navio, array_posicoes in posicoes_navio.items():
        if (i[0]-1, i[1]-1) in array_posicoes: # Bypass da matriz, pois a matriz começa em 0 e o jogo em 1
            print("Acertou", id_navio)
            posicoes_navio[id_navio].remove((i[0]-1, i[1]-1))

print(posicoes_navio)

"""
Faz a contagem de quantos navios foram afundados olhando quantas lista de navios não possuem mais elementos.
"""
for i in posicoes_navio: 
    if len(posicoes_navio[i]) == 0:
        navios_afundados +=1

print(navios_afundados)
