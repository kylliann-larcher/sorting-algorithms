tableau = [i for i in range (1, 1000)]
print("Tableau avant le tri:", tableau)
def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key 
        print(arr)
insertion(tableau)