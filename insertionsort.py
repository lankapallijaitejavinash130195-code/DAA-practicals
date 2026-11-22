def insertion_sort_new(arr):
    res = arr[:]  
    for i in range(1, len(res)):
        key = res[i]
        j = i - 1
        while j >= 0 and res[j] > key:
            res[j + 1] = res[j]
            j -= 1
        res[j + 1] = key
    return res


orig = [7,5,3,1]
print(insertion_sort_new(orig))  
print(orig)  