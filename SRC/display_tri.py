import pygame
import sys
import time

class Display:
    def __init__(self, values, algo_name="bubble"):
        pygame.init()
        self.values = values
        self.original_values = values.copy()
        self.n = len(values)
        self.algo_name = algo_name
        self.width, self.height = 1200, 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(f"Animation tri : {algo_name}")
        self.font = pygame.font.SysFont(None, 30)
        self.start_time = time.perf_counter()
        self.clock = pygame.time.Clock()
        self.running = True

    def draw_bars(self, highlight=None):
        self.screen.fill((255, 255, 255))
        bar_width = self.width // self.n
        max_val = max(self.values)

        for i, val in enumerate(self.values):
            bar_height = int((val / max_val) * (self.height - 100))
            x = i * bar_width
            y = self.height - bar_height
            color = (255, 0, 0) if highlight and i in highlight else (100, 100, 255)
            pygame.draw.rect(self.screen, color, (x, y, bar_width - 2, bar_height))

        pygame.draw.line(self.screen, (0, 0, 0), (self.width // 2, 0), (self.width // 2, self.height), 3)

        elapsed = time.perf_counter() - self.start_time
        txt1 = self.font.render(f"Algorithme : {self.algo_name}", True, (0, 0, 0))
        txt2 = self.font.render(f"Temps : {elapsed:.4f} sec", True, (0, 0, 0))
        self.screen.blit(txt1, (10, 10))
        self.screen.blit(txt2, (10, 40))

        pygame.display.update()

    def run_animation(self, step_function):
        while self.running:
            highlight = step_function()
            if highlight is None:
                self.running = False
            self.draw_bars(highlight)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.clock.tick(60)
        time.sleep(2)
        pygame.quit()
        sys.exit()
