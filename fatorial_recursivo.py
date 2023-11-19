def fatorial(n, valor=1):
    
    if (n < 1):
        return valor
    valor *= n
    return fatorial(n-1, valor)

print(fatorial(5))