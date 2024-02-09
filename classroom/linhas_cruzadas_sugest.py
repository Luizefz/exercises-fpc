def update(bit, n, i, v):
    i += 1
    while i <= n:
        bit[i] += v
        i += i & (-i)

def get_sum(bit, i):
    s = 0
    i += 1
    while i > 0:
        s += bit[i]
        i -= i & (-i)
    return s

def count_crossings(n, a):
    bit = [0]*(n+1)
    crossings = 0
    for i in range(n-1, -1, -1):
        crossings += get_sum(bit, a[i]-1)
        update(bit, n, a[i], 1)
    return crossings

n = int(input())
a = list(map(int, input().split()))
print(count_crossings(n, a))