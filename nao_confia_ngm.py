mtz_dimensaoes_campo = [int(i) for i in input().split()]
mtz_campo_batalha = [input() for i in range(mtz_dimensaoes_campo[0])]

qtd_navios = 1
posicoes_navio = {}

for i in range(mtz_dimensaoes_campo[0]):
    for j in range(mtz_dimensaoes_campo[1]):
        if mtz_campo_batalha[i][j] == "#":
            posicoes_navio[qtd_navios] = [i,j]
            qtd_navios += 1

key_list = posicoes_navio.keys()

for i in key_list:
    for j in key_list:
        navio_01 = posicoes_navio[i]
        navio_02 = posicoes_navio[j]
        
        if i == j:
            continue

        # Por algum motivo ele está colocando em todas as casas do dicionario os valores de pouquinho e pouquinho, resolve aí eu do amanhã
        elif navio_01[0] == navio_02[0] and abs(navio_01[1] - navio_02[1]) == 1:
            posicoes_navio[i] = posicoes_navio[i] + (navio_02)

        elif abs(navio_01[0] - navio_02[0]) == 1 and navio_01[1] == navio_02[1]:
            posicoes_navio[i] =  posicoes_navio[i] + (navio_02)


print(posicoes_navio)