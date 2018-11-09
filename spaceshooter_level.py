import pygame
import random
from controller import *
pygame.init()

class Space: #spaceship model
    def __init__(self, running = True, isJump = False, jumpCount = 10, x = 50, y = 440):
        self.x = x
        self.y = y
        self.running = running
        self.win = pygame.display.set_mode((800,600))
        self.image = pygame.image.load("Sprites//THEspaceship.png")
        self.enemyship = pygame.image.load("Sprites//enemyship.png")
        self.background = pygame.image.load("Sprites//space background.png")
        self.win.blit(self.background, (0,0))
        self.win.blit(self.image, (self.x,self.y))
        self.win.blit(self.enemyship, (50,50))
        self.speed = 5
        pygame.display.update()

        while self.running:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # keys = pygame.key.get_pressed()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

                    if event.key == pygame.K_LEFT: #and x > speed:
                        self.x -= self.speed

                    if event.key == pygame.K_RIGHT: #and x < 500 - width - speed:
                        self.x += self.speed

                    if event.key == pygame.K_UP: #and y > speed:   #y < speed and y < 800 - height - speed limits character to only left and right
                        self.y -= self.speed

                    if event.key == pygame.K_DOWN: #and y < 500 - height - speed:
                        self.y += self.speed

                    if event.key == pygame.K_SPACE:
                        self.image.shot()
                        active_sprite_list2.add(bullet)
                        bullet.shot()
# 
# class Bullet(pygame.sprite.Sprite):
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#         self.damage = 50
#         self.frames_bullet = []
#         sprite_sheet = SpriteSheet("Sprites//bullet.png")
#
#     def update(self):
#
#
#     def shot(self):
#
#     def reset(self):
