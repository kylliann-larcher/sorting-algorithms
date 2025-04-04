import random

class Sorting():
    def __init__(self,number):
        self.number_in_table = number
        self.table = self.table_creation()
        

    def table_creation(self):
        self.table = [i for i in range(1 ,self.number_in_table)]
        random.shuffle(self.table)
        return self.table
    
    def insertion_sort(self):
        print('insertion')
    
    def quicksort(self):
        print('quick')

    def selection_sort(self):
        n = len(self.table)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if self.table[j] < self.table[min_index]:
                    min_index = j
        # Échange des valeurs
            self.table[i], self.table[min_index] = self.table[min_index], self.table[i]

    def bubble_sort(self):
        n = len(self.table)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.table[j] > self.table[j + 1]:
                # Échange des éléments
                    self.table[j], self.table[j + 1] = self.table[j + 1], self.table[j]





    
sort = Sorting(20)
print("Avant tri :", sort.table)