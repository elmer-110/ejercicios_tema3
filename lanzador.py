import pygame
from lanzador import Lanzador
from torre import Torre
from piedra import Piedra
import sys
# Clase Lanzador
class Lanzador:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Torre de Hanói")
        self.clock = pygame.time.Clock()
        self.torres = [Torre(200, 500), Torre(400, 500), Torre(600, 500)]
        self.piedras = [Piedra(140 - i * 20, 20, RED, 0, 0) for i in range(7)]
        for piedra in self.piedras:
            self.torres[0].add_piedra(piedra)
        self.selected_piedra = None
        self.selected_torre = None

    def run(self):
        while True:
            self.screen.fill(WHITE)
            self.handle_events()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_click(event.pos)

    def handle_click(self, pos):
        for i, torre in enumerate(self.torres):
            if torre.x - 50 < pos[0] < torre.x + 50:
                if self.selected_piedra is None:
                    self.selected_piedra = torre.remove_piedra()
                    self.selected_torre = i
                else:
                    try:
                        self.torres[i].add_piedra(self.selected_piedra)
                        self.selected_piedra = None
                        self.selected_torre = None
                    except ValueError:
                        self.torres[self.selected_torre].add_piedra(self.selected_piedra)
                        self.selected_piedra = None
                        self.selected_torre = None

    def draw(self):
        for torre in self.torres:
            torre.draw(self.screen)
        if self.selected_piedra:
            self.selected_piedra.rect.center = pygame.mouse.get_pos()
            self.selected_piedra.draw(self.screen)