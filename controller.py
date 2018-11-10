import pygame

class Controller:
    scene = 0
    scenes_done = []
    insanity = 1
    insanity1 = pygame.image.load("Sprites//insanity1.png")
    insanity2 = pygame.image.load("Sprites//insanity2.png")
    insanity3 = pygame.image.load("Sprites//insanity3.png")
    insanity4 = pygame.image.load("Sprites//insanity4.png")
    insanity5 = pygame.image.load("Sprites//insanity5.png")
    score_current = 0
    def __init__(self):
        pygame.init()
        self.running_menu = True
        self.window = pygame.display.set_mode((800,600))
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
        window.blit(textsurface,(130,0))
        window.blit(score_surface,(235,0))
    def score(self, window, color):
        myfont = pygame.font.Font("Sprites//times.ttf", 45)
        textsurface = myfont.render("Score:", True, color)
        scores = str(Controller.score_current)
        score_surface = myfont.render(scores, True, color)
        window.blit(textsurface,(500,0))
        window.blit(score_surface,(600,0))
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
