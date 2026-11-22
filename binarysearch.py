def binary_search(arr, target):
    
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


print(binary_search([11, 2, 3, 4, 5], 11))  
print(binary_search([1, 2, 3, 4, 5], 6))  