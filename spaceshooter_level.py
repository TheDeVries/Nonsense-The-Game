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
        all_sprites_list = pygame.sprite.Group()
        blasts = pygame.sprite.Group()
        enemies = pygame.sprite.Group()
        hero = Hero("Sprites//THEspaceship.png")
        all_sprites_list.add(hero)
        hero.rect.y = 530
        pygame.display.update()

        for i in range(20):
            enemy = Enemy("Sprites//enemyship.png")
            enemies.add(enemy)
            enemy.rect.x = random.randrange(800)
            enemy.rect.y = random.randrange(350)
            all_sprites_list.add(enemy)


        while self.running:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.win.blit(self.background, (0,0))
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                exit()

            if keys[pygame.K_LEFT]: #and self.x > self.speed:
                hero.move_left()

            if keys[pygame.K_RIGHT]: #and self.x < 819 - self.width - self.speed:
                hero.move_right()

            if keys[pygame.K_SPACE]:
                blast = Blast("Sprites//spacebullet.png")
                blast.rect.x = hero.rect.x
                blast.rect.y = hero.rect.y
                all_sprites_list.add(blast)
                blasts.add(blast)

            # self.win.blit(self.image, (self.x,self.y))

            if keys[pygame.K_p]:
                Controller.scene_selector(self, 1)
                pygame.mixer.music.stop()
                self.toggle = False
                c1 = Controller()

            all_sprites_list.update()
            # hero.draw(self.win)
            # enemy.draw(self.win)
            # enemy.update()
            for blast in blasts:
                enemy_hit_list = pygame.sprite.spritecollide(blast,enemies, True)
                for enemy in enemy_hit_list:
                    print("collision")

                if blast.rect.y < -10:
                    blasts.remove(blast)
                    all_sprites_list.remove(blast)
            all_sprites_list.draw(self.win)
            # all_sprites_list.update()
            pygame.display.flip()

class Hero(pygame.sprite.Sprite):  #spaceship model
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)#.convert()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.width = 64
        self.height = 64
        self.speed = 44

    def move_left(self):
        if self.rect.x > self.speed:
            self.rect.x -= self.speed


    def move_right(self):
        if self.rect.x < 819 - self.width - self.speed:
            self.rect.x += self.speed

    def shoot(self):
        pass

    def draw(self, win):
        win.blit(self.image, self.rect)




class Enemy(pygame.sprite.Sprite):
    def __init__(self,filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)#.convert()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.speed = 10

    def update(self):
        self.movex = random.randint(-10,10)
        self.rect.x += self.movex


    def draw(self, win):
        win.blit(self.image, self.rect)




class Blast(pygame.sprite.Sprite):
    def __init__(self,filename):
        super().__init__()
        self.image = pygame.image.load(filename)#.convert()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.speed = 20
        self.damage = 1
        self.frames_bullet = []


    def update(self):
        self.rect.y -= self.speed
        print(self.rect.y)


    # def shot(self, win):
    #     self.toggle = True
    #     win.blit(self.image,self.rect)

    # def reset(self):

class Explosion:
    pass
