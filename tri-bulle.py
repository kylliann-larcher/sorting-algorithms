tableau = [i for i in range (1, 1000)]
print("Tableau avant le tri:", tableau)
def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)
bubble(tableau)