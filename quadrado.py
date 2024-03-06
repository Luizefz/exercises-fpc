def is_almost_magic(square):
    n = len(square)
    row_sum = [sum(row) for row in square]
    col_sum = [sum(col) for col in zip(*square)]
    diagonal_sum = sum(square[i][i] for i in range(n))
    anti_diagonal_sum = sum(square[i][n - i - 1] for i in range(n))

    magic_number = min(row_sum[0], col_sum[0], diagonal_sum, anti_diagonal_sum)

    for i in range(n):
        if row_sum[i] != magic_number:
            return False, (magic_number - row_sum[i], square[i][row_sum[i:].index(magic_number) + i])
        if col_sum[i] != magic_number:
            return False, (magic_number - col_sum[i], square[col_sum[i:].index(magic_number) + i][i])
        if diagonal_sum != magic_number:
            for j in range(n):
                if square[j][j] != magic_number:
                    return False, (magic_number - square[j][j], magic_number)
        if anti_diagonal_sum != magic_number:
            for j in range(n):
                if square[j][n - j - 1] != magic_number:
                    return False, (magic_number - square[j][n - j - 1], magic_number)

    return True, None

# Função para ler a entrada
def read_input():
    n = int(input())
    square = [list(map(int, input().split())) for _ in range(n)]
    return n, square

# Função para imprimir a saída
def print_output(original, new):
    print(original, new)

def main():
    n, square = read_input()
    almost_magic, altered_number = is_almost_magic(square)
    if not almost_magic:
        print_output(*altered_number)

if __name__ == "__main__":
    main()
