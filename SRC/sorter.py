class Sorter:
    def __init__(self, values, visualizer=None):
        self.values = values
        self.visualizer = visualizer  

    def bubble_sort(self):
        n = len(self.values)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.visualizer:
                    self.visualizer.draw_bars(j, j + 1)
                if self.values[j] > self.values[j + 1]:
                    self.values[j], self.values[j + 1] = self.values[j + 1], self.values[j]

    def selection_sort(self):
        n = len(self.table)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if self.table[j] < self.table[min_index]:
                    min_index = j
        # Échange des valeurs
            self.table[i], self.table[min_index] = self.table[min_index], self.table[i]
