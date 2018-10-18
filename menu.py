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
        self.start_button_unpressed = pygame.image.load("Sprites//start1.png").convert()
        self.start_button_pressed = pygame.image.load("Sprites//start2.png").convert()
        self.instruct_button_unpressed = pygame.image.load("Sprites//instruct1.png").convert()
        self.instruct_button_pressed = pygame.image.load("Sprites//instruct2.png").convert()
        # Method Calls
        self.background()
        self.start()
        self.instructions()
        self.title_pic()

    def background(self):
        '''
           creates random colors in background
        '''
        self.window.fill((50,220,100))
    def title_pic(self):
        '''
           blits title image onto surface
        '''
        self.window.blit(self.title, (200,100))
    def button(self, blit1, blit2, x1, x2, y1, y2, unpressed, pressed):
        """
           method for creating buttons
        """
        unpressed = pygame.transform.scale(unpressed, (126, 60))
        pressed = pygame.transform.scale(pressed, (126, 60))
        self.window.blit(unpressed, (blit1, blit2))
        mouse_posx = pygame.mouse.get_pos()[0]
        mouse_posy = pygame.mouse.get_pos()[1]
        if mouse_posx < x1 and mouse_posx > x2 and mouse_posy > y1 and mouse_posy < y2:
            self.window.blit(pressed, (blit1,blit2))
            return True
    def start(self):
        """
           create and control start button
        """
        y = self.button(100,400,226,100,400,460, self.start_button_unpressed, self.start_button_pressed)
        x = pygame.mouse.get_pressed()
        if x[0] == 1 and y == True:
            print("test complete")
    def instructions(self):
        """
           create and control instructions button and page
        """
        y = self.button(300,400,426,300,400,460, self.instruct_button_unpressed, self.instruct_button_pressed)
        x = pygame.mouse.get_pressed()
        if x[0] == 1 and y == True:
            print("test complete")


    def quit(self):
        pass
    def setting(self):
        pass
# test
