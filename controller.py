import pygame
import random

class Controller:
    scene = 0
    insanity = 1
    insanity1 = pygame.image.load("Sprites//insanity1.png")
    insanity2 = pygame.image.load("Sprites//insanity2.png")
    insanity3 = pygame.image.load("Sprites//insanity3.png")
    insanity4 = pygame.image.load("Sprites//insanity4.png")
    insanity5 = pygame.image.load("Sprites//insanity5.png")
    if scene == 0:
        spa = 0
        maz = 0
        clu = 0
        pla = 0
        typ = 0
    done_counter = {1: spa,  2: maz, 3: clu, 4: pla, 5: typ}
    score_current = 0
    scenes_done = []
    def __init__(self):
        pygame.init()
        self.running_menu = True
        self.window = pygame.display.set_mode((800,600))
        pygame.display.set_icon(pygame.image.load("Sprites//eyecon.png"))
        while self.running_menu:
            if Controller.scene == 0:
                men = Menu()
            elif Controller.scene == 1:
                space = Space()
            elif Controller.scene == 2:
                maze = Maze()
            elif Controller.scene == 3:
                club = Club()
            elif Controller.scene == 4:
                platformer = Platformer()
            elif Controller.scene == 5:
                typing = Typing()
    def scene_selector(self, scene_finished):
        Controller.done_counter[scene_finished] += 1
        print(Controller.done_counter[scene_finished])
        if Controller.insanity == 1:
            self.complete = pygame.mixer.Sound("Sounds//Electronic_Chime.wav")
            self.complete.set_volume(0.3)
        else:
            self.complete = pygame.mixer.Sound("Sounds//switch.wav")
        self.complete.play(loops = 0)
        Controller.scenes_done.append(scene_finished)
        Controller.score_current += 1
        rand = random.randrange(0,101)
        if rand < 20:
            if Controller.scene != 1:
                Controller.scene = 1
                Controller.scenes_done.append(1)
            elif Controller.scene == 1:
                rand = random.randrange(0,101)
                if rand < 15:
                    Controller.scene = 1
        elif rand > 20 and rand < 40:
            if Controller.scene != 2:
                Controller.scene = 2
                Controller.scenes_done.append(2)
            elif Controller.scene == 2:
                rand = random.randrange(0,101)
                if rand < 15:
                    Controller.scene = 2
        elif rand > 40 and rand < 60:
            if Controller.scene != 3:
                Controller.scene = 3
                Controller.scenes_done.append(3)
            elif Controller.scene == 3:
                rand = random.randrange(0,101)
                if rand < 15:
                    Controller.scene = 3
        elif rand > 60 and rand < 80:
            if Controller.scene != 4:
                Controller.scene = 4
                Controller.scenes_done.append(4)
            elif Controller.scene == 4:
                rand = random.randrange(0,101)
                if rand < 15:
                    Controller.scene = 4
        elif rand > 80 and rand < 100:
            if Controller.scene != 5:
                Controller.scene = 5
                Controller.scenes_done.append(5)
            elif Controller.scene == 5:
                rand = random.randrange(0,101)
                if rand < 15:
                    Controller.scene = 5

    def insanity_meter(self, window, color):
        if Controller.insanity == 1:
            window.blit(Controller.insanity1, (0,0))
        elif Controller.insanity == 2:
            window.blit(Controller.insanity2, (0,0))
        elif Controller.insanity == 3:
            window.blit(Controller.insanity3, (0,0))
        elif Controller.insanity == 4:
            window.blit(Controller.insanity4, (0,0))
        elif Controller.insanity == 5:
            window.blit(Controller.insanity5, (0,0))
        myfont = pygame.font.Font("Sprites//times.ttf", 30)
        textsurface = myfont.render("Insanity:", True, color)
        scores = str(Controller.score_current)
        score_surface = myfont.render(str(Controller.insanity), True, color)
        window.blit(textsurface,(0,18))
        window.blit(score_surface,(105,18))
    def score(self, window, color):
        myfont = pygame.font.Font("Sprites//times.ttf", 45)
        textsurface = myfont.render("Score:", True, color)
        scores = str(Controller.score_current)
        score_surface = myfont.render(scores, True, color)
        if Controller.score_current < 10:
            window.blit(textsurface,(650,0))
            window.blit(score_surface,(775,0))
        else:
            window.blit(textsurface, (625, 0))
            window.blit(score_surface, (750, 0))
    def clock(self, window, color, amount, former_time):
        myfont = pygame.font.Font("Sprites//digital-7.ttf", 60)
        self.time = int((amount - (pygame.time.get_ticks() - former_time)/1000))
        num_sec = int(self.time % 60)
        num_min = self.time // 60
        if self.time < 10:
            strtimer = "0" + str(num_min) + ":" + "0" + str(num_sec)
        else:
            if num_sec < 10:
                strtimer = "0" + str(num_min) + ":0" + str(num_sec)
            else:
                strtimer = "0" + str(num_min) + ":" + str(num_sec)
        clocktimer = myfont.render(strtimer, True, color)
        if Controller.score_current < 10:
            window.blit(clocktimer, (322, 3))
        else:
            window.blit(clocktimer, (297, 3))

class SpriteSheet(object):

    def __init__(self, file_name):

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()


    def get_image(self, x, y, width, height, color_key):

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming pink works as the transparent color
        image.set_colorkey((color_key))

        # Return the image
        return image


from club_level import *
from typing_level import *
from main_menu import *
from maze_level import *
from platform_level import *
from spaceshooter_level import *
