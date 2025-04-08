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
        print(f"le temps d'execution est de : {counter - start_time} secondes"  )                    
                

    
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
            print(f"le temps d'execution est de : {counter - start_time} secondes"  )
        
        return table_sort
    
        