class Pilha:
    class No:
        def __init__(self, valor = None, proximo_no = None, anterior_no = None):
            self.valor = valor
            self.proximo_no = proximo_no
            self.anterior_no = anterior_no

    def __init__(self):
        self.topo = None

    def isVazia(self):
        return self.topo is None

    def empilhar(self, valor):
        novo_no = self.No(valor)
        if self.isVazia():
            self.topo = novo_no
            return
        
        novo_no.anterior_no = self.topo
        self.topo = novo_no
    
    def desempilhar(self):
        if self.isVazia():
            return
        valor_topo = self.topo.valor
        self.topo = self.topo.anterior_no
        return valor_topo

    def elemento_topo(self):
        if self.isVazia():
            return None
        return self.topo.valor

def isSeuPar(topo, fechamento):
    if fechamento == ')' and topo == '(':
        return True
    if fechamento == ']' and topo == '[':
        return True
    if fechamento == '}' and topo == '{':
        return True
    return False

M = int(input())

resultados = []

for _ in range(M):
    n = input()
    pilha = Pilha()
    for i in n:
        if i in ')]}':
            if isSeuPar(pilha.elemento_topo(), i) and not pilha.isVazia():
                pilha.desempilhar()  
            else:
                pilha.empilhar(i)
        else:
            pilha.empilhar(i) 
    resultados.append('S' if pilha.isVazia() else 'N')

for k in resultados:
    print(k)

