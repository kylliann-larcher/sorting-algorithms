from SRC.display_tri import SortingVisualizer
from sorting import Sorting




if __name__ == "__main__":
    app = SortingVisualizer()
    app.run()
    sort = Sorting(100000000)
    sort.quicksort(sort.table_creation())
