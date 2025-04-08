tableau = [i for i in range (1, 1000)]
print("Tableau avant le tri:", tableau)
def tri(arr, n, i):
    largest = i 
    left = 2 * i + 1  
    right = 2 * i + 2  
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Échanger
        tri(arr, n, largest)
def heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        tri(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        tri(arr, i, 0) 
        print(arr)
heap(tableau)