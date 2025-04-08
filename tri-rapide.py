tableau = [i for i in range (1, 1000)]
print("Tableau avant le tri:", tableau)
def rapide(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] 
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]  
    right = [x for x in arr if x > pivot]  
    return rapide(left) + middle + rapide(right) 
    print(arr)
rapide(tableau)