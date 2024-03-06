def knapsack_max_value(N, C, weights, values):
    # Inicializa a tabela para guardar os valores máximos
    dp = [[0] * (C + 1) for _ in range(N + 1)]

    # Preenche a tabela
    for i in range(1, N + 1):
        for w in range(1, C + 1):
            # Se o peso do item for maior que a capacidade atual da mochila, não é possível pegá-lo
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # Caso contrário, considera-se pegar ou não o item para obter o valor máximo
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    # Retorna o valor máximo obtido
    return dp[N][C]

# Função para leitura da entrada
def read_input():
    N, C = map(int, input().split())
    weights = []
    values = []
    for _ in range(N):
        weight, value = map(int, input().split())
        weights.append(weight)
        values.append(value)
    return N, C, weights, values

# Leitura da entrada
N, C, weights, values = read_input()

# Chamada da função principal e impressão do resultado
print(knapsack_max_value(N, C, weights, values))
