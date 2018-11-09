import pygame

class Controller:
    scene = 0
    scenes_done = []
    sanity = 1
    sanity1 = pygame.image.load("Sprites//sanity1.png")
    sanity2 = pygame.image.load("Sprites//sanity2.png")
    sanity3 = pygame.image.load("Sprites//sanity3.png")
    sanity4 = pygame.image.load("Sprites//sanity4.png")
    sanity5 = pygame.image.load("Sprites//sanity5.png")
    score_current = 0
    def __init__(self):
        pygame.init()
        self.running_menu = True
        self.window = pygame.display.set_mode((800,600))
        while self.running_menu:
            if Controller.scene == 0:
                men = Menu()
            elif Controller.scene == 1:
                club = Club()
            elif Controller.scene == 2:
                mazey = Maze()
            elif Controller.scene == 3:
                platform_level = PlatformLevel()
            elif Controller.scene == 4:
                typing = Typing()
            





    def sanity_meter(self, window, color):
        if Controller.sanity == 1:
            window.blit(Controller.sanity1, (0,0))
        elif Controller.sanity == 2:
            window.blit(Controller.sanity2, (0,0))
        elif Controller.sanity == 3:
            window.blit(Controller.sanity3, (0,0))
        elif Controller.sanity == 4:
            window.blit(Controller.sanity4, (0,0))
        elif Controller.sanity == 5:
            window.blit(Controller.sanity5, (0,0))
        myfont = pygame.font.SysFont('Times New Roman', 30)
        textsurface = myfont.render("Insanity:", True, color)
        scores = str(Controller.score_current)
        score_surface = myfont.render(str(Controller.sanity), True, color)
        window.blit(textsurface,(130,0))
        window.blit(score_surface,(235,0))
    def score(self, window, color):
        myfont = pygame.font.SysFont('Times New Roman', 45)
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
