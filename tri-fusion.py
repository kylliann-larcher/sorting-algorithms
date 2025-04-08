tableau = [i for i in range (1, 1000)]
print("Tableau avant le tri:", tableau)
def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  
        left_half = arr[:mid]  
        right_half = arr[mid:]

        merge(left_half)  
        merge(right_half)  
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    print(arr)
merge(tableau)