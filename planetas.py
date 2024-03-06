M, N = map(int, input().split())
planos = [list(map(int, input().split())) for _ in range(M)]
planetas = [list(map(int, input().split())) for _ in range(N)]

def ponto_dentro_da_regiao(x, y, z, plano):
    A, B, C, D = plano
    return A*x + B*y + C*z <= D

def contar_planetas_em_regioes(planos, planetas):
    contagem_planetas_regioes = [0] * M  
    for planeta in planetas:
        for i, plano in enumerate(planos):
            if ponto_dentro_da_regiao(planeta[0], planeta[1], planeta[2], plano):
                contagem_planetas_regioes[i] += 1
                break
    return max(contagem_planetas_regioes)

print(contar_planetas_em_regioes(planos, planetas))
