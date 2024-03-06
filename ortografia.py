class Lista:
    class No:
        def __init__(self, valor = None, proximo_no = None, anterior_no = None):
            self.valor = valor
            self.proximo_no = proximo_no
            self.anterior_no = anterior_no

    def __init__(self):
        self.inicio = None
        self.fim = None

    def isVazia(self):
        return self.inicio is None and self.fim is None

    def inserir(self, valor):
        novo_no = self.No(valor)
        if self.isVazia():
            novo_no.anterior_no = None
            novo_no.proximo_no = None
            self.inicio = novo_no
            self.fim = novo_no
            return

        atual_no = self.inicio
        while atual_no.proximo_no != None:
            atual_no = atual_no.proximo_no
        
        atual_no.proximo_no = novo_no
        novo_no.anterior_no = atual_no
        self.fim = novo_no
        return
    
    def remover(self, valor):
        if self.isVazia():
            return
        
        atual_no = self.inicio
        while atual_no.valor != valor:
            atual_no = atual_no.proximo_no

        anterior_no = atual_no.anterior_no
        proximo_no = atual_no.proximo_no

        anterior_no.proximo_no = proximo_no
        proximo_no.anterior_no = anterior_no

        return f'valor {atual_no.valor} removido!'
    
    def iterador(self):
        atual_no = self.inicio
        while atual_no is not None:
            yield atual_no.valor
            atual_no = atual_no.proximo_no

    def imprimir(self):
        atual_no = self.inicio
        while atual_no != None:
            print(atual_no.valor)
            atual_no = atual_no.proximo_no
    

def calcula_distancia(A, B):
    distancia = 0
    # Verifica se cada letra é igual e está na posição da do dicionario
    for letra_palavra_a, letra_palavra_b in zip(A, B):
        if letra_palavra_a != letra_palavra_b:
            distancia += 1
    return distancia

# Leitura da entrada usando a classe Lista
dicionario = Lista()
N, M = map(int, input().split())
for _ in range(N):
    dicionario.inserir(input().strip())

palavras_usuario = Lista()
for _ in range(M):
    palavras_usuario.inserir(input().strip())

# Processamento e saída
atual_no_palavra_usuario = palavras_usuario.inicio
while atual_no_palavra_usuario is not None:
    palavra_usuario = atual_no_palavra_usuario.valor
    palavras_referidas = [palavra for palavra in dicionario.iterador() if calcula_distancia(palavra, palavra_usuario) <= 2]
    if palavras_referidas:
        print(" ".join(palavras_referidas))
    atual_no_palavra_usuario = atual_no_palavra_usuario.proximo_no