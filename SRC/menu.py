import pygame
import sys

class AlgoMenu:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 500
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Choix du tri et de la taille")
        self.FONT = pygame.font.SysFont(None, 36)
        self.options = [
            ("B: Tri à bulle", pygame.K_b, "bubble"),
            ("I: Insertion", pygame.K_i, "insertion"),
            ("S: Sélection", pygame.K_s, "selection"),
            ("H: Tas (heap)", pygame.K_h, "heap"),
            ("M: Fusion (merge)", pygame.K_m, "merge"),
            ("P: Peigne (comb)", pygame.K_p, "peigne"),
        ]
        self.selected_algo = None
        self.size_input = ""
        self.finished = False

    def draw(self):
        self.SCREEN.fill((255, 255, 255))
        title = self.FONT.render("Choisis un algorithme de tri :", True, (0, 0, 0))
        self.SCREEN.blit(title, (40, 30))

        for i, (text, _, _) in enumerate(self.options):
            color = (0, 0, 255) if self.selected_algo == self.options[i][2] else (0, 0, 0)
            rendered = self.FONT.render(text, True, color)
            self.SCREEN.blit(rendered, (60, 70 + i * 40))

        input_label = self.FONT.render("Entrez le nombre d'éléments à trier :", True, (0, 0, 0))
        input_box = self.FONT.render(self.size_input or "...", True, (255, 0, 0))
        self.SCREEN.blit(input_label, (40, 340))
        self.SCREEN.blit(input_box, (500, 340))

        if self.selected_algo and self.size_input.isdigit():
            confirm = self.FONT.render("Appuie sur ENTREE pour valider", True, (0, 150, 0))
            self.SCREEN.blit(confirm, (200, 400))

        pygame.display.update()

    def run(self):
        while not self.finished:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    # Choix de l'algo
                    for _, key, algo in self.options:
                        if event.key == key:
                            self.selected_algo = algo

                    # Entrée clavier pour la taille
                    if event.unicode.isdigit():
                        self.size_input += event.unicode
                    elif event.key == pygame.K_BACKSPACE:
                        self.size_input = self.size_input[:-1]
                    elif event.key == pygame.K_RETURN:
                        if self.selected_algo and self.size_input.isdigit():
                            self.finished = True

        return self.selected_algo, int(self.size_input)
