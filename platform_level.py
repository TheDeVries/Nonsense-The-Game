import pygame
from controller import *


class PlatformLevel:
    x_camera = 0
    y_camera = 0
    def __init__(self):
        pygame.init()
        self.move_camera = 0
        self.window = pygame.display.set_mode((800,600))
        self.background = pygame.image.load("Sprites//sky.png")
        self.background = pygame.transform.scale(self.background, (2000 + PlatformLevel.x_camera,600 + PlatformLevel.y_camera))
        self.rect = self.background.get_rect()
        self.rect.move_ip((0,0))
        self.window.fill((255,255,255))
        self.running = True
        player = Player_Platform()
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
                if Controller.sanity <= 2:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            self.move_camera = 1
                            player.go_left()
                        if event.key == pygame.K_d:
                            self.move_camera = 2
                            player.go_right()
                        if event.key == pygame.K_LEFT:
                            self.move_camera = 1
                            player.go_left()
                        if event.key == pygame.K_RIGHT:
                            self.move_camera = 2
                            player.go_right()
                    elif event.type == pygame.KEYUP:
                        player.stop()
                        self.move_camera = 0
            if self.move_camera == 1:
                PlatformLevel.x_camera -= 5
            elif self.move_camera == 2:
                PlatformLevel.x_camera += 5


            self.window.blit(self.background, (0, 0))
            self.platforms()
            active_sprite_list2.update()

            active_sprite_list2.draw(self.window)

            pygame.display.flip()
    def platforms(self):
        pygame.draw.rect(self.window, (255,255,255), pygame.Rect(100 - PlatformLevel.x_camera,100,100,100))
class Player_Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_change = 0
        self.y_change = 0
        self.health = 100
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_f = []

        self.direction = "F"

        sprite_sheet = SpriteSheet("Sprites//stickman.png")

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


        # Set the image the player starts with
        self.image = self.walking_frames_f[0]
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.move_ip(400,300)
        self.frame = 0
        self.frame_right = 0
        self.time = 0

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
