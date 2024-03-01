class No:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None
class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
    def __len__(self):
        return self.tamanho
    def __repr__(self):
        r = ""
        ponteiro = self.topo
        while(ponteiro):
            r = r + str(ponteiro.dado) + "\n"
            ponteiro = ponteiro.proximo
        return r
    def empilhar(self,dado):
        no = No(dado)
        no.proximo = self.topo
        self.topo = no
        self.tamanho = self.tamanho + 1
    def is_empty(self):
        return self.tamanho == 0
    def desempilhar(self):
        if self.tamanho > 0:
            no = self.topo
            self.topo = self.topo.proximo
            self.tamanho = self.tamanho - 1
            return no.dado
        raise IndexError("A pilha está vazia")
    def ver_topo(self):
        if self.tamanho > 0:
            return self.topo.dado
        raise IndexError("A pilha está vazia")
    def __str__(self):
        return self.__repr__()
def expressao_bem_definida(expressao):
    pilha = Pilha()

    for char in expressao:
        if char in "({[":
            pilha.empilhar(char)
        elif char in ")}]":
            if pilha.tamanho == 0:
                return 'N'  # Caractere de fechamento sem correspondente de abertura
            topo = pilha.desempilhar()
            if (char == ')' and topo != '(') or (char == '}' and topo != '{') or (char == ']' and topo != '['):
                return 'N'  # Caracteres de abertura e fechamento não correspondem

    return 'S' if pilha.tamanho == 0 else 'N'  # Se a pilha não estiver vazia, a expressão não está bem definida


# Leitura do número de instâncias
T = int(input())

# Processamento de cada instância
for _ in range(T):
    expressao = input()
    resultado = expressao_bem_definida(expressao)
    print(resultado)