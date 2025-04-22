import  pygame

# Clase Piedra
class Piedra:
    def __init__(self, width, height, color, x, y):
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)