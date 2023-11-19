def fatorial(n):
    valor = 1
    for i in range(1, n+1):
        valor *= i
    return valor

print(fatorial(4))