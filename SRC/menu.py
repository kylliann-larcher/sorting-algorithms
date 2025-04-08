import pygame
import sys

class AlgoMenu:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 1200, 720
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Choix de l'algorithme de tri")
        self.FONT = pygame.font.SysFont(None, 36)
        self.options = [
            ("Appuie sur B pour Tri à bulle", pygame.K_b, "bubble"),
            ("Appuie sur I pour Tri par insertion", pygame.K_i, "insertion"),
            ("Appuie sur S pour Tri par sélection", pygame.K_s, "selection"),
            ("ESC pour quitter", pygame.K_ESCAPE, None),
        ]

    def draw(self):
        self.SCREEN.fill((255, 255, 255))
        for i, (text, _, _) in enumerate(self.options):
            rendered = self.FONT.render(text, True, (0, 0, 0))
            self.SCREEN.blit(rendered, (40, 50 + i * 40))
        pygame.display.update()

    def run(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    for _, key, algo in self.options:
                        if event.key == key:
                            if algo is None:
                                pygame.quit()
                                sys.exit()
                            return algo
