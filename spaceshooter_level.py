import pygame
import random
from controller import *
pygame.init()

class Space(pygame.sprite.Sprite):
    def __init__(self, running = True):
        pygame.sprite.Sprite.__init__(self)
        self.running = running
        self.win = pygame.display.set_mode((800,600))
        self.background = pygame.image.load("Sprites//space background.png")
        # pygame.mixer.music.load("Sounds//space music.wav")
        # pygame.mixer.music.play(-1,0.0)
        self.music = True
        hero = Hero(50,530, "Sprites//THEspaceship.png")
        enemy = Enemy(0,0, "Sprites//enemyship.png")
        pygame.display.update()

        while self.running:
            pygame.time.delay(100)
            for event in pygame.event.get():
                Controller.basic_command(self, event)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                exit()

<<<<<<< HEAD
            if keys[pygame.K_LEFT]: #and self.x > self.speed:
                hero.move_left()

            if keys[pygame.K_RIGHT]: #and self.x < 819 - self.width - self.speed:
                hero.move_right()

=======
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
>>>>>>> c1752017361090d876806d4423af63c3b0f0365c
            if keys[pygame.K_SPACE]:
                self.image.shot()
                active_sprite_list2.add(bullet)
                bullet.shot()
            self.win.blit(self.background, (0,0))
<<<<<<< HEAD
            # self.win.blit(self.image, (self.x,self.y))

            if keys[pygame.K_p]:
                Controller.scene_selector(self, 1)
                pygame.mixer.music.stop()
                self.toggle = False
                c1 = Controller()
            hero.draw(self.win)
=======
            self.win.blit(self.image, (self.x,self.y))
>>>>>>> c1752017361090d876806d4423af63c3b0f0365c
            enemy.draw(self.win)
            enemy.update()
            pygame.display.flip()

class Hero(pygame.sprite.Sprite):  #spaceship model
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = 64
        self.height = 64
        self.heroship = pygame.transform.scale(self.image, (50,50))
        self.speed = 44

    def move_left(self):
        if self.rect.x > self.speed:
            self.rect.x -= self.speed


    def move_right(self):
        if self.rect.x < 819 - self.width - self.speed:
            self.rect.x += self.speed


    def draw(self, win):
        win.blit(self.image, self.rect)




class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.enemyship = pygame.transform.scale(self.image, (380,380))
        self.speed = 10

    def update(self):
        self.movex = random.randint(-10,10)
        self.rect.x += self.movex


    def draw(self, win):
        win.blit(self.image, self.rect)


Space()

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
#     def reset(self)
