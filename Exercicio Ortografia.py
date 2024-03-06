def calcula_distancia(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],       # Remoção
                                  dp[i][j - 1],       # Inserção
                                  dp[i - 1][j - 1])   # Substituição

    return dp[m][n]

def busca_palavras(dicionario, palavra_usuario):
    palavras_referidas = []

    for palavra_dict in dicionario:
        distancia = calcula_distancia(palavra_usuario, palavra_dict)
        if distancia <= 2:
            palavras_referidas.append(palavra_dict)

    return palavras_referidas


N, M = map(int, input().split())
dicionario = [input().strip() for _ in range(N)]
palavras_usuario = [input().strip() for _ in range(M)]

# Processamento e saída
for palavra_usuario in palavras_usuario:
    palavras_referidas = busca_palavras(dicionario, palavra_usuario)
    if palavras_referidas:
        print(" ".join(palavras_referidas))
    else:
        print()