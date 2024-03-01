n = int(input())
A = [[int(value) for value in input().split()] for y in range(n)]

# Calcular a segunda menor soma sem usar sum ou min
row_sums = [0] * n
second_min_sum = float('inf')

for y in range(n):
    current_sum = 0
    for x in range(n):
        current_sum += A[y][x]
    row_sums[y] = current_sum

    # Encontrar a segunda menor soma durante o cálculo
    if current_sum < second_min_sum:
        second_min_sum = current_sum

# Encontrar a linha onde a soma não é igual à segunda menor soma
cy = -1
for y in range(n):
    if row_sums[y] != second_min_sum:
        cy = y

# Encontrar a coluna onde a soma não é igual à segunda menor soma
cx = -1
for x in range(n):
    col_sum = 0
    for y in range(n):
        col_sum += A[y][x]
    if col_sum != second_min_sum:
        cx = x

# Imprimir os resultados
print(A[cy][cx] + (second_min_sum - row_sums[cy]), A[cy][cx])
