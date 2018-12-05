import pygame
import random
from controller import *
pygame.init()

class Space(pygame.sprite.Sprite):
    def __init__(self, running = True):
        pygame.sprite.Sprite.__init__(self)
        self.running = running
        self.start_tick = pygame.time.get_ticks()
        self.win = pygame.display.set_mode((800,600))
        self.background = pygame.image.load("Sprites//space background.png")
        if Controller.insanity < 4:
            pygame.mixer.music.load("Sounds//space music.wav")
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(loops=-1)
        else:
            pygame.mixer.music.load("Sounds//Musicbox.wav")
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play(loops=-1)
        self.music = True
        self.score = 0
        self.completions = Controller.done_counter[1]
        self.handler = 0
        self.winner = True
        self.game_over = False
        #self.difficultify()
        difficulty = {0: '005 030', 1: '010 035', 2: '015 060', 3: '020 060', 4: '025 060', 5: '010 30', 6: '015 35', 7: '010 025', 8: '020 050', 9: '025 050', 10: '030 050'}
        diff_str = difficulty[self.completions - self.handler]
        time_limit = int(diff_str[4:])
        all_sprites_list = pygame.sprite.Group()
        heroblasts = pygame.sprite.Group()
        enemyblasts = pygame.sprite.Group()
        enemies = pygame.sprite.Group()
        explosion = pygame.sprite.Group()
        heroship = pygame.sprite.Group()
        hero = Hero("Sprites//THEspaceship.png")
        all_sprites_list.add(hero)
        heroship.add(hero)
        hero.rect.y = 530
        pygame.display.update()
        self.done_explosion = []

        for i in range(5):
            if Controller.insanity < 3:
                enemy = Enemy("Sprites//enemyship.png")
            else:
                enemy = Enemy("Sprites//Stevenmoore.png")

            enemyblast = EnemyBlast("Sprites//enemyblast.png")
            enemies.add(enemy)
            enemy.rect.x = random.randrange(800)
            enemy.rect.y = random.randrange(350)
            all_sprites_list.add(enemy)
            if random.randrange(100):
                enemyblast.rect.x = enemy.rect.x
                enemyblast.rect.y = enemy.rect.y
                all_sprites_list.add(enemyblast)
                enemyblasts.add(enemyblast)
                self.enemyblastsound = pygame.mixer.Sound("Sounds//enemyblastsound.wav")
                self.enemyblastsound.set_volume(1.0)
                self.enemyblastsound.play(loops=0)



        while self.running:
            pygame.time.delay(50)
            for event in pygame.event.get():
                Controller.basic_command(self, event)

            self.win.blit(self.background, (0,0))
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                hero.move_left()

            if keys[pygame.K_RIGHT]:
                hero.move_right()

            if keys[pygame.K_SPACE]:
                heroblast = HeroBlast("Sprites//spacebullet.png")
                heroblast.rect.x = hero.rect.x
                heroblast.rect.y = hero.rect.y
                all_sprites_list.add(heroblast)
                heroblasts.add(heroblast)
                self.heroblastsound = pygame.mixer.Sound("Sounds//Ki blast.wav")
                self.heroblastsound.set_volume(1.0)
                self.heroblastsound.play(loops=0)

            all_sprites_list.update()

            for enemyblast in enemyblasts:  #enemy fire colliding with hero ship
                hero_hit_list = pygame.sprite.spritecollide(enemyblast,heroship, True, pygame.sprite.collide_circle)
                for hero_coord in hero_hit_list:
                    x = hero_coord.rect.x
                    y = hero_coord.rect.y
                    explode = Explosion(x,y)
                    explosion.add(explode)
                    self.done_explosion.append(explode)
                    # if Controller.insanity < 3:
                    self.explosionsound = pygame.mixer.Sound("Sounds//explosoundeffect.wav")
                    self.explosionsound.set_volume(0.5)
                    self.explosionsound.play(loops=0)
                    self.game_over = True

            for heroblast in heroblasts: #hero fire colliding with enemy ships
                enemy_hit_list = pygame.sprite.spritecollide(heroblast,enemies, True, pygame.sprite.collide_circle)
                for enemy_coord in enemy_hit_list:
                    self.score += 1
                    heroblasts.remove(heroblast)
                    all_sprites_list.remove(heroblast)
                    x = enemy_coord.rect.x
                    y = enemy_coord.rect.y
                    explode = Explosion(x,y)
                    explosion.add(explode)
                    self.done_explosion.append(explode)
                    # if Controller.insanity < 3:
                    self.explosionsound = pygame.mixer.Sound("Sounds//explosoundeffect.wav")
                    self.explosionsound.set_volume(0.5)
                    self.explosionsound.play(loops=0)
                    print(self.score)
                    print(enemies)

                if heroblast.rect.y < -10:
                    heroblasts.remove(heroblast)
                    all_sprites_list.remove(heroblast)

            for done in range(len(self.done_explosion)):
                if self.done_explosion[done].done == True:
                    explosion.remove(self.done_explosion[done])
                    self.done_explosion.remove(self.done_explosion[done])
                    break




            if len(enemies) == 0:
                myfont = pygame.font.SysFont(None,30)
                message = myfont.render("YOU WIN!! Press TAB to continue", False, (255,255,255))
                self.win.blit(message, (255,255))
                # pygame.mixer.music.pause()
                # # self.victorytheme = pygame.mixer.music.load("Sounds//Victoryscreentheme.wav")
                # # pygame.mixer.music.play(loops=-1)
                pygame.display.flip()
                if keys[pygame.K_TAB]:
                    Controller.transition(self,1,True)


            elif len(heroship) == 0:

                myfont = pygame.font.SysFont(None,30)
                message = myfont.render("Game Over!! Press TAB to continue", False, (255,255,255))
                self.win.blit(message, (255,255))
                pygame.display.flip()
                if keys[pygame.K_TAB]:
                    Controller.transition(self,1,False)


            # print(enemies.has(enemy))         #victory things (OPTIONAL)
            # if enemies.has(enemy) == False:
            #     pygame.mixer.music.pause()
            #     self.victorytheme = pygame.mixer.music.load("Sounds//Victoryscreentheme.wav")
            #     pygame.mixer.music.play(loops=0)




            explosion.draw(self.win)
            explosion.update()
            all_sprites_list.draw(self.win)
            Controller.score(self, self.win, (255,255,255))
            Controller.insanity_meter(self, self.win, (255,255,255))
            Controller.clock(self, self.win, (240, 93, 93), time_limit, self.start_tick)
            if self.score == 20:
                Controller.done_counter[1]
            # all_sprites_list.update()
            pygame.display.flip()

    # def difficultify(self):         #must fix
    #     dif = Controller.done_counter[1]
    #     if dif % 2 == 0 and dif !=0:
    #         self.speed += 20

class Hero(pygame.sprite.Sprite):  #spaceship model
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.radius = 20
        BLUE = (0,0,255)
        # pygame.draw.circle(self.image,BLUE, self.rect.center,self.radius)
        self.width = 64
        self.height = 64
        self.speed = 44

    def move_left(self):
        if Controller.insanity < 2:
            if self.rect.x >= self.speed:
                self.rect.x -= self.speed
        else:
            if self.rect.x < 819 - self.width - self.speed:
                self.rect.x += self.speed


    def move_right(self):
        if Controller.insanity < 2:
            if self.rect.x < 819 - self.width - self.speed:
                self.rect.x += self.speed
        else:
            if self.rect.x >= self.speed:
                self.rect.x -= self.speed

    def draw(self, win):
        win.blit(self.image, self.rect)




class Enemy(pygame.sprite.Sprite):
    def __init__(self,filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.radius = 20
        BLUE = (0,0,255)
        # pygame.draw.circle(self.image,BLUE, self.rect.center,self.radius)
        self.speed = 10
        print(self.speed)

    def update(self):
        self.movex = random.randint(-self.speed, self.speed)
        if self.rect.x + self.movex > 0 and self.rect.x + self.movex + 20 < 800:
            self.rect.x += self.movex
        else:
            self.rect.x -= self.movex


    def draw(self, win):
        win.blit(self.image, self.rect)




class HeroBlast(pygame.sprite.Sprite):
    def __init__(self,filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.radius = 10
        BLUE = (0,0,255)
        # pygame.draw.circle(self.image,BLUE, self.rect.center,self.radius)
        self.speed = 30
        self.damage = 1
        self.frames_bullet = []


    def update(self):
        self.rect.y -= self.speed
        #print(self.rect.y)



class EnemyBlast(pygame.sprite.Sprite):
    def __init__(self,filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.radius = 10
        BLUE = (0,0,255)
        #pygame.draw.circle(self.image,BLUE, self.rect.center,self.radius)
        self.speed = 30
        self.damage = 1
        self.frames_bullet = []


    def update(self):
        self.rect.y += self.speed
        #print(self.rect.y)

class Explosion(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("Sprites//explosion.png")
        self.frames = []
        self.x = x
        self.y = y
        color_key_player = (0,0,0)
        for x1 in range(0,801,100):
            image = sprite_sheet.get_image(x1, 0, 100, 100, color_key_player)
            self.frames.append(image)
        for x2 in range(0,801,100):
            image = sprite_sheet.get_image(x2, 100, 100, 100, color_key_player)
            self.frames.append(image)
        for x3 in range(0,801,100):
            image = sprite_sheet.get_image(x3, 200, 100, 100, color_key_player)
            self.frames.append(image)
        for x4 in range(0,801,100):
            image = sprite_sheet.get_image(x4, 300, 100, 100, color_key_player)
            self.frames.append(image)
        for x5 in range(0,801,100):
            image = sprite_sheet.get_image(x5, 400, 100, 100, color_key_player)
            self.frames.append(image)
        for x6 in range(0,801,100):
            image = sprite_sheet.get_image(x6, 500, 100, 100, color_key_player)
            self.frames.append(image)
        for x7 in range(0,801,100):
            image = sprite_sheet.get_image(x7, 600, 100, 100, color_key_player)
            self.frames.append(image)
        for x8 in range(0,801,100):
            image = sprite_sheet.get_image(x8, 700, 100, 100, color_key_player)
            self.frames.append(image)
        for x9 in range(0,801,100):
            image = sprite_sheet.get_image(x9, 800, 100, 100, color_key_player)
            self.frames.append(image)
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x,self.y)
        self.frame = 0
        self.done = False
    def update(self):
        self.frame += 4
        if self.frame >= 81:
            self.frame = 0
            self.done = True
        self.image = self.frames[self.frame]

    def reset(self):
        self.done = False
