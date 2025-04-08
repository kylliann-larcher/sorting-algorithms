class SortingAlgoAnimator:
    def __init__(self, values, algorithm_name):
        self.values = values
        self.n = len(values)
        self.algorithm_name = algorithm_name
        self.i = 0
        self.j = 0
        self.gap = self.n
        self.shrink = 1.3
        self.sorted = False
        self.heap_size = self.n
        self.stack = []
        self.merged = []
        self.left = 0
        self.right = self.n - 1
        self.gen = None
        self.min_index = 0
        self.init_generator()

    def init_generator(self):
        if self.algorithm_name == "bubble":
            self.gen = self._bubble_generator()
        elif self.algorithm_name == "insertion":
            self.gen = self._insertion_generator()
        elif self.algorithm_name == "selection":
            self.gen = self._selection_generator()
        elif self.algorithm_name == "heap":
            self.gen = self._heap_generator()
        elif self.algorithm_name == "merge":
            self.gen = self._merge_generator()
        elif self.algorithm_name == "peigne":
            self.gen = self._comb_generator()

    def step(self):
        try:
            return next(self.gen)
        except StopIteration:
            return None

    def _bubble_generator(self):
        for i in range(self.n):
            for j in range(0, self.n - i - 1):
                if self.values[j] > self.values[j + 1]:
                    self.values[j], self.values[j + 1] = self.values[j + 1], self.values[j]
                yield [j, j + 1]

    def _insertion_generator(self):
        for i in range(1, self.n):
            key = self.values[i]
            j = i - 1
            while j >= 0 and self.values[j] > key:
                self.values[j + 1] = self.values[j]
                yield [j, j + 1]
                j -= 1
            self.values[j + 1] = key
            yield [j + 1, i]

    def _selection_generator(self):
        for i in range(self.n):
            min_idx = i
            for j in range(i + 1, self.n):
                if self.values[j] < self.values[min_idx]:
                    min_idx = j
                yield [min_idx, j]
            self.values[i], self.values[min_idx] = self.values[min_idx], self.values[i]
            yield [i, min_idx]

    def _heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.values[left] > self.values[largest]:
            largest = left
        if right < n and self.values[right] > self.values[largest]:
            largest = right

        if largest != i:
            self.values[i], self.values[largest] = self.values[largest], self.values[i]
            yield [i, largest]
            yield from self._heapify(n, largest)

    def _heap_generator(self):
        n = self.n
        for i in range(n // 2 - 1, -1, -1):
            yield from self._heapify(n, i)
        for i in range(n - 1, 0, -1):
            self.values[0], self.values[i] = self.values[i], self.values[0]
            yield [0, i]
            yield from self._heapify(i, 0)

    def _merge_generator(self):
        def merge_sort_gen(arr, l, r):
            if l < r:
                m = (l + r) // 2
                yield from merge_sort_gen(arr, l, m)
                yield from merge_sort_gen(arr, m + 1, r)
                yield from merge(arr, l, m, r)

        def merge(arr, l, m, r):
            left = arr[l:m + 1]
            right = arr[m + 1:r + 1]
            i = j = 0
            k = l

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                yield [k]
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                yield [k]
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                yield [k]
                k += 1

        yield from merge_sort_gen(self.values, 0, self.n - 1)

    def _comb_generator(self):
        gap = self.n
        shrink = self.shrink
        sorted = False

        while not sorted:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted = True

            for i in range(0, self.n - gap):
                if self.values[i] > self.values[i + gap]:
                    self.values[i], self.values[i + gap] = self.values[i + gap], self.values[i]
                    sorted = False
                yield [i, i + gap]
