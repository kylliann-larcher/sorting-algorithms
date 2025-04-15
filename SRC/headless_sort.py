import time
from sorting import Sorting

def run_terminal_sort(algo_name, size):
    print(f"🔎 Taille {size} trop grande pour l'affichage visuel. Tri en cours dans le terminal...")

    s = Sorting(size)
    start = time.perf_counter()

    if algo_name == "bubble":
        s.bubble_sort()
    elif algo_name == "insertion":
        s.insertion_sort()
    elif algo_name == "selection":
        s.selection_sort()
    elif algo_name == "heap":
        s.heap_sort()
    elif algo_name == "merge":
        s.merge_sort()
    elif algo_name == "peigne":
        s.peigne_sort()
    elif algo_name == "quicksort":
        s.quick_sort()

    else:
        print("❌ Algorithme non reconnu.")
        return

    end = time.perf_counter()
    print(f"✅ Tri terminé en {end - start:.4f} secondes.")
