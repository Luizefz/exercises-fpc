num_decimais = [int(i) for i in input().split()]
casas_binarias = [4294967296, 2147483648, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

num_01_bin = ''
num_02_bin = ''

for i in casas_binarias:
        num_01_bin += str(num_decimais[0] // i) # pega a divisão inteira do numero digitado pelos resultados das elevacoes na base 2
        num_decimais[0] = num_decimais[0] % i # atribui o resto da divisão ao numero, se não for divisível, resto == proprio numero, se nao resto == resto

        num_02_bin += str(num_decimais[1] // i)
        num_decimais[1] = num_decimais[1] % i
# while num_decimais[0] >= 1:
#     num_01_bin.append(num_decimais[0] % 2)
#     num_decimais[0] = num_decimais[0] // 2

# while num_decimais[1] >= 1:
#     num_02_bin.append(num_decimais[1] % 2)
#     num_decimais[1] = num_decimais[1] // 2

