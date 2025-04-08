import pygame
import sys
import time

class DisplayTri:
    def __init__(self, values, algo_name="bubble"):
        pygame.init()
        self.WIDTH, self.HEIGHT = 1000, 600
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Animation du tri")
        self.FONT = pygame.font.SysFont(None, 30)

        self.values = values
        self.algo_name = algo_name
        self.running = True
        self.start_time = time.perf_counter()

    def draw_bars(self, current_indices=None):
        self.SCREEN.fill((255, 255, 255))
        bar_width = (self.WIDTH - 50) // len(self.values)
        max_val = max(self.values)

        for i, val in enumerate(self.values):
            bar_height = int((val / max_val) * (self.HEIGHT - 100))
            x = 25 + i * bar_width
            y = self.HEIGHT - bar_height

            color = (100, 100, 255)
            if current_indices and i in current_indices:
                color = (255, 0, 0)
            pygame.draw.rect(self.SCREEN, color, (x, y, bar_width - 2, bar_height))

        # Ligne centrale
        pygame.draw.line(self.SCREEN, (0, 0, 0), (self.WIDTH // 2, 0), (self.WIDTH // 2, self.HEIGHT), 3)

        # Infos
        elapsed = time.perf_counter() - self.start_time
        time_text = self.FONT.render(f"Temps : {elapsed:.4f} sec", True, (0, 0, 0))
        algo_text = self.FONT.render(f"Algo : {self.algo_name}", True, (0, 0, 0))
        self.SCREEN.blit(time_text, (10, 10))
        self.SCREEN.blit(algo_text, (10, 40))

        pygame.display.update()
