def maior_lucro(t,c,v):
    divisao = t // c
    valor = divisao * v
    return valor

n,t = map(int, input().split())
solicitacoes = [[int(i) for i in input().split()] for _ in range(n)]

maior_valor = 0
for i in solicitacoes:
    valor = maior_lucro(t,i[0],i[1])
    if valor >= maior_valor:
        maior_valor = valor

print(maior_valor)