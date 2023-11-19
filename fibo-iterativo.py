def fib(num):
    a, b = 0, 1 # Pega os dois valores anteriores e soma, depois pega o valor da soma e soma com o valor anterior[...]
    for _ in range(2, num + 1):
        soma = a + b
        a, b = b, soma

    return soma

def chamados(num):
    a, b = 2, 4 # Do mesmo jeito da contagem iterativa do valor do Fibonacci, o valor de chamados da funcao cresce na mesma lógica
    for i in range(3, num): # num == 4, começa a contar do 3
        soma = a + b + 2 # Percebi que o valor de chamados do proximo termo eh (n-1) + (n-2) + 2
        a, b = b, soma
    return b

num_testes = int(input())
fib_valores = [int(input()) for i in range(num_testes)]

for i in fib_valores:
    valor = fib(i)
    chamadas = chamados(i)
    print(f'fib({i}) = {chamadas} calls = {valor}')