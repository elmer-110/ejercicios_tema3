import pygame
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)  # Definición del color negro
FPS = 60

# Clase Torre
class Torre:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.piedras = []

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x - 10, self.y - 200, 20, 400))
        for piedra in self.piedras:
            piedra.draw(screen)

    def add_piedra(self, piedra):
        if not self.piedras or piedra.width < self.piedras[-1].width:
            piedra.rect.center = (self.x, self.y - len(self.piedras) * 20)
            self.piedras.append(piedra)
        else:
            raise ValueError("No puedes colocar una piedra más grande sobre una más pequeña.")

    def remove_piedra(self):
        if self.piedras:
            return self.piedras.pop()
        return None
