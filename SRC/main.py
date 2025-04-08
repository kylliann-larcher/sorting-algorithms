from sorting import Sorting
from display_tri import Display
from animator import SortingAlgoAnimator
from menu import AlgoMenu
import sys


while True:
    menu = AlgoMenu()
    algo_name, size = menu.run()

    while True:
        s = Sorting(size)
        values = s.table.copy()

        algo = SortingAlgoAnimator(values, algo_name)
        display = Display(values, algo_name)
        display.run_animation(algo.step)

        choice = display.get_user_choice()
        if choice == "retry":
            continue  # relancer avec même algo
        elif choice == "menu":
            break  # retour au menu
        else:
            sys.exit()
