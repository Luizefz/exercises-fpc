def fib(num):
    global chamadas
    chamadas += 1

    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)

num_testes = int(input())
fib_valores = [int(input()) for i in range(num_testes)]
chamadas = -1

for i in fib_valores:
    valor = fib(i)
    print(f'fib({i}) = {chamadas} calls = {valor}')
    chamadas = -1