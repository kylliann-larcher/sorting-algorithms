import random
import time
class Sorting():
    def __init__(self,number):
        self.number_in_table = number
        self.table = self.table_creation()
        self.empty_list = []
        

    def table_creation(self):
        self.table = [i for i in range(1 ,self.number_in_table)]
        random.shuffle(self.table)
        return self.table


    def bubble_sort(self):
        start_time= time.perf_counter()
        n = len(self.table)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.table[j] > self.table[j + 1]:
                # Échange des éléments
                    self.table[j], self.table[j + 1] = self.table[j + 1], self.table[j]
        counter =time.perf_counter()
        print(f"bubble execution time : {counter - start_time} secondes"  )


    def insertion_sort(self):
        start_time= time.perf_counter()

        for i in self.table:
            if len(self.empty_list) == 0 : 
                self.empty_list.append(i)
            else:
                for j,k in enumerate(self.empty_list):
                    if i < k:
                        self.empty_list.insert(j, i)
                        break
                else:
                    self.empty_list.append(i)
        counter =time.perf_counter()
        print(f"insertion execution time: {counter - start_time} secondes"  )                    


    def selection_sort(self):
        start_time= time.perf_counter()
        n = len(self.table)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if self.table[j] < self.table[min_index]:
                    min_index = j
        # Échange des valeurs
            self.table[i], self.table[min_index] = self.table[min_index], self.table[i] 
        counter =time.perf_counter()    
        print(f"selection sort execution time: {counter - start_time} secondes"  )  

    
    def quick_sort(self):
        self._quick_sort(0, len(self.table) - 1)

    def _quick_sort(self, low, high):
        if low < high:
            pi = self._partition(low, high)
            self._quick_sort(low, pi - 1)
            self._quick_sort(pi + 1, high)

    def _partition(self, low, high):
        pivot = self.table[high]
        i = low - 1
        for j in range(low, high):
            if self.table[j] <= pivot:
                i += 1
                self.table[i], self.table[j] = self.table[j], self.table[i]
        self.table[i + 1], self.table[high] = self.table[high], self.table[i + 1]
        return i + 1

    

    def peigne_sort(self):
        start_time= time.perf_counter()
        n = len(self.table)
        gap = n
        shrink = 1.3
        sorted = False
        while not sorted:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted = True
            for i in range(n - gap):
                if self.table[i] > self.table[i + gap]:
                    self.table[i], self.table[i + gap] = self.table[i + gap], self.table[i]
                    sorted = False
                    print(self.table)
        counter =time.perf_counter()
        print(f"peigne sort execution time : {counter - start_time} secondes"  )
    
    def merge_sort(self):
        self._merge_sort(0, len(self.table) - 1)

    def _merge_sort(self, left, right):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort(left, mid)
            self._merge_sort(mid + 1, right)
            self._merge(left, mid, right)

    def _merge(self, left, mid, right):
        L = self.table[left:mid+1]
        R = self.table[mid+1:right+1]
        i = j = 0
        k = left
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                self.table[k] = L[i]
                i += 1
            else:
                self.table[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            self.table[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            self.table[k] = R[j]
            j += 1
            k += 1

    
    def tri(self, n, i):
        largest = i 
        left = 2 * i + 1  
        right = 2 * i + 2  
        if left < n and self.table[left] > self.table[largest]:
            largest = left
        if right < n and self.table[right] > self.table[largest]:
            largest = right
        if largest != i:
            self.table[i], self.table[largest] = self.table[largest], self.table[i]  # Échanger
            self.tri( n, largest)
    
    def heap_sort(self):
        start_time= time.perf_counter()
        n = len(self.table)
        for i in range(n // 2 - 1, -1, -1):
            self.tri(n, i)
        for i in range(n - 1, 0, -1):
            self.table[i], self.table[0] = self.table[0], self.table[i]  
            self.tri( i, 0) 
        counter =time.perf_counter()
        print(f"tri par tas execution time : {counter - start_time} secondes"  )
            