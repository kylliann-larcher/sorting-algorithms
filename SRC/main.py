import random
import pygame
import sys
from animator import SortingAlgoAnimator
from display_tri import DisplayTri

def generate_list(n):
    return [random.randint(10, 500) for _ in range(n)]

def main():
    pygame.init()
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Choix de l'algorithme de tri")
    font = pygame.font.SysFont(None, 40)

    menu_text = [
        "Appuie sur B pour Bubble Sort",
        "Appuie sur Q pour Quick Sort (à venir)",
        "Appuie sur ESC pour quitter"
    ]

    running = True
    while running:
        screen.fill((255, 255, 255))

        for i, line in enumerate(menu_text):
            text = font.render(line, True, (0, 0, 0))
            screen.blit(text, (50, 100 + i * 50))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_b:
                    start_sorting("bubble")
                    running = False

def start_sorting(algo_name):
    values = generate_list(80)
    animator = SortingAlgoAnimator(values, algo_name)
    visual = DisplayTri(values, algo_name)

    clock = pygame.time.Clock()
    while True:
        visual.draw_bars(current_indices=[animator.index_j, animator.index_j + 1] if not animator.done else [])
        if not animator.done:
            animator.step()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)

if __name__ == "__main__":
    main()
