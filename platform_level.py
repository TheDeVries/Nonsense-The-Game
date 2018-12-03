import pygame
from controller import *

class Platformer:
    x_camera = 0
    y_camera = 0
    player_fall = True
    ground = False
    direction = "L"
    gravity = False
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800,600))
        self.background = pygame.image.load("Sprites//galaxy2.png")
        self.death = pygame.image.load("Sprites//Player_Death.png")
        self.rect = self.background.get_rect()
        self.rect.move_ip((0,0))
        self.window.fill((255,255,255))
        self.running = True
        self.posx = 400-18
        self.posy = 300-22
        self.game_over = False
        player = Player_Platform()
        bullet = Fireball()
        death = Player_Death()
        self.player_death_group = pygame.sprite.Group()
        self.player_death_group.add(death)
        self.player_group = pygame.sprite.Group()
        self.player_group.add(player)
        self.enemies = pygame.sprite.Group()
        self.laser_group = pygame.sprite.Group()
        self.player_fireball = pygame.sprite.Group()
        self.enemy_coords = [0,0,
                             100,100]
        self.laser_coord = [45,50,
                            145,150]
        self.enemy = ""
        self.enemy_list = []
        self.laser_list = []
        for enemies in range(0, 4, 2):
            enemy = Enemy(self.enemy_coords[enemies], self.enemy_coords[enemies+1])
            self.enemy_list.append(enemy)
            self.enemies.add(enemy)
        for laser_iter in range (0,4,2):
            laser = Laser(self.laser_coord[laser_iter], self.laser_coord[laser_iter+1])
            self.laser_list.append(laser)
            self.laser_group.add(laser)
        while self.running:
            for event in pygame.event.get():
                # Quit button
                Controller.basic_command(self, event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player.go_left()

                    if event.key == pygame.K_d:
                        player.go_right()
                    if event.key == pygame.K_LEFT:
                        player.go_left()
                    if event.key == pygame.K_RIGHT:
                        player.go_right()
                    if event.key == pygame.K_LSHIFT:
                        if Platformer.direction == "L":
                            player.shot()
                            self.player_fireball.add(bullet)
                            bullet.shot_left()
                        elif Platformer.direction == "R":
                            player.shot()
                            self.player_fireball.add(bullet)
                            bullet.shot_right()
                    if event.key == pygame.K_SPACE:
                        player.jump_method()
                elif event.type == pygame.KEYUP:
                    if event.key != pygame.K_SPACE:
                        player.stop()
            self.window.blit(self.background, (0, 0))
            player.gravity()
            Platforms = Platforms_Map(self.window)
            Platforms.platforms(player)
            for enemy_movement in self.enemy_list:
                enemy_movement.camera_follow()
            if pygame.sprite.groupcollide(self.player_group, self.enemies, False, False):
                self.running = False
                self.game_over = True
            for laser_direction in range(0,len(self.laser_list)):
                if self.enemy_list[laser_direction].rect.x < player.rect.x:
                    if self.laser_list[laser_direction].progress == 0:
                        self.laser_list[laser_direction].shot_right()
                elif self.enemy_list[laser_direction].rect.x > player.rect.x:
                    if self.laser_list[laser_direction].progress == 0:
                        self.laser_list[laser_direction].shot_left()
            for laser_done in range(0,len(self.laser_list)):
                if self.laser_list[laser_done].done == True:
                    self.laser_group.empty()
            for laser_iter in range(0,len(self.laser_list)):
                self.laser_group.add(self.laser_list[laser_iter])
            if pygame.sprite.groupcollide(self.player_group, self.laser_group, False, False):
                self.running = False
                self.game_over = True
            for enemy_death in range(0, len(self.enemy_list)):
                if pygame.sprite.collide_rect(self.enemy_list[enemy_death], bullet):
                    self.enemies.remove(self.enemy_list[enemy_death])
                    self.enemy_list.remove(self.enemy_list[enemy_death])
                    self.laser_group.remove(self.laser_list[enemy_death])
                    self.laser_list.remove(self.laser_list[enemy_death])
                    #laser_direction.done = False
            self.player_group.update()
            self.player_group.draw(self.window)
            self.enemies.update()
            self.enemies.draw(self.window)
            self.laser_group.update()
            self.laser_group.draw(self.window)
            self.player_fireball.update()
            self.player_fireball.draw(self.window)
            if bullet.done == True:
                self.player_fireball.remove(bullet)
                bullet.done = False
            pygame.display.flip()
            print(self.laser_list)
            print(self.laser_group)
        while self.game_over:
            for event in pygame.event.get():
                # Quit button
                Controller.basic_command(self, event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Controller.scene_selector(self,4,False)
            self.window.blit(self.background, (0, 0))
            self.player_death_group.update()
            self.player_death_group.draw(self.window)
            pygame.display.flip()


class Platforms_Map:
    def __init__(self,window):
        self.running = True
        self.window = window
        self.platformrect_list = []
        self.platform_collide_list = []

    def platforms(self,player):
        self.platform_list = [(0,500 - Platformer.y_camera ,800,400),
                            (200 - Platformer.x_camera,300 - Platformer.y_camera ,200,20),
                            (300 - Platformer.x_camera, 200 - Platformer.y_camera ,200,20),
                            (350 - Platformer.x_camera, 100 - Platformer.y_camera ,200,20),
                            (300 - Platformer.x_camera, 0 - Platformer.y_camera ,200,20)]
        for platform in self.platform_list:
            rect = pygame.draw.rect(self.window, (255,255,255), pygame.Rect(platform))
            self.platformrect_list.append(rect)
        for platformrect in range(0,5):
            if self.platformrect_list[platformrect].colliderect(player):
                self.platform_collide_list.append(self.platformrect_list[platformrect])
                Platformer.ground = True
                Platformer.player_fall = False
            else:
                Platformer.player_fall = True
        for collide in self.platform_collide_list:
            if collide.colliderect(player):
                Platformer.ground = True
                Platformer.player_fall = False
            else:
                Platformer.player_fall = True
                self.platform_collide_list.remove(collide)
        if Platformer.y_camera >= 160:
            Platformer.player_fall = False







class Player_Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_change = 0
        self.y_change = 0
        self.health = 100
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_f = []
        self.jumping_frames_l = []
        self.jumping_frames_r = []
        self.shooting = []

        self.direction = "F"
        sprite_sheet = SpriteSheet("Sprites//stickman.png")
        sprite_sheet_shot = SpriteSheet("Sprites//Player_Shot.png")
        sprite_sheet_jump = SpriteSheet("Sprites//Platformer_jump.png")

        color_key_player = (255,255,255,255)
        image = sprite_sheet_jump.get_image(0, 223, 180, 223, color_key_player)
        image = pygame.transform.scale(image, (36,44))
        self.jumping_frames_l.append(image)
        image = sprite_sheet_jump.get_image(180, 0, 180, 223, color_key_player)
        image = pygame.transform.scale(image, (36,44))
        self.jumping_frames_l.append(image)
        image = sprite_sheet_jump.get_image(0, 0, 180, 223, color_key_player)
        image = pygame.transform.scale(image, (36,44))
        self.jumping_frames_r.append(image)
        image = sprite_sheet_jump.get_image(180, 223, 180, 223, color_key_player)
        image = pygame.transform.scale(image, (36,44))
        self.jumping_frames_r.append(image)

        image = sprite_sheet.get_image(0, 0, 180, 221, color_key_player)
        image = pygame.transform.scale(image, (36,44))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(180, 0, 180, 221, color_key_player)
        image = pygame.transform.scale(image, (36,44))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(360, 0, 180, 221, color_key_player)
        image = pygame.transform.scale(image, (36,44))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 221, 180, 221, color_key_player)
        image = pygame.transform.scale(image, (36,44))
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(180, 221, 180, 221, color_key_player)
        image = pygame.transform.scale(image, (36,44))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(360, 221, 180, 221, color_key_player)
        image = pygame.transform.scale(image, (36,44))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 442, 180, 221, color_key_player)
        image = pygame.transform.scale(image, (36,44))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(180, 442, 180, 221, color_key_player)
        image = pygame.transform.scale(image, (36,44))
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(360, 442, 180, 221, color_key_player)
        image = pygame.transform.scale(image, (36,44))
        self.walking_frames_f.append(image)

        image = sprite_sheet_shot.get_image(0, 0, 180, 239, color_key_player)
        image = pygame.transform.scale(image, (36,45))
        self.shooting.append(image)





        # Set the image the player starts with
        self.image = self.walking_frames_f[0]
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.move_ip(400,300)
        self.frame = 0
        self.frame_right = 0
        self.shot_frame = 0
        self.shot_frame_l = 0
        self.time = 0
        self.move = False
        self.jump = 0
        self.mass = 5
        self.velocity = 3
        self.jump = True
        self.jump_height = 0

    def update(self):

        # Move left/right
        if self.direction == "R":
            self.time += 1
            if self.time % 3 == 0:
                self.frame += 1
                if self.frame > 3:
                    self.frame = 0
                    self.image = self.walking_frames_r[self.frame]
                self.image = self.walking_frames_r[self.frame]
            Platformer.x_camera += 5
            if Platformer.player_fall == True:
                Platformer.y_camera += 5
            Platformer.direction = "R"

        elif self.direction == "L":
            self.time += 1
            if self.time % 3 == 0:
                self.frame_right += 1
                if self.frame_right > 3:
                    self.frame_right = 0
                    self.image = self.walking_frames_l[self.frame_right]
                self.image = self.walking_frames_l[self.frame_right]
            Platformer.x_camera -= 5
            if Platformer.player_fall == True:
                Platformer.y_camera += 5
            Platformer.direction = "L"
        elif self.direction == "S":
            self.image = self.shooting[0]
        elif self.direction == "JR":
            Platformer.direction = "R"
            if self.jump_height < 50:
                self.jump_height += 1
                Platformer.y_camera -= 10
                Platformer.x_camera += 5
                self.image = self.jumping_frames_r[0]
                Platformer.ground = False
                Platformer.gravity = False
            if self.jump_height >= 50:
                self.jump_height += 1
                Platformer.x_camera += 5
                self.image = self.jumping_frames_r[1]
                Platformer.gravity = True
            if Platformer.player_fall == False:
                self.jump_height = 0

        elif self.direction == "JL":
            Platformer.direction = "L"
            if self.jump_height < 50:
                self.jump_height += 1
                Platformer.y_camera -= 10
                Platformer.x_camera -= 5
                self.image = self.jumping_frames_l[0]
                Platformer.ground = False
                Platformer.gravity = False
            if self.jump_height >= 50:
                self.jump_height += 1
                Platformer.x_camera -= 5
                self.image = self.jumping_frames_l[1]
                Platformer.gravity = True
            if Platformer.player_fall == False:
                self.jump_height = 0
        elif self.direction == "JF":
            if self.jump_height < 50:
                self.jump_height += 1
                Platformer.y_camera -= 10
                Platformer.ground = False
                Platformer.gravity = False
            if self.jump_height >= 50:
                self.jump_height += 1
                Platformer.gravity = True
            if Platformer.player_fall == False:
                self.jump_height = 0


















    # Player-controlled movement:
    def go_left(self):
        self.direction = "L"


    def go_right(self):
        self.direction = "R"


    def stop(self):
        self.direction = "F"
        self.image = self.walking_frames_f[0]
        self.frame_right = 0
        self.frame = 0
    def shot(self):
        self.direction = "S"

    def jump_method(self):
        if self.direction == "L":
            self.direction = "JL"
        elif self.direction == "R":
            self.direction = "JR"
        elif Platformer.direction == "F":
            self.direction = "JF"



    def gravity(self):
        if Platformer.player_fall == True:
            Platformer.y_camera += 5
class Fireball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.damage = 50
        self.frames_r = []
        self.frames_l = []
        self.frames_u = []
        self.direction = ""
        sprite_sheet = SpriteSheet("Sprites//Fireball(1).png")

        color_key_player = (0,0,0,0)
        image = sprite_sheet.get_image(0, 0, 24, 24, color_key_player)
        self.frames_r.append(image)
        image = sprite_sheet.get_image(24, 0, 24, 24, color_key_player)
        self.frames_r.append(image)
        image = sprite_sheet.get_image(48, 0, 24, 24, color_key_player)
        self.frames_r.append(image)
        image = sprite_sheet.get_image(72, 0, 24, 24, color_key_player)
        self.frames_r.append(image)

        image = sprite_sheet.get_image(0, 24, 24, 24, color_key_player)
        self.frames_l.append(image)
        image = sprite_sheet.get_image(24, 24, 24, 24, color_key_player)
        self.frames_l.append(image)
        image = sprite_sheet.get_image(48, 24, 24, 24, color_key_player)
        self.frames_l.append(image)
        image = sprite_sheet.get_image(72, 24, 24, 24, color_key_player)
        self.frames_l.append(image)

        image = sprite_sheet.get_image(0, 48, 24, 24, color_key_player)
        self.frames_u.append(image)
        image = sprite_sheet.get_image(24, 48, 24, 24, color_key_player)
        self.frames_u.append(image)
        image = sprite_sheet.get_image(48, 48, 24, 24, color_key_player)
        self.frames_u.append(image)
        image = sprite_sheet.get_image(72, 48, 24, 24, color_key_player)
        self.frames_u.append(image)

        image = sprite_sheet.get_image(100,100,24,24, color_key_player)
        self.frames_u.append(image)
        self.image = self.frames_u[-1]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(420,290)
        self.toggle = False
        self.frame = 0
        self.time = 0
        self.done = False
    def update(self):
        if self.direction == "R":
            if self.toggle == True:
                self.time += 1
                if self.time % 3 == 0:
                    self.x += 10
                    self.frame += 1
                    if self.frame >= 4:
                        self.frame = 0
                        self.image = self.frames_r[self.frame]
                    self.image = self.frames_r[self.frame]
                self.rect = self.rect.move(self.x, self.y)
                if self.rect.x >= 800:
                    self.done = True
                    self.reset_right()
                    self.x = 0
                    self.y = 0
                    self.image = self.frames_u[-1]
        elif self.direction == "L":
            if self.toggle == True:
                self.time += 1
                if self.time % 3 == 0:
                    self.x -= 10
                    self.frame += 1
                    if self.frame >= 4:
                        self.frame = 0
                        self.image = self.frames_l[self.frame]
                    self.image = self.frames_l[self.frame]
                self.rect = self.rect.move(self.x, self.y)
                if self.rect.x <= 0:
                    self.done = True
                    self.reset_left()
                    self.x = 0
                    self.y = 0
                    self.image = self.frames_u[-1]

    def shot_left(self):
        self.toggle = True
        self.direction = "L"
    def shot_right(self):
        self.toggle = True
        self.direction = "R"
    def reset_right(self):
        self.toggle = False
        self.rect = self.rect.move(-380,0)
    def reset_left(self):
        self.toggle = False
        self.rect = self.rect.move(420, 0)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x_change = 0
        self.y_change = 0
        self.health = 50
        self.damage = 100
        self.x = x
        self.y = y
        self.frames = []
        self.shot = False
        self.follow = ""

        sprite_sheet = SpriteSheet("Sprites//bad_guy.png")

        color_key_player = (255,255,255,255)
        for x1 in range(0,357,89):
            image = sprite_sheet.get_image(x1, 0, 89, 119, color_key_player)
            self.frames.append(image)
        for x2 in range(0,357,89):
            image = sprite_sheet.get_image(x2, 119, 89, 119, color_key_player)
            self.frames.append(image)
        for x3 in range(0,357,89):
            image = sprite_sheet.get_image(x3, 238, 89, 119, color_key_player)
            self.frames.append(image)
        for x4 in range(0,268,89):
            image = sprite_sheet.get_image(x4, 357, 89, 119, color_key_player)
            self.frames.append(image)

        self.image = self.frames[0]
        self.time = 0
        self.frame = 0
        self.rect = self.image.get_rect()

    def update(self):
        self.time += 1
        if self.time % 3 == 0:
            self.frame += 1
            if self.frame >= 19:
                self.frame = 0
                self.image = self.frames[self.frame]
            if self.frame >= 8:
                self.shot = True
            self.image = self.frames[self.frame]
    def camera_follow(self):
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x - Platformer.x_camera,self.y - Platformer.y_camera)
class Player_Death(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        sprite_sheet_death = SpriteSheet("Sprites//Player_Death.png")
        self.frames = []

        color_key_player = (255,255,255,255)
        for x1 in range(0,409,204):
            image = sprite_sheet_death.get_image(x1, 0, 204, 194, color_key_player)
            self.frames.append(image)
        for x2 in range(0,409,204):
            image = sprite_sheet_death.get_image(x2, 194, 204, 194, color_key_player)
            self.frames.append(image)
        for x3 in range(0,205,204):
            image = sprite_sheet_death.get_image(x3, 388, 204, 194, color_key_player)
            self.frames.append(image)
        self.image = self.frames[0]
        self.frame = 0
        self.time = 0
        self.rect = self.image.get_rect()
        self.rect.center = (400,300)
    def update(self):
        self.time += 1
        if self.time % 3 == 0:
            self.frame += 1
            if self.frame >= 8:
                self.frame = 0
                self.image = self.frames[self.frame]
            self.image = self.frames[self.frame]
class Laser(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.changex = 0
        self.changey = 0
        self.damage = 100
        self.direction = ""
        if Controller.insanity <= 2:
            self.image = pygame.image.load("Sprites//Bad_guy_shot.png")
        elif Controller.insanity > 2:
            self.image = pygame.image.load("Sprites//Bad_guy_shot_insanity2.png")
        self.toggle = False
        self.rect = self.image.get_rect()
        self.frame = 0
        self.time = 0
        self.done = False
        self.progress = 0
    def update(self):
        if self.direction == "R":
            if self.toggle == True:
                self.progress = 1
                self.time += 1
                if self.time % 2 == 0:
                    self.changex += 10
                self.rect = self.image.get_rect()
                self.rect = self.rect.move(self.x + self.changex - Platformer.x_camera, self.y - Platformer.y_camera)
            if self.changex >= 400:
                self.done = True
                self.reset()
        elif self.direction == "L":
            if self.toggle == True:
                self.progress = 2
                self.time += 1
                if self.time % 2 == 0:
                    self.changex -= 10
                self.rect = self.image.get_rect()
                self.rect = self.rect.move(self.x + self.changex - Platformer.x_camera, self.y - Platformer.y_camera)
            if self.changex <= -400:
                self.done = True
                self.reset()

    def shot_left(self):
        self.reset()
        self.toggle = True
        self.direction = "L"
    def shot_right(self):
        self.reset()
        self.toggle = True
        self.direction = "R"
    def reset(self):
        self.progress = 0
        self.changex = 0
