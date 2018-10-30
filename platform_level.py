import pygame
from controller import *

pygame.init()
class PlatformLevel:
    def __init__(self):
        self.window = pygame.display.set_mode((800,600))
        self.running = True
        while self.running:
            for event in pygame.event.get():
                # Quit button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # Keybinds
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
