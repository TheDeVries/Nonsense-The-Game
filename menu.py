import pygame
import time
import random
class Menu:
    def __init__(self):
        init = pygame.init()
        self.window = pygame.display.set_mode((800,600))
        self.title = pygame.image.load("Sprites//titlecard.png").convert()
        self.randomize()
        self.start_button()
        self.title_pic()

    def randomize(self):
        x = random.randint(0, 255)
        x1 = random.randint(0, 255)
        x2 = random.randint(0, 255)
        self.window.fill((x,x1,x2))
    def title_pic(self):
        self.window.blit(self.title, (200,100))



    def start_button(self):
        pass



    def instructions(self):
        pass
    def quit(self):
        pass
    def setting(self):
        pass
# test
