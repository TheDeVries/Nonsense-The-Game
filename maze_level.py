import pygame
import random
from controller import *
pygame.init()

class Maze:
    x_camera = 0
    y_camera = 0
    def __init__(self):
        self.start_tick = pygame.time.get_ticks()
        self.running = True
        self.wn = pygame.display.set_mode((800,600), pygame.HWSURFACE)
        self.hedge = pygame.image.load("Sprites//hedge.png")
        self.grass = pygame.image.load("Sprites//grass.png")
        self.hedge_insanity4 = pygame.image.load("Sprites//hedge_insanity4.png")

        self.finish = pygame.image.load("Sprites//finish.png")
        self.song = pygame.mixer.music.load("Sounds//Tchaikovsky - Valse Sentimentale.wav")
        self.boo = pygame.mixer.Sound("Sounds//Demon_Your_Soul_is_mine-BlueMann-1903732045.wav")
        self.insanity2_graphics = pygame.image.load("Sprites//insanity2_maze.png").convert()
        player = Player()
        active_sprite_list = pygame.sprite.Group()
        active_sprite_list.add(player)
        self.blacklist = []
        self.finish_list = []
        self.posy = 300-24
        self.posx = 400-24
        self.tile_size = 96
        self.map_height = 25
        self.map_width = 25
        self.move_camera = 0
        self.random_map = random.randint(1,2)
        self.maze_map = self.random_map
        self.eno = 10
        self.toggle = True
        self.test = True
        self.insanity2_pos = -800
        self.insanity5toggle = False
        if Controller.insanity == 1:
            pygame.mixer.music.play(loops=-1, start=0.0)
        self.map_list = [["1","1","3","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
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

        self.map_list2 = [["1","1","3","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                          ["1","2","2","2","2","2","2","2","2","2","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                          ["1","2","2","2","2","1","1","1","1","2","2","2","2","2","2","2","2","2","2","2","2","1","1","1","1"],
                          ["1","2","2","2","2","2","2","1","1","2","1","1","1","1","1","1","1","1","1","1","2","1","1","1","1"],
                          ["1","2","2","2","2","1","2","2","2","2","1","2","2","2","2","2","2","2","2","1","2","2","2","2","1"],
                          ["1","1","2","1","2","1","2","2","2","2","1","2","1","1","1","1","1","1","2","1","1","1","1","2","1"],
                          ["1","1","2","1","2","1","1","1","1","1","1","2","1","2","2","2","2","1","2","1","2","2","2","2","1"],
                          ["1","1","2","1","2","2","2","2","2","2","2","2","1","2","1","1","2","1","2","1","2","1","1","1","1"],
                          ["1","1","2","1","2","1","2","2","1","1","1","1","1","2","1","2","2","1","2","1","2","2","2","2","1"],
                          ["1","1","2","1","2","1","2","2","1","2","2","2","1","2","1","2","1","1","2","1","1","1","1","1","1"],
                          ["1","1","2","2","2","1","1","1","1","2","1","2","1","2","1","2","1","2","2","2","2","2","2","2","1"],
                          ["1","1","2","1","2","2","2","1","1","2","1","2","1","2","1","2","1","2","2","2","2","2","2","2","1"],
                          ["1","1","2","1","1","1","2","2","2","2","1","2","1","2","1","2","1","2","1","2","1","2","1","2","1"],
                          ["1","1","2","2","2","1","1","1","1","2","1","2","2","2","1","2","1","2","2","2","1","2","1","2","1"],
                          ["1","1","1","1","2","2","2","2","2","2","1","1","1","1","1","1","1","1","2","1","1","2","1","2","1"],
                          ["1","1","1","2","2","1","1","2","1","1","1","2","2","2","1","2","1","2","2","1","2","2","1","2","1"],
                          ["1","1","1","2","1","1","2","2","1","2","2","2","2","2","1","2","1","1","1","1","2","1","1","2","1"],
                          ["1","2","2","2","1","1","2","2","1","2","1","1","1","1","1","2","2","2","1","2","2","1","1","1","1"],
                          ["1","2","1","1","1","1","1","2","1","2","1","2","2","2","1","2","1","2","1","2","1","1","1","2","1"],
                          ["1","2","1","2","2","2","2","2","1","2","1","2","1","2","1","2","1","2","1","2","2","2","2","2","1"],
                          ["1","2","1","2","1","2","1","1","1","2","1","2","1","2","1","2","1","2","1","1","1","1","2","2","1"],
                          ["1","2","2","2","1","2","2","2","2","2","1","2","1","2","1","2","1","2","1","2","2","2","2","1","1"],
                          ["1","2","1","1","1","2","1","1","1","1","1","2","1","2","1","2","1","2","1","1","1","1","2","2","1"],
                          ["1","2","1","2","2","2","2","2","2","2","2","2","1","2","2","2","1","2","2","2","2","1","1","2","3"],
                          ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
        while self.running:
            for event in pygame.event.get():
                # Quit button
                Controller.basic_command(event)
                if Controller.insanity <= 2:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            player.go_up()
                            self.move_camera = 1
                        if event.key == pygame.K_a:
                            player.go_left()
                            self.move_camera = 2
                        if event.key == pygame.K_s:
                            player.go_down()
                            self.move_camera = 3
                        if event.key == pygame.K_d:
                            player.go_right()
                            self.move_camera = 4
                        if event.key == pygame.K_UP:
                            player.go_up()
                            self.move_camera = 1
                        if event.key == pygame.K_LEFT:
                            player.go_left()
                            self.move_camera = 2
                        if event.key == pygame.K_DOWN:
                            player.go_down()
                            self.move_camera = 3
                        if event.key == pygame.K_RIGHT:
                            player.go_right()
                            self.move_camera = 4
                    elif event.type == pygame.KEYUP:
                        self.move_camera = 0
                        player.stop()
                if Controller.insanity >= 3:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            player.go_up()
                            self.move_camera = 1
                        if event.key == pygame.K_d:
                            player.go_left()
                            self.move_camera = 2
                        if event.key == pygame.K_w:
                            player.go_down()
                            self.move_camera = 3
                        if event.key == pygame.K_a:
                            player.go_right()
                            self.move_camera = 4
                        if event.key == pygame.K_DOWN:
                            player.go_up()
                            self.move_camera = 1
                        if event.key == pygame.K_RIGHT:
                            player.go_left()
                            self.move_camera = 2
                        if event.key == pygame.K_UP:
                            player.go_down()
                            self.move_camera = 3
                        if event.key == pygame.K_LEFT:
                            player.go_right()
                            self.move_camera = 4
                        if event.key == pygame.K_p:
                            Controller.scene_selector(self, 2)
                            pygame.mixer.music.stop()
                            self.toggle = False
                            c1 = Controller()
                    elif event.type == pygame.KEYUP:
                        self.move_camera = 0
                        player.stop()
            if self.move_camera == 1:
                self.posy -= self.eno
                Maze.y_camera -= self.eno
            elif self.move_camera == 2:
                self.posx -= self.eno
                Maze.x_camera -= self.eno
                self.insanity2_pos -= self.eno
            elif self.move_camera == 3:
                self.posy += self.eno
                Maze.y_camera += self.eno
            elif self.move_camera == 4:
                self.posx += self.eno
                Maze.x_camera += self.eno
                self.insanity2_pos += self.eno
            self.player_rec = pygame.Rect(self.posx,self.posy,48,48)
            self.wn.fill((0,0,0))
            if self.maze_map == 1:
                self.map_build(self.map_list)
            elif self.maze_map == 2:
                self.map_build(self.map_list2)
            if Controller.insanity == 5 and self.insanity5toggle == False:
                face = insanity5Face()
                active_sprite_list.add(face)
                self.insanity5toggle = True
            self.time = int((pygame.time.get_ticks()-self.start_tick)/1000)

            active_sprite_list.update()

            active_sprite_list.draw(self.wn)
            Controller.insanity_meter(self, self.wn, (255,255,255))
            Controller.score(self, self.wn, (255,255,255))
            for x in self.blacklist:
                if x.colliderect(self.player_rec):
                    self.move_camera = 0
                if x.contains(self.player_rec):
                    print("Boo! insanity level 5, score reduction!")
                    Controller.score_current -= 1
                    self.boo.play(loops=1)
                    Controller.insanity += 1
                    if Controller.insanity > 5:
                        pygame.mixer.music.load("Sounds//Tchaikovsky Distorted.wav")
                        pygame.mixer.music.play(loops=-1, start=0.0)
                        Controller.insanity = 5
            for y in self.finish_list:
                if y.colliderect(self.player_rec):
                    Maze.x_camera = 0
                    Maze.y_camera = 0
                    Controller.scene_selector(self, 2)
                    pygame.mixer.music.stop()
                    self.toggle = False
                    c1 = Controller()
            if Controller.insanity >= 2:
                self.insanity_results(Controller.insanity)
            if self.time == 60 and Controller.insanity < 2:
                Controller.insanity = 2
            elif self.time == 90 and Controller.insanity < 3:
                Controller.insanity = 3
                pygame.mixer.music.load("Sounds//Tchaikovsky Distorted.wav")
                pygame.mixer.music.play(loops=-1, start=0.0)
            elif self.time == 120 and Controller.insanity < 4:
                Controller.insanity = 4
            elif self.time >= 240:
                Controller.insanity = 5

            self.clock()
            pygame.display.flip()

    def map_build(self, map_list):
        if Controller.insanity < 4:
            textures = {"1":self.hedge, "2":self.grass, "3":self.finish}
        elif Controller.insanity >= 3:
            textures = {"1":self.hedge_insanity4, "2":self.grass, "3":self.finish}


        for rows in range(self.map_height):
            for columns in range(self.map_width):
                if textures[map_list[rows][columns]] == self.hedge:
                    self.rec = textures[map_list[rows][columns]].get_rect()
                    self.blacklist += [self.rec.move(columns*self.tile_size, rows*self.tile_size)]
                if textures[map_list[rows][columns]] == self.finish:
                    self.rec1 = textures[map_list[rows][columns]].get_rect()
                    self.finish_list += [self.rec1.move(columns*self.tile_size, rows*self.tile_size)]
                self.wn.blit(textures[map_list[rows][columns]], (columns*self.tile_size - Maze.x_camera, rows*self.tile_size - Maze.y_camera))
    def insanity_results(self, insanity):
        insanity_graphics = []
        self.insanity2_graphics.set_colorkey((0,0,0,0))
        if self.insanity2_pos <= -2400:
            self.insanity2_pos = 0
        elif self.insanity2_pos >= 0:
            self.insanity2_pos = -2400
        self.wn.blit(self.insanity2_graphics, (self.insanity2_pos,0))
        if Controller.insanity == 5:
            pass
    def clock(self):
        myfont = pygame.font.Font("Sprites//digital-7.ttf", 55)
        timefont = myfont.render("Time:", True, (240, 93, 93))
        strtimer = str(self.time)
        clocktimer = myfont.render(strtimer, True, (240, 93, 93))
        self.wn.blit(timefont,(300,0))
        self.wn.blit(clocktimer,(400,0))

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

        color_key_player = (255,100,178,200)
        image = sprite_sheet.get_image(0, 48, 48, 48, (255,100,178,200))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(48, 48, 48, 48, (255,100,178,200))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(96, 48, 48, 48, (255,100,178,200))
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(0, 96, 48, 48, (255,100,178,200))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(48, 96, 48, 48, (255,100,178,200))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(96, 96, 48, 48, (255,100,178,200))
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(0, 0, 48, 48, (255,100,178,200))
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(48, 0, 48, 48, (255,100,178,200))
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(96, 0, 48, 48, (255,100,178,200))
        self.walking_frames_d.append(image)

        image = sprite_sheet.get_image(0, 144, 48, 48, (255,100,178,200))
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(48, 144, 48, 48, (255,100,178,200))
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(96, 144, 48, 48, (255,100,178,200))
        self.walking_frames_u.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.move_ip(400-24,300-24)

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
class insanity5Face(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        sprite_sheet = SpriteSheet("Sprites//creepy.png")
        self.insanity5_frames = []
        color_key_insanity5 = (255,188,200,100)
        for xyx in range(0,321,32):
            image = sprite_sheet.get_image(xyx, 0, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy in range(0,321,32):
            image = sprite_sheet.get_image(xy, 32, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy1 in range(0,321,32):
            image = sprite_sheet.get_image(xy1, 64, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy2 in range(0,321,32):
            image = sprite_sheet.get_image(xy2, 96, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy3 in range(0,321,32):
            image = sprite_sheet.get_image(xy3, 128, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy4 in range(0,321,32):
            image = sprite_sheet.get_image(xy4, 160, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy5 in range(0,321,32):
            image = sprite_sheet.get_image(xy5, 192, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy6 in range(0,321,32):
            image = sprite_sheet.get_image(xy6, 224, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy7 in range(0, 321,32):
            image = sprite_sheet.get_image(xy7, 256, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy8 in range(0,321,32):
            image = sprite_sheet.get_image(xy8, 288, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy9 in range(0,321,32):
            image = sprite_sheet.get_image(xy9, 320, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        self.index = 0
        self.image = self.insanity5_frames[self.index]
        self.rect = self.image.get_rect()
        self.rect.move_ip(0,-100)
    def update(self):
        self.index += 1
        if self.index >= len(self.insanity5_frames)-1:
            self.index = 120
        self.image = self.insanity5_frames[self.index]
