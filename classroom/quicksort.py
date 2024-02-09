import time
def quicksort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[len(array)-1]
    left = []
    right = []
    for i in range(len(array)-1):
        if array[i] < pivot:
            left.append(array[i])
        else:
            right.append(array[i])

    return quicksort(left) + [pivot] + quicksort(right)

array = [3, 6, 8, 10, 1, 2, 1, 5, 7, 4, 9, 5, 2, 3, 6, 8, 10, 1, 2, 1, 5, 7, 4, 9, 5, 2, 3, 6, 8, 10, 1, 2, 1, 5, 7, 4, 9, 5, 2, 3, 6, 8, 10, 1, 2, 1, 5, 7, 4, 9, 5, 2, 3, 6, 8, 10, 1, 2, 1, 5, 7, 4, 9, 5, 2, 3, 6, 8, 10, 1, 2, 1, 5, 7, 4, 9, 5, 2, 3, 6, 8, 10, 1, 2, 1, 5, 7, 4, 9, 5, 2, 3, 6, 8, 10, 1, 2, 1, 5, 7, 4, 9, 5, 2, 3, 6, 8, 10, 1, 2, 1, 5, 7, 4, 9, 5]
print(quicksort(array))