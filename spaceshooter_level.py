import pygame
import random
from controller import *
pygame.init()

class Space(pygame.sprite.Sprite): #spaceship model
    def __init__(self, running = True, isJump = False, jumpCount = 10, x = 50, y = 530):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.running = running
        self.win = pygame.display.set_mode((800,600))
        self.width = 64
        self.height = 64
        self.image = pygame.image.load("Sprites//THEspaceship.png")
        self.background = pygame.image.load("Sprites//space background.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        pygame.mixer.music.load("Sounds//space music.wav")
        pygame.mixer.music.play(-1,0.0)
        self.music = True
        self.speed = 44
        enemy = Enemy(380,380, "Sprites//enemyship.png")
        pygame.display.update()

        while self.running:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                exit()

            if keys[pygame.K_LEFT] and self.x > self.speed:
                self.x -= self.speed

            if keys[pygame.K_RIGHT] and self.x < 819 - self.width - self.speed:
                self.x += self.speed

            '''

            You can probably just get rid of all of this if you don't want the ship moving up and down

            if keys[pygame.K_UP] and self.y < self.speed:   #y < speed and y < 800 - height - speed limits character to only left and right
                self.y -= self.speed

            if keys[pygame.K_DOWN] and self.y < 800 - self.height - self.speed:
                self.y += self.speed
            '''
            if keys[pygame.K_SPACE]:
                self.image.shot()
                active_sprite_list2.add(bullet)
                bullet.shot()
            self.win.blit(self.background, (0,0))
            self.win.blit(self.image, (self.x,self.y))

            enemy.draw(self.win)
            enemy.update()
            pygame.display.flip()

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.enemyship = pygame.transform.scale(self.image, (380,380))
        self.speed = 10

    def update(self):
        self.movex = random.randint(-10,10)
        self.rect.x += self.movex


    def draw(self, win):
        win.blit(self.image, self.rect)




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
