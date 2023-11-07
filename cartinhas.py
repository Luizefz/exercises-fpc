def MDC_cartas(cartas_01, cartas_02):
    if cartas_01 % cartas_02 == 0:
        return cartas_02
    elif cartas_02 % cartas_01 == 0:
        return cartas_01
    else:
        return MDC_cartas(cartas_02, cartas_01 % cartas_02)
    

num_duplas = int(input())
num_cartas = [[int(i) for i in input().split()] for i in range(num_duplas)]

for i in num_cartas:
    print(MDC_cartas(i[0], i[1]))