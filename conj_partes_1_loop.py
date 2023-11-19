def substring(n, inicio=0):
    if inicio >= len(n):
        return
    for i in range(len(n)+1):
        print(n[inicio:i])
    substring(n, inicio + 1)

substring("carlos")