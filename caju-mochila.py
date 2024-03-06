def calcula_quantidade_colheita(matriz_fazenda, L, C, M, N):
    
    # Calcula a matriz de acumulado
    acumulado = [[0] * (C + 1) for _ in range(L + 1)]
    for i in range(1, L + 1):
        for j in range(1, C + 1):
            acumulado[i][j] = acumulado[i - 1][j] + acumulado[i][j - 1] - acumulado[i - 1][j - 1] + matriz_fazenda[i - 1][j - 1]

    max_ponto = 0  # Maxima quantidade na colheita

    # Calcula a quantidade máxima de colheita em uma área de M x N cajueiros
    for i in range(M, L + 1):
        for j in range(N, C + 1):
            ponto = acumulado[i][j] - acumulado[i - M][j] - acumulado[i][j - N] + acumulado[i - M][j - N]
            max_ponto = max(max_ponto, ponto)

    return max_ponto

# Exemplo de uso:
L, C, M, N = map(int, input().split())
matriz_fazenda = [[int(i) for i in input().split()] for _ in range(L)]

quantidade_maxima_colheita = calcula_quantidade_colheita(matriz_fazenda, L, C, M, N)
print(quantidade_maxima_colheita)

# MAX = 10000

# matriz = [[0] * MAX for _ in range(MAX)]
# acumulado = [[0] * MAX for _ in range(MAX)]

# l, c, n, m = map(int, input().split())


# for i in range(l):
#     matriz[i] = list(map(int, input().split()))

# for i in range(l):
#     for j in range(c):
#         acumulado[i][j] = matriz[i][j]
#         if i > 0:
#             acumulado[i][j] += acumulado[i - 1][j]
#         if j > 0:
#             acumulado[i][j] += acumulado[i][j - 1]
#         if i > 0 and j > 0:
#             acumulado[i][j] -= acumulado[i - 1][j - 1]

# max_ponto = 0

# for i in range(n - 1, l):
#     for j in range(m - 1, c):   
#         ponto = acumulado[i][j] - acumulado[i - n][j] - acumulado[i][j - m] + acumulado[i - n][j - m]
#         if ponto > max_ponto:
#             max_ponto = ponto

# print(max_ponto)