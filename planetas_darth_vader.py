class Planeta:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Plano:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

def esta_na_regiao(plano, planeta):
    return plano.A * planeta.x + plano.B * planeta.y + plano.C * planeta.z >= plano.D

def contar_planetas_na_regiao(planos, planetas):
    regiao_contadores = [0] * len(planos)

    for planeta in planetas:
        for i, plano in enumerate(planos):
            if esta_na_regiao(plano, planeta):
                regiao_contadores[i] += 1
                break

    return max(regiao_contadores)

# Leitura da entrada
M, N = map(int, input().split())
planos = [Plano(*map(int, input().split())) for _ in range(M)]
planetas = [Planeta(*map(int, input().split())) for _ in range(N)]

# Processamento
max_planetas_regiao = contar_planetas_na_regiao(planos, planetas)

# Saída
print(max_planetas_regiao)
