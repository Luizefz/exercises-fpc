class Fila:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return len(self.items) == 0

    def inserir(self, item):
        self.items.append(item)

    def remover(self):
        if not self.esta_vazia():
            return self.items.pop(0)
        else:
            raise IndexError("A fila está vazia")

    def frente(self):
        if not self.esta_vazia():
            return self.items[0]
        return 0

t = int(input())

for i in range(t):
    n = int(input())
    filaf = Fila()
    filap = Fila()
    caso = []
    for j in range(n):
        a = input().split()
        if 'f' in a:
            filaf.inserir(a[1])
        elif 'p' in a:
            filap.inserir(a[1])
        elif 'A' in a:
            if filaf.esta_vazia():
                filap.remover()
            else : filaf.remover()
        elif 'B' in a:
            if filap.esta_vazia():
                filaf.remover()
            else : filap.remover()
        elif 'I' in a:
            aux = []
            aux.append(filaf.frente())
            aux.append(filap.frente())
            caso.append(aux)

    print(f'Caso {i + 1}:')
    for valor in caso:
        print(' '.join(map(str, valor)))