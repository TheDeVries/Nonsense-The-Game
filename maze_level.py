import pygame
from controller import *
pygame.init()
class Maze:
    x_camera = 0
    y_camera = 0
    def __init__(self):
        self.running = True
        self.wn = pygame.display.set_mode((800,600))
        self.mountain = pygame.image.load("Sprites//grass_mount1.png")
        self.grass = pygame.image.load("Sprites//grass.png")
        self.finish = pygame.image.load("Sprites//finish.png")
        self.song = pygame.mixer.music.load("Sounds//Tchaikovsky - Valse Sentimentale.wav")
        player = Player()
        active_sprite_list = pygame.sprite.Group()
        active_sprite_list.add(player)
        self.blacklist = []
        self.finish_list = []
        self.posy = 300
        self.posx = 400
        self.tile_size = 96
        self.map_height = 25
        self.map_width = 25
        self.move_camera = 0
        self.eno = 10
        self.toggle = True
        pygame.mixer.music.play(loops=-1, start=0.0)
        #self.player_rec.move_ip(400,300)
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
                    if event.key == pygame.K_w:
                        player.go_up()
                        self.move_camera = 1
                    elif event.key == pygame.K_a:
                        player.go_left()
                        self.move_camera = 2
                    elif event.key == pygame.K_s:
                        player.go_down()
                        self.move_camera = 3
                    elif event.key == pygame.K_d:
                        player.go_right()
                        self.move_camera = 4
                    elif event.key == pygame.K_UP:
                        player.go_up()
                        self.move_camera = 1
                    elif event.key == pygame.K_LEFT:
                        player.go_left()
                        self.move_camera = 2
                    elif event.key == pygame.K_DOWN:
                        player.go_down()
                        self.move_camera = 3
                    elif event.key == pygame.K_RIGHT:
                        player.go_right()
                        self.move_camera = 4
                elif event.type == pygame.KEYUP:
                    self.move_camera = 0
                    player.stop()
            if self.move_camera == 1:
                self.posy -= self.eno
                Maze.y_camera -= self.eno
            elif self.move_camera == 2:
                self.posx -= self.eno
                Maze.x_camera -= self.eno
            elif self.move_camera == 3:
                self.posy += self.eno
                Maze.y_camera += self.eno
            elif self.move_camera == 4:
                self.posx += self.eno
                Maze.x_camera += self.eno
            self.player_rec = pygame.Rect(self.posx,self.posy,48,48)
            #self.player_rec = self.player_rec.move(self.posx, self.posy)
            self.wn.fill((0,0,0))
            self.map_build()
            active_sprite_list.draw(self.wn)
            active_sprite_list.update()
            pygame.display.flip()
            for x in self.blacklist:
                if x.colliderect(self.player_rec):
                    self.move_camera = 0
            for y in self.finish_list:
                if y.colliderect(self.player_rec):
                    Controller.scene -= 1
                    c1 = Controller()

    def map_build(self):
        textures = {"1":self.mountain, "2":self.grass, "3":self.finish}
        map_list = [["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                    ["1","2","2","2","2","1","1","1","1","1","1","1","1","1","1","1","1","1","2","2","2","1","2","1","1"],
                    ["1","2","2","2","2","1","1","1","2","2","2","2","2","2","2","2","2","1","2","1","2","1","2","1","1"],
                    ["1","2","2","2","2","2","2","1","2","1","1","1","1","1","2","1","2","1","2","1","2","1","2","1","1"],
                    ["1","1","1","1","1","1","2","1","2","1","2","2","2","1","2","1","2","1","2","1","2","1","2","1","1"],
                    ["1","2","2","2","2","2","2","1","2","1","2","1","2","1","2","1","2","1","2","1","2","1","2","1","1"],
                    ["1","2","1","1","1","1","1","1","2","1","2","1","2","1","2","1","2","2","2","1","2","1","2","1","1"],
                    ["1","2","1","1","1","1","1","1","1","1","2","1","2","1","2","1","1","1","1","1","2","1","2","1","1"],
                    ["1","2","1","1","1","1","2","2","2","2","2","1","2","2","2","1","2","2","2","2","2","1","2","1","1"],
                    ["1","2","2","2","2","2","2","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","2","1","1"],
                    ["1","1","1","1","1","1","2","2","2","2","2","2","2","2","2","1","2","2","2","1","2","2","2","2","1"],
                    ["1","1","2","2","2","1","2","1","1","1","1","2","2","1","2","1","2","1","2","1","2","1","1","2","1"],
                    ["1","1","2","1","2","1","2","2","2","2","1","1","1","1","2","2","2","1","2","2","2","1","1","2","1"],
                    ["1","1","2","1","2","1","1","1","1","2","2","2","2","1","1","1","1","1","1","1","1","1","1","2","1"],
                    ["1","1","2","1","2","2","2","2","1","1","1","1","2","2","2","2","2","1","2","2","2","2","2","2","1"],
                    ["1","1","2","1","1","1","1","2","2","2","2","1","1","1","1","1","2","1","2","1","1","1","1","1","1"],
                    ["1","1","2","2","2","2","1","1","1","1","2","2","2","2","2","2","2","1","2","2","2","2","2","2","1"],
                    ["1","1","1","1","1","1","1","1","2","1","2","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                    ["1","1","2","2","2","2","2","2","2","1","2","1","2","2","2","2","2","1","2","1","2","2","2","1","1"],
                    ["1","1","2","1","1","1","1","1","2","1","2","1","2","1","1","1","2","2","2","1","2","1","2","1","1"],
                    ["1","1","2","2","2","1","2","1","2","2","2","1","2","2","2","1","1","1","1","1","2","1","1","1","1"],
                    ["1","1","2","1","2","1","2","1","1","1","1","1","2","1","2","2","2","2","2","2","2","1","2","2","1"],
                    ["1","1","2","1","2","1","2","1","2","2","2","2","2","1","1","1","1","1","1","1","1","1","2","2","3"],
                    ["1","1","1","1","2","2","2","2","2","1","1","1","2","2","2","2","2","2","2","2","2","2","2","2","1"],
                    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]

        for rows in range(self.map_height):
            for colums in range(self.map_width):
                if textures[map_list[rows][colums]] == self.mountain:
                    self.rec = textures[map_list[rows][colums]].get_rect()
                    self.blacklist += [self.rec.move(colums*self.tile_size, rows*self.tile_size)]
                if textures[map_list[rows][colums]] == self.finish:
                    self.rec1 = textures[map_list[rows][colums]].get_rect()
                    self.finish_list += [self.rec1.move(colums*self.tile_size, rows*self.tile_size)]
                self.wn.blit(textures[map_list[rows][colums]], (colums*self.tile_size - Maze.x_camera, rows*self.tile_size - Maze.y_camera))






class SpriteSheet(object):

    def __init__(self, file_name):

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()


    def get_image(self, x, y, width, height):

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey((255,100,178,200))

        # Return the image
        return image
class Player(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.change_x = 0
        self.change_y = 0
        self.x_val = 0
        self.y_val = 0

        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_d = []
        self.walking_frames_u = []

        self.direction = "D"


        sprite_sheet = SpriteSheet("Sprites//character_walk.png")

        image = sprite_sheet.get_image(0, 48, 48, 48)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(48, 48, 48, 48)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(96, 48, 48, 48)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(0, 96, 48, 48)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(48, 96, 48, 48)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(96, 96, 48, 48)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(0, 0, 48, 48)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(48, 0, 48, 48)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(96, 0, 48, 48)
        self.walking_frames_d.append(image)

        image = sprite_sheet.get_image(0, 144, 48, 48)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(48, 144, 48, 48)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(96, 144, 48, 48)
        self.walking_frames_u.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.move_ip(400,300)

        self.x_coord = self.rect.left
        self.y_coord = self.rect.top

    def update(self):


        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x - Maze.x_camera
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "L":
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]


        # Move up/down
        self.rect.y += self.change_y
        posy = self.rect.y - Maze.y_camera
        if self.direction == "U":
            frame = (posy // 30) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[frame]
        elif self.direction == "D":
            frame = (posy // 30) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[frame]







    # Player-controlled movement:
    def go_left(self):
        self.direction = "L"


    def go_right(self):
        self.direction = "R"

    def go_up(self):
        self.direction = "U"

    def go_down(self):
        self.direction = "D"

    def stop(self):
        self.change_x = 0
