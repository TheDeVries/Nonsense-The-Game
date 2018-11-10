import pygame
import random
from controller import *
pygame.init()

class Club:
    def __init__(self):
        self.running = True
        #Club & Characters
        self.window = pygame.display.set_mode((800, 600))
        self.club_background = pygame.image.load("Sprites//club.png").convert()
        self.club_background2 = pygame.image.load("Sprites//club2.png").convert()
        self.bar = pygame.image.load("Sprites//empty_bar.png").convert()
        self.bar_woman = pygame.image.load("Sprites//bar_woman.png").convert()
        self.bar_woman_front = pygame.image.load("Sprites//bar_woman_front.png").convert()
        self.bar_woman2 = pygame.image.load("Sprites//bar_woman2.png").convert()
        self.bar_woman2_front = pygame.image.load("Sprites//bar_woman2_front.png").convert()
        self.bar_man = pygame.image.load("Sprites//bar_man.png").convert()
        self.bar_man_front = pygame.image.load("Sprites//bar_man_front.png").convert()
        self.bar_man2 = pygame.image.load("Sprites//bar_man2.png").convert()
        self.bar_man2_front = pygame.image.load("Sprites//bar_man2_front.png").convert()
        self.bar_server = pygame.image.load("Sprites//bar_server.png").convert()
        self.bar_server_front = pygame.image.load("Sprites//bar_server_front.png").convert()

        #Keyboard DDR Setting
        self.speech_bubble = pygame.image.load("Sprites//speech_bubble.png").convert()
        self.arrow = pygame.image.load("Sprites//arrow.png").convert()
        self.arrow_orange = pygame.image.load("Sprites//arrow_orange.png").convert()

        self.arrow.set_colorkey((255,255,255))
        arrow_left = self.arrow
        arrow_up = pygame.transform.rotate(self.arrow, 270)
        arrow_down = pygame.transform.rotate(self.arrow, 90)
        arrow_right = pygame.transform.rotate(self.arrow, 180)
        la_left = self.arrow_orange
        la_up = pygame.transform.rotate(self.arrow_orange, 270)
        la_down = pygame.transform.rotate(self.arrow_orange, 90)
        la_right = pygame.transform.rotate(self.arrow_orange, 180)

        self.window.blit(self.club_background2, (0,0))
        #Must find way to randomize positions and put reliabe buttons at those positions.
        '''
        self.chosens = self.Randomize()
        '''
        while self.running == True:

            Controller.score(self, self.window, (255,255,255))
            Controller.insanity_meter(self, self.window, (255,255,255))

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
            '''
            if self.chosens[5] == self.bar_server:
                pass
            else:
                self.chosens[5].set_colorkey((255,255,255))
                self.chosens[5] = pygame.transform.scale(self.chosens[5], (250, 500))
                self.window.blit(self.chosens[5], self.chosens[2])
            self.chosens[4].set_colorkey((255,255,255))
            self.chosens[4] = pygame.transform.scale(self.chosens[4], (250, 500))
            self.window.blit(self.chosens[4], self.chosens[1])
            self.chosens[3].set_colorkey((255,255,255))
            self.chosens[3] = pygame.transform.scale(self.chosens[3], (250, 500))
            self.window.blit(self.chosens[3], self.chosens[0])
            self.bar.set_colorkey((0,0,64))
            self.window.blit(self.bar, (200, 300))
            if self.chosens[5] == self.bar_server:
                self.chosens[5].set_colorkey((255,255,255))
                self.bar_server2 = pygame.transform.scale(self.chosens[5], (250, 500))
                self.window.blit(self.bar_server2, (550, 200))
            '''

            self.bar_man2_front.set_colorkey((255,255,255))
            self.window.blit(self.bar_man2_front, (400, 300))
            self.speech_bubble.set_colorkey((255,255,255))
            self.window.blit(self.speech_bubble, (400, 65))
            self.window.blit(la_up, (105, 64))
            self.window.blit(la_down, (205, 64))
            self.window.blit(la_left, (5, 64))
            self.window.blit(la_right, (305, 64))

            Controller.insanity_meter(self, self.window, (255,255,255))
            pygame.display.flip()

    def Randomize(self):
        self.chosens = []
        self.positions = self.rand_positions()
        self.characters = self.rand_characters(self.positions)
        self.chosens = self.positions + self.characters
        return self.chosens

    def rand_positions(self):
        self.positions = [(200, 210), (325, 150), (450, 90), (575, 30), (550, 200)]
        for i in range(2):
            self.choice = random.choice(self.positions)
            self.positions.remove(self.choice)
        return self.positions

    def rand_characters(self, positions):
        self.characters = [self.bar_man, self.bar_man2, self.bar_woman, self.bar_woman2]
        self.chosen_characters = []
        for i in range(len(self.positions)):
            if self.positions[i] == (550,200):
                self.chosen_characters.append(self.bar_server)
            else:
                self.choice = random.choice(self.characters)
                self.chosen_characters.append(self.choice)
                self.characters.remove(self.choice)

        return self.chosen_characters

#Club Models
class Arrows(pygame.Sprite.sprite):
    pass
class Characters(pygame.Sprite.sprite):
    pass
class Dialogue(pygame.Sprite.sprite):
    pass
