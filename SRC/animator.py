class SortingAlgoAnimator:
    def __init__(self, values, algorithm_name):
        self.values = values
        self.n = len(values)
        self.algorithm_name = algorithm_name
        self.i = 0
        self.j = 0
        self.min_index = 0
        self.sorted = []

    def step(self):
        if self.algorithm_name == "bubble":
            return self.bubble_sort_step()
        elif self.algorithm_name == "insertion":
            return self.insertion_sort_step()
        elif self.algorithm_name == "selection":
            return self.selection_sort_step()
        return None

    def bubble_sort_step(self):
        if self.i < self.n:
            if self.j < self.n - self.i - 1:
                if self.values[self.j] > self.values[self.j + 1]:
                    self.values[self.j], self.values[self.j + 1] = self.values[self.j + 1], self.values[self.j]
                self.j += 1
                return [self.j - 1, self.j]
            else:
                self.j = 0
                self.i += 1
        else:
            return None
        return []

    def insertion_sort_step(self):
        if self.i < self.n:
            key = self.values[self.i]
            j = self.i - 1
            while j >= 0 and self.values[j] > key:
                self.values[j + 1] = self.values[j]
                j -= 1
            self.values[j + 1] = key
            self.i += 1
            return [j + 1, self.i]
        else:
            return None

    def selection_sort_step(self):
        if self.i < self.n:
            if self.j == 0:
                self.min_index = self.i
            if self.j < self.n:
                if self.values[self.j] < self.values[self.min_index]:
                    self.min_index = self.j
                self.j += 1
                return [self.min_index, self.j - 1]
            else:
                self.values[self.i], self.values[self.min_index] = self.values[self.min_index], self.values[self.i]
                self.i += 1
                self.j = self.i
        else:
            return None
        return []
