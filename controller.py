import pygame
from main_menu import *

class Controller:
    sanity = 1
    sanity1 = pygame.image.load("Sprites//sanity1.png")
    sanity2 = pygame.image.load("Sprites//sanity2.png")
    sanity3 = pygame.image.load("Sprites//sanity3.png")
    sanity4 = pygame.image.load("Sprites//sanity4.png")
    sanity5 = pygame.image.load("Sprites//sanity5.png")
    def __init__(self, instance):
        pygame.init()
    def sanity_meter(self, window):
        if Controller.sanity == 1:
            window.blit(Controller.sanity1, (0,0))
        elif Controller.sanity == 2:
            window.blit(Controller.sanity2, (0,0))
        elif Controller.sanity == 3:
            window.blit(Controller.sanity3, (0,0))
        elif Controller.sanity == 4:
            window.blit(Controller.sanity4, (0,0))
        elif Controller.sanity == 5:
            window.blit(Controller.sanity5, (0,0))
