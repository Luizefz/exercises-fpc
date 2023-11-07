num_decimais = [int(i) for i in input().split()]

casas_binarias = [4294967296, 2147483648, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

num_01_casas = []
num_02_casas = []
num_soma_casas = []
num_soma_decimal = 0

for i in casas_binarias:
        num_01_casas.append(int(num_decimais[0]/i)) # pega o inteiro da divisão do numero digitado, pelos resultados das elevacoes na base 2
        num_decimais[0] = num_decimais[0] % i # atribui o resto da divisão ao numero, se não for divisível, resto == proprio numero, se nao resto == resto

        num_02_casas.append(int(num_decimais[1]/i))
        num_decimais[1] = num_decimais[1] % i

for casa_num_01, casa_num_02 in zip(num_01_casas, num_02_casas):
    if casa_num_01 == casa_num_02: # faz um XOR comparando os 2 elementos de mesmo indice das listas
        num_soma_casas.append(0)
    else:
        num_soma_casas.append(1)

for casa_num_soma, casas_num_binario in zip(num_soma_casas, casas_binarias):
     if casa_num_soma == 1:
          num_soma_decimal += casas_num_binario


print(f'  {num_01_casas}\n+ {num_02_casas}\n  {num_soma_casas}\n  {num_soma_decimal}')