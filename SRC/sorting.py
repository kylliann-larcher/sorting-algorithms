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

    
    def quicksort(self, table, top_level=True):
        if top_level:
            start_time= time.perf_counter()

        if len(table)<=1:
            return table

        pivot_choice = random.randint(0, len(table)-1)
        pivot = table[pivot_choice]
        ##rest = table[:pivot_choice] + table[pivot_choice+1:]
        under_number = [i for i in table if i < pivot]
        beyond_number = [i for i in table if i > pivot]
        
        """for i in rest:
            if i < pivot:
                under_number.append(i)
            elif i > pivot:
                beyond_number.append(i)"""
                
        table_sort = self.quicksort(under_number, False) + [pivot] + self.quicksort(beyond_number, False)
        
        if top_level:
            counter =time.perf_counter()
            print(f"quicksort execution time : {counter - start_time} secondes"  )
        
        return table_sort
    

    def peigne(self):
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
    
    def merge(self, table, top_level=True):
        
        if top_level:
            start_time= time.perf_counter()

        if len(table) > 1:
            mid = len(table) // 2  
            left_half = table[:mid]  
            right_half = table[mid:]

            left_sorted = self.merge(left_half)  
            right_sorted = self.merge(right_half)  

            i = j = k = 0
            while i < len(left_sorted) and j < len(right_sorted):
                if left_sorted[i] < right_sorted[j]:
                    table[k] = left_sorted[i]
                    i += 1
                else:
                    table[k] = right_sorted[j]
                    j += 1
                k += 1
            while i < len(left_sorted):
                table[k] = left_sorted[i]
                i += 1
                k += 1
            while j < len(right_sorted):
                table[k] = right_sorted[j]
                j += 1
                k += 1

        if top_level:
            counter =time.perf_counter()
            print(f"merge sort execution time : {counter - start_time} secondes"  )
        

        return table
    
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
    
    def heap(self):
        start_time= time.perf_counter()
        n = len(self.table)
        for i in range(n // 2 - 1, -1, -1):
            self.tri(n, i)
        for i in range(n - 1, 0, -1):
            self.table[i], self.table[0] = self.table[0], self.table[i]  
            self.tri( i, 0) 
        counter =time.perf_counter()
        print(f"tri par tas execution time : {counter - start_time} secondes"  )
            