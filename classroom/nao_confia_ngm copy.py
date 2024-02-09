matrix_dimensoes = [int(i) for i in input().split()]
matrix_campo_batalha = [input() for _ in range(matrix_dimensoes[0])]
qtd_tiros = int(input())
tiros = [[int(i) for i in input().split()] for _ in range(qtd_tiros)]

qtd_navios = 1
posicoes_navio = {}

navios_concatenados = {}
navios_afundados = 0

# Identificação dos navios
for y in range(matrix_dimensoes[0]):
    for x in range(matrix_dimensoes[1]):
        if matrix_campo_batalha[y][x] == '#':
            posicoes_navio[qtd_navios] = [(y, x)]
            qtd_navios += 1

posicoes_navio_copia = {key: list(value) for key, value in posicoes_navio.items()}
print(posicoes_navio)

# Verificação de adjacência e concatenação
navios_concatenados = set()  # Usaremos um conjunto para evitar duplicatas

for i in posicoes_navio:
    for j in posicoes_navio:
        if i == j or j in navios_concatenados:
            continue
        if posicoes_navio[i][0][0] == posicoes_navio[j][0][0] and abs(posicoes_navio[i][0][1] - posicoes_navio[j][0][1]) == 1:
            posicoes_navio_copia[i].extend(posicoes_navio[j])
            navios_concatenados.add(j)
            print(posicoes_navio_copia[i], posicoes_navio[j])

        if posicoes_navio[i][0][1] == posicoes_navio[j][0][1] and abs(posicoes_navio[i][0][0] - posicoes_navio[j][0][0]) == 1:
            posicoes_navio_copia[i].extend(posicoes_navio[j])
            navios_concatenados.add(j)
            print(posicoes_navio_copia[i], posicoes_navio[j])

# Remover navios concatenados
for i in navios_concatenados:
    del posicoes_navio[i]

print(posicoes_navio)

# Contagem de navios afundados
for tiro in tiros:
    for id_navio, array_posicoes in posicoes_navio.items():
        if (tiro[0]-1, tiro[1]-1) in array_posicoes:
            posicoes_navio[id_navio].remove((tiro[0]-1, tiro[1]-1))

for i in posicoes_navio:
    if len(posicoes_navio[i]) == 0:
        navios_afundados += 1

print(navios_afundados)
