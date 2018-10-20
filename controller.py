import pygame
from club_level import *
from typing_level import *
from main_menu import *

class Controller:
    sanity = 1
    scence = 0
    sanity1 = pygame.image.load("Sprites//sanity1.png")
    sanity2 = pygame.image.load("Sprites//sanity2.png")
    sanity3 = pygame.image.load("Sprites//sanity3.png")
    sanity4 = pygame.image.load("Sprites//sanity4.png")
    sanity5 = pygame.image.load("Sprites//sanity5.png")
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800,600))
        self.running = True
        while self.running:

            if Controller.scence == 0:
                men = Menu()
            elif Controller.scence == 1:
                club = Club()

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
