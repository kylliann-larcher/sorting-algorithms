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
        self.width, self.height = 1000, 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(f"Animation tri : {algo_name}")
        self.font = pygame.font.SysFont(None, 30)
        self.big_font = pygame.font.SysFont(None, 50)
        self.start_time = time.perf_counter()
        self.end_time = None
        self.clock = pygame.time.Clock()
        self.running = True
        self.finished = False
        self.user_choice = None  # "menu" ou "retry"

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

                # Règle de mesure
        ruler_x = self.width // 2
        step = 50  # tous les 50 pixels
        for y in range(50, self.height - 50, step):
            pygame.draw.line(self.screen, (0, 0, 0), (ruler_x - 10, y), (ruler_x + 10, y), 2)
            val = int((self.height - y) / (self.height - 100) * max_val)
            label = self.font.render(str(val), True, (0, 0, 0))
            self.screen.blit(label, (ruler_x + 15, y - 10))


        elapsed = self.end_time - self.start_time if self.finished else time.perf_counter() - self.start_time
        txt1 = self.font.render(f"Algorithme : {self.algo_name}", True, (0, 0, 0))
        txt2 = self.font.render(f"Temps : {elapsed:.4f} sec", True, (0, 0, 0))
        self.screen.blit(txt1, (10, 10))
        self.screen.blit(txt2, (10, 40))

        if self.finished:
            msg1 = self.big_font.render("VOS DONNÉES SONT TRIÉES", True, (0, 100, 0))
            msg2 = self.font.render("Appuie sur R pour recommencer ou M pour retourner au menu", True, (0, 100, 0))
            self.screen.blit(msg1, (self.width // 2 - msg1.get_width() // 2, self.height // 2 - 40))
            self.screen.blit(msg2, (self.width // 2 - msg2.get_width() // 2, self.height // 2 + 10))
            msg3 = self.font.render("Appuie sur V pour voir les données dans le terminal", True, (0, 100, 0))
            self.screen.blit(msg3, (self.width // 2 - msg3.get_width() // 2, self.height // 2 + 40))


        pygame.display.update()

    def run_animation(self, step_function):
        while self.running:
            if not self.finished:
                highlight = step_function()
                if highlight is None:
                    self.finished = True
                    self.end_time = time.perf_counter()
                self.draw_bars(highlight)
            else:
                self.draw_bars()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            self.user_choice = "retry"
                            self.running = False
                        elif event.key == pygame.K_m:
                            self.user_choice = "menu"
                            self.running = False
                        elif event.key == pygame.K_v:
                            print("\n📋 Données générées :")
                            print("Avant tri :", self.original_values)
                            print("Après tri :", self.values)
                                            
            self.clock.tick(60)

        pygame.quit()

    def get_user_choice(self):
        return self.user_choice
