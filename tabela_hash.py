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

    def imprimir(self):
        atual_no = self.inicio
        while atual_no != None:
            print(atual_no.valor)
            atual_no = atual_no.proximo_no
        return print('--------')
    
    def quantidade_elementos(self):
        atual_no = self.inicio
        contador = 0
        while atual_no != None:
            contador += 1
            atual_no = atual_no.proximo_no
        return contador

class TabelaHash:
    def __init__(self, m):
        self.m = m
        self.T = [None]*m #inicia lista estatica

    def hash(self, chave):
        return chave % self.m

    def inserir(self, chave, dado):
        endereco = self.hash(chave)
        if self.T[endereco] is None:
            self.T[endereco] = Lista()
        self.T[endereco].inserir(dado)

    def __str__(self):
        s = ""
        for i in self.T:
            s += f"{str(i.quantidade_elementos()) if i is not None else 'Vazio'} \n"
        return s

tabela_hash = TabelaHash(4)
dados = [(11, "Khadijra"), (23, "Brasileiro"), (20, "Batima")]
for chave, dado in dados:
    tabela_hash.inserir(chave, dado)
print(tabela_hash)