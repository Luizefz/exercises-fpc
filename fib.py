num_testes = int(input())
fib_num = []
fib_calls = -1

def fib(number):
    global fib_calls

    fib_calls += 1

    if number <= 1: 
        return number
        
    return fib(number - 1) + fib(number - 2)    

for i in range(num_testes):
    fib_num.append(int(input()))

for i in fib_num:
    valor_fib = fib(i)
    print(f'fib({i}) = {fib_calls} calls = {valor_fib}')
    fib_calls = -1