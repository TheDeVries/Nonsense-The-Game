import pygame
from main_menu import *

class Instructions:
    def __init__(self):
        self.window = pygame.display.set_mode((800,600))
        self.running = True

        # Main Menu Loop
        while self.running:
            for event in pygame.event.get():
                # Quit button
                if event.type == pygame.QUIT:
                    foo = Menu()
                    self.running = False

                # Keybinds
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        bar = Menu()
                        self.running = False

                self.instruct()

                pygame.display.flip()
    def instruct(self):
        self.window.fill((255,255,255))
        myfont = pygame.font.SysFont('Times New Roman', 30)
        textsurface = myfont.render('Instructions: Example instructions...', True, (0, 0, 0))
        self.window.blit(textsurface,(0,0))
