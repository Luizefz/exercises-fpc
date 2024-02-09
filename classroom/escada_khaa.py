def calcDegrau(N, pilha):
    soma = 0
    for i in range(N):
        soma += pilha[i]

    mudar = 0
    movimentos = 0
    somatorio = (((2 * soma) // N) + (N - 1)) // 2
    pos = 1 + somatorio - N

    for i in range(N):
        mudar += (pilha[i] - (i + pos))
        if pilha[i] > i + pos:
            movimentos += (pilha[i] - (i + pos))

    if mudar != 0:
        return -1
    else:
        return movimentos

N = int(input())
pilha = list(map(int, input().split()))
resultado = calcDegrau(N, pilha)
print(resultado)
