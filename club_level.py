import pygame
import random
from controller import *
pygame.init()

class Club:
    def __init__(self):
        self.start_tick = pygame.time.get_ticks()
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
        active_sprite_list = pygame.sprite.Group()

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
            Controller.clock(self, self.window, 1, 30, self.start_tick)

            if self.setting == 1:

                for i in range(-1, -len(self.chosens)+2, -1):
                    if self.chosens[i] != "Sprites//bar_server.png":
                        sprite = Character(self.chosens[i], self.chosens[i-3], self.setting, self.window)
                self.window.blit(self.bar, (200, 300))
                if self.chosens[5] == "Sprites//bar_server.png":
                    sprite = Character(self.chosens[5], self.chosens[2], self.setting, self.window)
            elif self.setting == 2:

                Character("Sprites//bar_server_front.png", (400, 300), self.setting, self.window)
                self.speech_bubble.set_colorkey((255,255,255))
                self.window.blit(self.speech_bubble, (400, 65))
                self.window.blit(la_up, (105, 64))
                self.window.blit(la_down, (205, 64))
                self.window.blit(la_left, (5, 64))
                self.window.blit(la_right, (305, 64))

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
                    if event.key == pygame.K_SPACE:
                        Club()
                    if event.key == pygame.K_p:
                        Controller.scene_selector(self, 3)
                        pygame.mixer.music.stop()
                        self.toggle = False
                        c1 = Controller()
                # Mouseclick
                if event.type == pygame.MOUSEBUTTONDOWN and self.setting == 1:
                    clicked_pos = pygame.mouse.get_pos()
                    sprite2 = pygame.sprite.Sprite()
                    self.rect2 = pygame.Rect((clicked_pos), (30, 30))
                    pygame.draw.rect(self.window, (255,255,255), [(clicked_pos), (30, 30)])
                    sprite2.rect = self.rect2
                    print(sprite)
                    print(sprite2)
                    if pygame.sprite.collide_rect(sprite, sprite2) == True:
                        self.window.blit(self.club_background2, (0,0))
                        self.setting = 2

            pygame.display.flip()

    def Randomize(self):
        '''
        Returns a list where the first three items are position tuples randomly picked from five possible options
        and the last three items are sprite strings that match with the position three indexes prior.
        Example: (pos1, pos2, pos3, sprite1, sprite2, sprite3)
        '''
        self.chosens = []
        self.positions = self.rand_positions()
        self.characters = self.rand_characters(self.positions)
        self.chosens = self.positions + self.characters
        return self.chosens

    def rand_positions(self):
        '''
        Removes two of the possible character blit positions leaving the three chosen positions to return
        '''
        self.positions = [(200, 210), (325, 150), (450, 90), (575, 30), (550, 200)]
        for i in range(2):
            self.choice = random.choice(self.positions)
            self.positions.remove(self.choice)
        return self.positions

    def rand_characters(self, positions):
        '''
        Takes positions as paramter and selects characters to return based on those positions
        This is mostly randomized except when the bar_server position is selected and this sprite is confirmed
        to be a part of the returned list of chosen characters.
        '''
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

# Club Models
class Character(pygame.sprite.Sprite):
    def __init__(self, file, position, setting, window):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255,255,255))
        if setting == 1:
            self.rect.x = 250
            self.rect.y = 500
            self.character = pygame.transform.scale(self.image, (250, 500))
            window.blit(self.character, position)
        else:
            self.rect.x = 400
            self.rect.y = 300
            self.character = self.image
            window.blit(self.character, position)
    def getRect(self):
        return self.rect
# Setting 2 Exclusive
class Dialogue:
    def __init__(self, position, window):
        myfont = pygame.font.Font("Sprites//times.ttf", 45)

class Arrows(pygame.sprite.Sprite):
    pass
