from sorting import Sorting
from display_tri import Display
from animator import SortingAlgoAnimator
from menu import AlgoMenu

if __name__ == "__main__":
    menu = AlgoMenu()
    algo_name = menu.run()

    s = Sorting(80)
    values = s.table

    algo = SortingAlgoAnimator(values, algo_name)
    display = Display(values, algo_name)
    display.run_animation(algo.step)
