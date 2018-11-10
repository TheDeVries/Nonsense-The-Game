import pygame
import random
from controller import *
pygame.init()

class Space(pygame.sprite.Sprite): #spaceship model
    def __init__(self, running = True, isJump = False, jumpCount = 10, x = 50, y = 440):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.running = running
        self.win = pygame.display.set_mode((800,600))
        self.width = 64
        self.height = 64
        self.image = pygame.image.load("Sprites//THEspaceship.png")
        self.enemyship = pygame.image.load("Sprites//enemyship.png")
        self.background = pygame.image.load("Sprites//space background.png")
        self.speed = 44
        pygame.display.update()

        while self.running:
            pygame.time.delay(100)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                exit()

            if keys[pygame.K_LEFT] and x > self.speed:
                self.x -= self.speed

            if keys[pygame.K_RIGHT] and x < 800 - self.width - self.speed:
                self.x += self.speed

            if keys[pygame.K_UP] and y < self.speed:   #y < speed and y < 800 - height - speed limits character to only left and right
                self.y -= self.speed

            if keys[pygame.K_DOWN] and y < 800 - self.height - self.speed:
                self.y += self.speed

            if keys[pygame.K_SPACE]:
                self.image.shot()
                active_sprite_list2.add(bullet)
                bullet.shot()
            self.win.blit(self.background, (0,0))
            self.win.blit(self.image, (self.x,self.y))
            self.win.blit(self.enemyship, (50,50))
            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


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
