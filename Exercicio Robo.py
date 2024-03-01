class Position:
    def __init__(self, x, y, prox_x, prox_y):
        self.x = x
        self.y = y
        self.prox_x = prox_x
        self.prox_y = prox_y

def main():
    while True:
        L, C, S = map(int, input().split())
        if L == 0:
            break

        fig = 0
        tab = [input().strip() for _ in range(L)]
        cmd = input().strip()

        pos = None
        for i in range(L):
            for j in range(C):
                if tab[i][j] != '.' and tab[i][j] != '*' and tab[i][j] != '#':
                    pos = Position(i, j, 0, 0)
                    if tab[i][j] == 'N':
                        pos.prox_x = i - 1
                        pos.prox_y = j
                    elif tab[i][j] == 'S':
                        pos.prox_x = i + 1
                        pos.prox_y = j
                    elif tab[i][j] == 'L':
                        pos.prox_x = i
                        pos.prox_y = j + 1
                    elif tab[i][j] == 'O':
                        pos.prox_x = i
                        pos.prox_y = j - 1

        for i in range(S):
            if cmd[i] == 'D':
                if pos.prox_y == pos.y:
                    pos.prox_x, pos.prox_y = (pos.x, pos.y - 1) if pos.prox_x > pos.x else (pos.x, pos.y + 1)
                else:
                    pos.prox_x, pos.prox_y = (pos.x + 1, pos.y) if pos.prox_y > pos.y else (pos.x - 1, pos.y)
            elif cmd[i] == 'E':
                if pos.prox_x == pos.x:
                    pos.prox_x, pos.prox_y = (pos.x - 1, pos.y) if pos.prox_y > pos.y else (pos.x + 1, pos.y)
                else:
                    pos.prox_x, pos.prox_y = (pos.x, pos.y + 1) if pos.prox_x > pos.x else (pos.x, pos.y - 1)
            elif cmd[i] == 'F':
                if (
                    0 <= pos.prox_x < L
                    and 0 <= pos.prox_y < C
                    and tab[pos.prox_x][pos.prox_y] != '#'
                ):
                    if tab[pos.prox_x][pos.prox_y] == '*':
                        tab[pos.prox_x] = tab[pos.prox_x][: pos.prox_y] + '.' + tab[pos.prox_x][pos.prox_y + 1 :]
                        fig += 1
                    if pos.prox_y == pos.y:
                        pos.x, pos.prox_x = pos.prox_x, pos.prox_x + 1 if pos.prox_x > pos.x else pos.prox_x - 1
                    else:
                        pos.y, pos.prox_y = pos.prox_y, pos.prox_y + 1 if pos.prox_y > pos.y else pos.prox_y - 1

        print(fig)

if __name__ == "__main__":
    main()
