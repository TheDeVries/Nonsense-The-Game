import pygame

class Controller:
    scene = 0
    def __init__(self):
        pygame.init()
        self.running_menu = True
        self.window = pygame.display.set_mode((800,600))
        self.sanity = 1
        self.sanity1 = pygame.image.load("Sprites//sanity1.png")
        self.sanity2 = pygame.image.load("Sprites//sanity2.png")
        self.sanity3 = pygame.image.load("Sprites//sanity3.png")
        self.sanity4 = pygame.image.load("Sprites//sanity4.png")
        self.sanity5 = pygame.image.load("Sprites//sanity5.png")
        while self.running_menu:
            if Controller.scene == 0:
                men = Menu()
            elif Controller.scene == 1:
                club = Club()
            elif Controller.scene == 2:
                mazey = Maze()
                if mazey.toggle == False:
                    print("hi")
                    Controller.scene -= 1





    def sanity_meter(self, window):
        if self.sanity == 1:
            window.blit(self.sanity1, (0,0))
        elif self.sanity == 2:
            window.blit(self.sanity2, (0,0))
        elif self.sanity == 3:
            window.blit(self.sanity3, (0,0))
        elif self.sanity == 4:
            window.blit(self.sanity4, (0,0))
        elif self.sanity == 5:
            window.blit(self.sanity5, (0,0))
from club_level import *
from typing_level import *
from main_menu import *
from maze_level import *
