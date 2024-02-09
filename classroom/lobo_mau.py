# Função para verificar se um movimento está dentro dos limites da fazenda
def dentro_limites(i, j, R, C):
    return 0 <= i < R and 0 <= j < C

# Função para checar se um campo vazio não pertence a nenhum pasto
def campo_vazio_nao_pertence(i, j, R, C, visited, fazenda):
    # Verifica se um campo vazio não pertence a um pasto se estiver na borda
    if fazenda[i][j] == '.' and (i == 0 or i == R - 1 or j == 0 or j == C - 1):
        return True
    return False

# Função para contar o número de ovelhas e lobos
def contar_animais(R, C, fazenda):
    ovelhas = 0
    lobos = 0

    # Direções possíveis: cima, baixo, esquerda, direita
    direcoes = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Inicialização da matriz para campos visitados
    visitado = [[False for _ in range(C)] for _ in range(R)]

    # Percorre toda a fazenda
    for i in range(R):
        for j in range(C):
            # Se o campo não for uma cerca e não foi visitado ainda
            if fazenda[i][j] != '#' and not visitado[i][j]:
                # Se um campo vazio não pertence a um pasto, marca como visitado
                if campo_vazio_nao_pertence(i, j, R, C, visitado, fazenda):
                    visitado[i][j] = True
                else:
                    ovelha = 0
                    lobo = 0
                    fila = [(i, j)]  # Fila para percorrer o pasto

                    while fila:
                        x, y = fila.pop(0)
                        visitado[x][y] = True

                        # Contagem de ovelhas e lobos
                        if fazenda[x][y] == 'k':
                            ovelha += 1
                        elif fazenda[x][y] == 'v':
                            lobo += 1

                        # Verifica os vizinhos
                        for dx, dy in direcoes:
                            nx, ny = x + dx, y + dy
                            # Verifica se está dentro dos limites e se não é uma cerca nem visitado
                            if dentro_limites(nx, ny, R, C) and fazenda[nx][ny] != '#' and not visitado[nx][ny]:
                                fila.append((nx, ny))
                                visitado[nx][ny] = True

                    # Compara o número de ovelhas e lobos no pasto
                    if ovelha > lobo:
                        ovelhas += ovelha
                    else:
                        lobos += lobo

    return ovelhas, lobos

# Leitura da entrada
R, C = map(int, input().split())
fazenda = []
for _ in range(R):
    fazenda.append(list(input()))

# Chamada da função para contar o número de ovelhas e lobos
num_ovelhas, num_lobos = contar_animais(R, C, fazenda)

# Saída do resultado
print(num_ovelhas, num_lobos)