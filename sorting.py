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
                

    
    def quicksort(self):
        print('quick')


    
