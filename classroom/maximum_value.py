def find_maximum(lst):
    if len(lst) == 0:
        return None
    return find_max(0, len(lst)-1, lst)

def find_max(i, j, lst):
    if i == j:
        return lst[i]
    mid = (i + j) // 2
    return max(
        find_max(i, mid, lst),
        find_max(mid+1, j, lst)
    )

print(find_maximum([1, 2, 3, 4, 10, 6, 7, 8, 9, 5])) # 10