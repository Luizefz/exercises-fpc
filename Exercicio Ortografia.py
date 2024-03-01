# def calcula_distancia(A, B):
#     m, n = len(A), len(B)
#     dp = [[0] * (n + 1) for _ in range(m + 1)]

#     for i in range(m + 1):
#         for j in range(n + 1):
#             if i == 0:
#                 dp[i][j] = j
#             elif j == 0:
#                 dp[i][j] = i
#             elif A[i - 1] == B[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = 1 + min(dp[i - 1][j],       # Remoção
#                                   dp[i][j - 1],       # Inserção
#                                   dp[i - 1][j - 1])   # Substituição

#     return dp[m][n]

# def busca_palavras(dicionario, palavra_usuario):
#     palavras_referidas = []

#     for palavra_dict in dicionario:
#         distancia = calcula_distancia(palavra_usuario, palavra_dict)
#         if distancia <= 2:
#             palavras_referidas.append(palavra_dict)

#     return palavras_referidas

# def main():
#     # Leitura da entrada
#     N, M = map(int, input().split())
#     dicionario = [input().strip() for _ in range(N)]
#     palavras_usuario = [input().strip() for _ in range(M)]

#     # Processamento e saída
#     for palavra_usuario in palavras_usuario:
#         palavras_referidas = busca_palavras(dicionario, palavra_usuario)
#         if palavras_referidas:
#             print(" ".join(palavras_referidas))
#         else:
#             print()

# if __name__ == "__main__":
#     main()

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None

    def esta_vazia(self):
        return self.topo is None

    def empilhar(self, item):
        novo_no = No(item)
        novo_no.proximo = self.topo
        self.topo = novo_no

    def desempilhar(self):
        if not self.esta_vazia():
            item_removido = self.topo.valor
            self.topo = self.topo.proximo
            return item_removido
        else:
            return None

    def topo(self):
        if not self.esta_vazia():
            return self.topo.valor
        else:
            return None

def distancia_palavras(palavra1, palavra2):
    return sum(1 for c1, c2 in zip(palavra1, palavra2) if c1 != c2)

def buscar_palavras(palavra, dicionario):
    return [palavra_dicio for palavra_dicio in dicionario if distancia_palavras(palavra, palavra_dicio) <= 2]

# Leitura da entrada
N, M = map(int, input().split())
dicionario = [input() for _ in range(N)]
palavras_usuario = [input() for _ in range(M)]

# Processamento
for palavra in palavras_usuario:
    palavras_corrigidas = buscar_palavras(palavra, dicionario)
    print(" ".join(palavras_corrigidas))
