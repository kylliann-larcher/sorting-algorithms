class SortingAlgoAnimator:
    def __init__(self, values, algorithm_name):
        self.values = values
        self.n = len(values)
        self.algorithm_name = algorithm_name
        self.index_i = 0
        self.index_j = 0
        self.done = False

    def step(self):
        """Effectue une étape d’animation selon l’algorithme choisi."""
        if self.algorithm_name == "bubble":
            return self.bubble_sort_step()
        # Tu pourras ajouter d'autres algos ici plus tard
        return self.done

    def bubble_sort_step(self):
        """Étape de tri à bulle animée"""
        if self.index_i < self.n:
            if self.index_j < self.n - self.index_i - 1:
                if self.values[self.index_j] > self.values[self.index_j + 1]:
                    self.values[self.index_j], self.values[self.index_j + 1] = self.values[self.index_j + 1], self.values[self.index_j]
                self.index_j += 1
            else:
                self.index_j = 0
                self.index_i += 1
        else:
            self.done = True
        return self.done
