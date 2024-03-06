class Fila:
    class No:
        def __init__(self, valor = None, proximo = None):
            self.valor = valor
            self.proximo = proximo

    def __init__(self):
        self.primeiro_no = None
        self.ultimo_no = None

    def inserir(self, valor_no):
        novo_no = self.No(valor_no)

        #Se não tiver itens na Fila, adiciona No início
        if self.primeiro_no == None:
            self.primeiro_no = novo_no
            self.ultimo_no = novo_no
            return
        
        #Se já tiver itens na fila, referencia o novo No
        #no próximo do ultimo elemento
        self.ultimo_no.proximo = novo_no
        
        #Troca o ultimo elemento pelo novo No
        self.ultimo_no = novo_no
    
    def remover(self):
        #FIFO - Primeiro No sai da fila
        if self.primeiro_no == None:
            self.ultimo_no = None
            return 0
        
        antigo_primeiro_no = self.primeiro_no.valor
        #Primeiro No agora é o sucessor do antigo primeiro
        self.primeiro_no = self.primeiro_no.proximo
        return antigo_primeiro_no
    
    def primeiro(self):
        if self.primeiro_no != None:
            return self.primeiro_no.valor
        return 0
    
    def isVazia(self):
        if self.primeiro_no == None and self.ultimo_no == None:
            return True
        return False


pessoas_frente = Fila()
vezes_impimir = {}

T = int(input())
N = int(input())

for i in range(T):
    A = Fila()
    P = Fila()
    vezes_impimir[i] = 0
    for _ in range(N):
        valor = input().split()
        if valor[0] == 'f':
            A.inserir(valor[1])
        
        elif valor[0] == 'p':
            P.inserir(valor[1])
        
        elif valor[0] == 'A':
            if A.isVazia():
                P.remover()
                continue
            else: A.remover()
        
        elif valor[0] == 'B':
            if P.isVazia():
                A.remover()
                continue
            else: P.remover()
        
        elif valor[0] == 'I':
            vezes_impimir[i] += 1
            pessoas_frente.inserir(f'{A.primeiro()} {P.primeiro()}')
    
    if i+1 < T:
        N = int(input())


for y in range(T):
    quantidade_imprimir = vezes_impimir[y]
    print(f"Caso {y+1}")
    for _ in range(quantidade_imprimir):
        print(pessoas_frente.remover())
        
