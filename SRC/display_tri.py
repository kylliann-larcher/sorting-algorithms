import pygame
import random
import sys
import time
from sorter import Sorter

class SortingVisualizer:
    def __init__(self, width=800, height=600, nb_bars=50):
        pygame.init()
        self.WIDTH = width
        self.HEIGHT = height
        self.nb_bars = nb_bars
        self.WHITE = (255, 255, 255)
        self.GREY = (160, 160, 160)
        self.RED = (255, 0, 0)

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Visualisation du tri")
        self.clock = pygame.time.Clock()

        self.values = [random.randint(10, self.HEIGHT - 10) for _ in range(self.nb_bars)]
        self.sorter = Sorter(self.values, visualizer=self)

    def draw_bars(self, color_index=-1, color_index2=-1):
        self.screen.fill(self.WHITE)
        bar_width = self.WIDTH // self.nb_bars
        for i, val in enumerate(self.values):
            if i == color_index or i == color_index2:
                color = self.RED
            else:
                color = self.GREY
            pygame.draw.rect(self.screen, color, (i * bar_width, self.HEIGHT - val, bar_width - 2, val))
        pygame.display.update()
        pygame.time.delay(10)

    def run(self):
        running = True
        started = False
        while running:
            self.draw_bars()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not started:
                        started = True
                        self.sorter.bubble_sort()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()
