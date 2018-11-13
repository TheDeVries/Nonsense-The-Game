import pygame
import random
from controller import *
pygame.init()

class Club:
    def __init__(self):
        self.running = True
        #Sounds
        self.club_music = pygame.mixer.music.load("Sounds//HOME - Above All.wav")
        pygame.mixer.music.play(loops=-1, start=0.0)

        #Club Setting
        self.window = pygame.display.set_mode((800, 600))
        self.club_background = pygame.image.load("Sprites//club.png").convert()
        self.club_background2 = pygame.image.load("Sprites//club2.png").convert()
        self.bar = pygame.image.load("Sprites//empty_bar.png").convert()
        self.bar.set_colorkey((0,0,64))

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

        self.setting = 1
        self.window.blit(self.club_background, (0,0))
        self.chosens = self.Randomize()

        while self.running == True:

            Controller.score(self, self.window, (255,255,255))
            Controller.insanity_meter(self, self.window, (255,255,255))

            if self.setting == 1:

                for i in range(-1, -len(self.chosens)+2, -1):
                    if self.chosens[i] != "Sprites//bar_server.png":
                        Character(self.chosens[i], self.chosens[i-3], self.setting, self.window)
                self.window.blit(self.bar, (200, 300))
                if self.chosens[5] == "Sprites//bar_server.png":
                    Character(self.chosens[5], self.chosens[2], self.setting, self.window)

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
                        #elif event.key == pygame.K_SPACE:
                            #Club()

                pygame.display.flip()

            elif self.setting == 2:
                '''
                self.bar_man2_front.set_colorkey((255,255,255))
                self.window.blit(self.bar_man2_front, (400, 300))
                self.speech_bubble.set_colorkey((255,255,255))
                self.window.blit(self.speech_bubble, (400, 65))
                self.window.blit(la_up, (105, 64))
                self.window.blit(la_down, (205, 64))
                self.window.blit(la_left, (5, 64))
                self.window.blit(la_right, (305, 64))
                '''
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
        self.characters = ["Sprites//bar_man.png", "Sprites//bar_man2.png", "Sprites//bar_woman.png", "Sprites//bar_woman2.png"]
        self.chosen_characters = []
        for i in range(len(self.positions)):
            if self.positions[i] == (550,200):
                self.chosen_characters.append("Sprites//bar_server.png")
            else:
                self.choice = random.choice(self.characters)
                self.chosen_characters.append(self.choice)
                self.characters.remove(self.choice)

        return self.chosen_characters

#Club Models
class Character(pygame.sprite.Sprite):
    def __init__(self, image, position, setting, window):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255,255,255))
        if setting == 1:
            self.rect.x = 125
            self.rect.y = 250
            self.character = pygame.transform.scale(self.image, (250, 500))
            window.blit(self.character, position)
        else:
            self.rect.x = 400
            self.rect.y = 300
    def clickable(self, setting):
        if setting == 1:
            pass
#Setting 2 Exclusive
class Dialogue(pygame.sprite.Sprite):
    pass

class Arrows(pygame.sprite.Sprite):
    pass
