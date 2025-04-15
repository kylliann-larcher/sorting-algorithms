from menu import AlgoMenu
from sorting import Sorting
from display_tri import Display
from animator import SortingAlgoAnimator
from headless_sort import run_terminal_sort

if __name__ == "__main__":
    while True:  # Boucle MENU
        menu = AlgoMenu()
        algo_name, size = menu.run()

        if size > 300:
            run_terminal_sort(algo_name, size)
            exit()

        while True:  # Boucle TRI
            s = Sorting(size)
            values = s.table.copy()

            algo = SortingAlgoAnimator(values, algo_name)
            display = Display(values, algo_name)
            display.run_animation(algo.step)

            choice = display.get_user_choice()
            if choice == "retry":
                continue
            elif choice == "menu":
                break  # revient au menu
            else:
                exit()
