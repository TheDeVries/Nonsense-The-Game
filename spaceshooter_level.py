import pygame
import random
pygame.init()
from controller import *

class Space:
    def __init__(self):
        self.image = pygame.image.load("THEspaceship.png")
        self.background = pygame.image.load("space background.png")
        self.running = True
        self.rect.bottom = screen_rect.bottom
        self.rect.centerx = screen_rect.centerx
