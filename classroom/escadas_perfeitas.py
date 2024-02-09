def calculaDegrau(N, pilha_blocos):
    soma = sum(pilha_blocos)
    ultimo_termo_pa = (((2 * soma) // N) + (N - 1)) // 2
    primeiro_termo_pa = 1 + ultimo_termo_pa - N

    movimentos = 0

    for i in range(N):
        """Subtraindo o índice + primeiro termo do PA, sabemos quantos blocos deveriam estar na coluna. Soma nos movimentos"""
        movimentos += (pilha_blocos[i] - (i + primeiro_termo_pa))
        
        """Se o bloco atual estiver mais alto que o esperado, somamos o excesso de blocos."""
        if pilha_blocos[i] > i + primeiro_termo_pa:
            movimentos += (pilha_blocos[i] - (i + primeiro_termo_pa))

    if movimentos != 0:
        return("-1")
    else:
     return movimentos
    
n = int(input())
pilha = list(map(int, input().split()))
resultado = print(calculaDegrau(n, pilha))

