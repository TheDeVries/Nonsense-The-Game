import pygame
import time
import random
class Menu:
    def __init__(self):
        '''
           inits the menu
        '''
        init = pygame.init()
        self.window = pygame.display.set_mode((800,600))
        self.title = pygame.image.load("Sprites//titlecard.png").convert()
        self.start_button_unpressed = pygame.image.load("Pictures//start1.png").convert()
        self.start_button_pressed = pygame.image.load("Pictures//start2.png").convert()
        # Method Calls
        self.randomize()
        self.start_button()
        self.title_pic()

    def randomize(self):
        '''
           creates random colors in background
        '''
        x = random.randint(0, 255)
        x1 = random.randint(0, 255)
        x2 = random.randint(0, 255)
        self.window.fill((x,x1,x2))
    def title_pic(self):
        '''
           blits title image onto surface
        '''
        self.window.blit(self.title, (200,100))
    def start_button(self):
        self.start_button_pressed = pygame.transform.scale(self.start_button_pressed, (126, 60))
        self.window.blit(self.start_button_pressed, (100,400))



    def instructions(self):
        pass
    def quit(self):
        pass
    def setting(self):
        pass
# test
