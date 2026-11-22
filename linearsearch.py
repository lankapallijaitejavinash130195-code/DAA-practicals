def linear_search(arr, target):
    
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

print(linear_search([4, 2, 7, 1], 7))  
print(linear_search([4, 2, 7, 1], 5))  