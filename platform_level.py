import pygame
from controller import *

class Platformer:
    x_camera = 0
    y_camera = 0
    def __init__(self):
        pygame.init()
        self.move_camera = 0
        self.window = pygame.display.set_mode((800,600))
        self.background = pygame.image.load("Sprites//sky.png")
        self.background = pygame.transform.scale(self.background, (2000 + Platformer.x_camera,600 + Platformer.y_camera))
        self.rect = self.background.get_rect()
        self.rect.move_ip((0,0))
        self.window.fill((255,255,255))
        self.platform_list = []
        self.running = True
        self.player_jump = False
        player = Player_Platform()
        bullet = Bullet()
        active_sprite_list2 = pygame.sprite.Group()
        active_sprite_list2.add(player)
        while self.running:
            for event in pygame.event.get():
                # Quit button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # Keybinds
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player.go_left()
                        self.move_camera = 1
                    if event.key == pygame.K_d:
                        self.move_camera = 2
                        player.go_right()
                    if event.key == pygame.K_LEFT:
                        self.move_camera = 1
                        player.go_left()
                    if event.key == pygame.K_RIGHT:
                        self.move_camera = 2
                        player.go_right()
                    if event.key == pygame.K_LSHIFT:
                        player.shot()
                        active_sprite_list2.add(bullet)
                        bullet.shot()
                    if event.key == pygame.K_SPACE:
                        if self.player_jump == True:
                            self.move_camera = 4
                elif event.type == pygame.KEYUP:
                    if event.key != pygame.K_SPACE:
                        player.stop()
                        self.move_camera = 0
            if self.move_camera == 1:
                Platformer.x_camera -= 5
            elif self.move_camera == 2:
                Platformer.x_camera += 5
            elif self.move_camera == 3:
                Platformer.y_camera += 10
            elif self.move_camera == 4:
                Platformer.y_camera -=100
            self.window.blit(self.background, (0, 0))
            self.platforms()
            for plat in range(0, len(self.platform_list)-1):
                if self.platform_list[plat].colliderect(player):
                    self.move_camera = 0
                    self.player_jump = True
                else:
                    self.move_camera =  3
                    self.player_jump = False
            active_sprite_list2.update()
            active_sprite_list2.draw(self.window)
            if bullet.done == True:
                active_sprite_list2.remove(bullet)
                bullet.done = False
            print(Platformer.x_camera)
            pygame.display.flip()
    def platforms(self):
        #Floor
        self.platform1 = pygame.draw.rect(self.window, (255,255,255), pygame.Rect(0,500 - Platformer.y_camera,800,400))
        self.platform_list.append(self.platform1)
        #platforms_list
        self.platform2 = pygame.draw.rect(self.window, (255,255,255), pygame.Rect(0 - Platformer.x_camera,425 - Platformer.y_camera,100,40))
        self.platform_list.append(self.platform2)



class Player_Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_change = 0
        self.y_change = 0
        self.health = 100
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_f = []
        self.shooting = []

        self.direction = "F"

        sprite_sheet = SpriteSheet("Sprites//stickman.png")
        sprite_sheet_shot = SpriteSheet("Sprites//shot1.png")

        color_key_player = (255,255,255,255)
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

        image = sprite_sheet_shot.get_image(0, 0, 197, 218, color_key_player)
        image = pygame.transform.scale(image, (40,44))
        self.shooting.append(image)
        image = sprite_sheet_shot.get_image(197, 0, 197, 218, color_key_player)
        image = pygame.transform.scale(image, (40,44))
        self.shooting.append(image)
        image = sprite_sheet_shot.get_image(0, 218, 197, 218, color_key_player)
        image = pygame.transform.scale(image, (40,44))
        self.shooting.append(image)

        image = sprite_sheet_shot.get_image(197, 218, 197, 218, color_key_player)
        image = pygame.transform.scale(image, (40,44))
        self.shooting.append(image)




        # Set the image the player starts with
        self.image = self.walking_frames_f[0]
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.move_ip(400,300)
        self.frame = 0
        self.frame_right = 0
        self.shot_frame = 0
        self.shot_frame_L = 2
        self.time = 0
        self.move = False

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
        elif self.direction == "L":
            self.time += 1
            if self.time % 3 == 0:
                self.frame_right += 1
                if self.frame_right > 3:
                    self.frame_right = 0
                    self.image = self.walking_frames_l[self.frame_right]
                self.image = self.walking_frames_l[self.frame_right]
        elif self.direction == "SR":
            self.time += 1
            if self.time % 3 == 0:
                self.shot_frame += 1
                if self.shot_frame > 1:
                    self.shot_frame = 0
                    self.image = self.shooting[self.shot_frame]
                self.image = self.shooting[self.shot_frame]








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
        self.direction = "SR"
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.damage = 50
        self.frames_bullet = []
        sprite_sheet = SpriteSheet("Sprites//bullet.png")

        color_key_player = (0,0,0,0)
        image = sprite_sheet.get_image(0, 0, 16, 12, color_key_player)
        self.frames_bullet.append(image)
        image = sprite_sheet.get_image(16, 0, 16, 12, color_key_player)
        self.frames_bullet.append(image)
        image = sprite_sheet.get_image(32, 0, 16, 12, color_key_player)
        self.frames_bullet.append(image)
        image = sprite_sheet.get_image(0, 12, 16, 12, color_key_player)
        self.frames_bullet.append(image)

        image = sprite_sheet.get_image(16, 12, 16, 12, color_key_player)
        self.frames_bullet.append(image)
        image = sprite_sheet.get_image(32, 12, 16, 12, color_key_player)
        self.frames_bullet.append(image)
        image = sprite_sheet.get_image(0, 24, 16, 12, color_key_player)
        self.frames_bullet.append(image)
        image = sprite_sheet.get_image(16, 24, 16, 12, color_key_player)
        self.frames_bullet.append(image)

        image = sprite_sheet.get_image(32, 24, 16, 12, color_key_player)
        self.frames_bullet.append(image)

        image = sprite_sheet.get_image(0, 36, 16, 12, color_key_player)
        self.frames_bullet.append(image)
        image = sprite_sheet.get_image(16, 36, 16, 12, color_key_player)
        self.frames_bullet.append(image)
        image = sprite_sheet.get_image(32, 36, 16, 12, color_key_player)
        self.frames_bullet.append(image)

        image = sprite_sheet.get_image(0, 48, 16, 12, color_key_player)
        self.frames_bullet.append(image)
        image = sprite_sheet.get_image(16,48,16,12, color_key_player)
        self.frames_bullet.append(image)
        self.image = self.frames_bullet[-1]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(430,300)
        self.toggle = False
        self.frame = 0
        self.time = 0
        self.done = False
    def update(self):
        if self.toggle == True:
            self.time += 1
            if self.time % 3 == 0:
                self.x += 25
                self.frame += 1
                if self.frame > 12:
                    self.frame = 0
                    self.image = self.frames_bullet[self.frame]
                self.image = self.frames_bullet[self.frame]
            self.rect = self.rect.move(self.x, self.y)
        if self.rect.x >= 800:
            self.done = True
            self.reset()
            self.x = 0
            self.image = self.frames_bullet[-1]

    def shot(self):
        self.toggle = True
    def reset(self):
        self.toggle = False
        self.rect = self.rect.move(-370,0)
