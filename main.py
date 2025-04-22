import pygame
import sys


# Configuración inicial
pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE, BLACK, RED = (255, 255, 255), (0, 0, 0), (255, 0, 0)
FPS = 60




# Main
if __name__ == "__main__":
    juego = Lanzador()
    juego.run()