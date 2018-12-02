import pygame
from controller import *

class Platformer:
    x_camera = 0
    y_camera = 0
    player_fall = True
    ground = False
    direction = ""
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800,600))
        self.background = pygame.image.load("Sprites//galaxy2.png")
        self.rect = self.background.get_rect()
        self.rect.move_ip((0,0))
        self.window.fill((255,255,255))
        self.running = True
        self.posx = 400-18
        self.posy = 300-22
        player = Player_Platform()
        bullet = Fireball()
        self.active_sprite_list2 = pygame.sprite.Group()
        self.active_sprite_list2.add(player)
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
                        player.shot()
                        self.active_sprite_list2.add(bullet)
                        bullet.shot()
                    if event.key == pygame.K_SPACE:
                        player.jump_method()
                elif event.type == pygame.KEYUP:
                    if event.key != pygame.K_SPACE:
                        player.stop()
            self.player_rec = pygame.Rect(400,300,48,48)

            self.window.blit(self.background, (0, 0))
            player.gravity()
            Platforms = Platforms_Map(self.window)
            Platforms.platforms(self.player_rec)
            self.active_sprite_list2.update()
            self.active_sprite_list2.draw(self.window)
            if bullet.done == True:
                self.active_sprite_list2.remove(bullet)
                bullet.done = False
            pygame.display.flip()
            print(Platforms.platformrect_list)
            print(Platformer.y_camera)
            print(Platformer.player_fall)
            print(self.player_rec)

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


            print(self.platformrect_list[platformrect].colliderect(player))
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
            if self.jump_height < 50:
                self.jump_height += 1
                Platformer.y_camera -= 10
                Platformer.x_camera += 5
                self.image = self.jumping_frames_r[0]
                Platformer.ground = False
            if self.jump_height >= 50:
                self.jump_height += 1
                Platformer.x_camera += 5
                self.image = self.jumping_frames_r[1]
            if Platformer.player_fall == False:
                self.jump_height = 0
        elif self.direction == "JL":
            if self.jump_height < 50:
                self.jump_height += 1
                Platformer.y_camera -= 10
                Platformer.x_camera -= 5
                self.image = self.jumping_frames_l[0]
                Platformer.ground = False
            if self.jump_height >= 50:
                self.jump_height += 1
                Platformer.x_camera -= 5
                self.image = self.jumping_frames_l[1]
            if Platformer.player_fall == False:
                self.jump_height = 0
        elif self.direction == "JF":
            if self.jump_height < 50:
                self.jump_height += 1
                Platformer.y_camera -= 10
                Platformer.ground = False
            if self.jump_height >= 50:
                self.jump_height += 1
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
        elif self.direction == "F":
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
        self.rect = self.rect.move(430,300)
        self.toggle = False
        self.frame = 0
        self.time = 0
        self.done = False
    def update(self):
        if Platformer.direction == "R":
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
                    self.image = self.frames_u[-1]
        elif Platformer.direction == "L":
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
                    self.image = self.frames_u[-1]

    def shot(self):
        self.toggle = True
    def reset_right(self):
        self.toggle = False
        self.rect = self.rect.move(-370,0)
    def reset_left(self):
        self.toggle = False
        self.rect = self.rect.move(430, 0)
