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

    






