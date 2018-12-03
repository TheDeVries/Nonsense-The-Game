import pygame
import random
from controller import *
pygame.init()

class Club:
    def __init__(self):
        self.start_tick = pygame.time.get_ticks()
        self.running = True
        self.completions = Controller.done_counter[3]
        difficulty = {}
        num_seconds = 25
        #Sounds
        if Controller.insanity < 4:
            self.club_music = pygame.mixer.music.load("Sounds//HOME - Above All.wav")
        else:
            self.club_music = pygame.mixer.music.load("Sounds//Flatline.wav")
        pygame.mixer.music.play(loops=-1, start=0.0)

        #Club Setting
        self.window = pygame.display.set_mode((800, 600))
        self.club_background = pygame.image.load("Sprites//club.png").convert()
        self.club_background2 = pygame.image.load("Sprites//club2.png").convert()
        self.bar = pygame.image.load("Sprites//empty_bar.png").convert()
        self.bar.set_colorkey((0,0,64))

        #Keyboard DDR Setting
        self.speech_bubble = pygame.image.load("Sprites//speech_bubble.png").convert()
        self.directions = ['left', 'up', 'down', 'right']
        landing_arrows = pygame.sprite.Group()
        self.arrow_group = pygame.sprite.Group()
        for i in self.directions:
            sprite = Arrow(2, i, 0)
            landing_arrows.add(sprite)

        #Last considerations
        self.setting = 1
        self.mooded = False
        their_moods = ["normal", "high", "low"]
        our_background = self.club_background
        tex = random.randint(1,3)
        bad_background = pygame.image.load("Sprites//glitch_texture" + str(tex) + ".png").convert()
        self.chosens = self.Randomize()

        while self.running == True:
            self.window.blit(bad_background, (0,0))
            self.window.blit(our_background, (0,0))
            Controller.score(self, self.window, (255,255,255))
            Controller.insanity_meter(self, self.window, (255,255,255))

            if self.setting == 1:
                if Controller.insanity > 1:
                    if (pygame.time.get_ticks() - self.start_tick)/1000 == 1:
                        our_background.set_colorkey((0,0,64))
                    if Controller.insanity > 2:
                        our_background.set_colorkey((0,0,64))

                if self.completions > 0:
                    Controller.clock(self, self.window, (240, 93, 93), 10, self.start_tick)
                else:
                    pass
                character_group = pygame.sprite.Group()
                server_group = pygame.sprite.Group()

                for i in range(-1, -len(self.chosens)+2, -1):
                    if self.chosens[i] != "Sprites//bar_server.png" and self.chosens[i] != "Sprites//c_server.png":
                        sprite = Character(self.chosens[i], self.chosens[i-3])
                        if self.mooded == False:
                            feel_num = random.randint(0, (len(their_moods)-1))
                            the_mood = their_moods[feel_num]
                            del their_moods[feel_num]
                            sprite.mood = the_mood
                        character_group.add(sprite)
                character_group.draw(self.window)
                self.window.blit(self.bar, (200, 300))
                if self.chosens[5] == "Sprites//bar_server.png" or self.chosens[5] == "Sprites//c_server.png":
                    sprite = Character(self.chosens[5], self.chosens[2])
                    sprite.mood = their_moods[0]
                    server_group.add(sprite)
                server_group.draw(self.window)
                self.mooded = True

            elif self.setting == 2:
                Controller.clock(self, self.window, (93, 240, 93), num_seconds, self.start_tick)

                image_string = self.clicked_character[:-4] + "_front.png"
                image_surface = pygame.image.load(image_string).convert()
                image_surface.set_colorkey((255,255,255))
                self.window.blit(image_surface, (400, 300))
                self.speech_bubble.set_colorkey((255,255,255))
                self.window.blit(self.speech_bubble, (400, 65))
                landing_arrows.draw(self.window)

                self.arrow_group.update(Arrow.position)
                self.arrow_group.draw(self.window)

                #if not self.arrow_group and Arrow.position[1] < 70:
                    #Controller.transition(self, Controller.scene, False)

            for event in pygame.event.get():
                Controller.basic_command(self, event)
                # Keybinds
                if event.type == pygame.KEYDOWN:
                    if self.setting == 2:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            if self.flying_arrow.position[1] in range(60, 170):
                                self.flying_arrow.kill()
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            pass
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            pass
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            pass

                # Mouseclick
                if event.type == pygame.MOUSEBUTTONDOWN and self.setting == 1:
                    clicked_pos = event.pos
                    self.clicked_character = self.check_collision(clicked_pos,character_group,server_group)
                    if self.clicked_character != False:
                        self.play_mood = self.clicked_character.mood
                        self.clicked_character = self.clicked_character.file
                        our_background = self.club_background2
                        self.setting = 2

            pygame.display.flip()

    def spawner(self, rate):
        pass


        sprite = Arrow(1, 'left', 1)
        self.arrow_group.add(sprite)

    def check_collision(self, point, *groups):
        for group in groups:
            for g in group:
                if g.rect.collidepoint(point):
                    try:
                        if g.mask.get_at(point) != 0:
                            return g
                    except:
                        print("error. instead, we're assuming a rectangle was clicked")
                        return g

        return False

    def Randomize(self):
        '''
        Returns a list where the first three items are position tuples randomly picked from five possible options
        and the last three items are sprite strings that match with the position three indexes prior.
        Example: (pos1, pos2, pos3, sprite1, sprite2, sprite3)
        '''
        self.chosens = []
        self.positions = self.rand_positions()
        self.characters = self.rand_characters(self.positions)
        self.chosens = self.positions + self.characters
        return self.chosens

    def rand_positions(self):
        '''
        Removes two of the possible character blit positions leaving the three chosen positions to return
        '''
        self.positions = [(200, 210), (325, 150), (450, 90), (575, 30), (550, 200)]
        for i in range(2):
            self.choice = random.choice(self.positions)
            self.positions.remove(self.choice)
        return self.positions

    def rand_characters(self, positions):
        '''
        Takes positions as parameter and selects characters to return based on those positions
        This is mostly randomized except when the bar_server position is selected and this sprite is confirmed to be a part of the returned list of chosen characters.
        This also reponds to insanity by selecting creepier sprites with a higher chance of them appearing with more insanity.
        '''
        self.characters = ["Sprites//bar_man.png", "Sprites//bar_man2.png", "Sprites//bar_woman.png", "Sprites//bar_woman2.png"]

        if Controller.insanity == 2:
            i = random.randint(0,9)
            if i < 5:
                if i == 1:
                    self.characters.remove("Sprites//bar_man.png")
                    self.characters.append("Sprites//c_man.png")
                elif i == 2:
                    self.characters.remove("Sprites//bar_man2.png")
                    self.characters.append("Sprites//c_man2.png")
                elif i == 3:
                    self.characters.remove("Sprites//bar_woman.png")
                    self.characters.append("Sprites//c_woman.png")
                elif i == 4:
                    self.characters.remove("Sprites//bar_woman2.png")
                    self.characters.append("Sprites//c_woman2.png")

        elif Controller.insanity == 3:
            i = random.randint(0,8)
            if i < 5:
                if i == 1:
                    self.characters.remove("Sprites//bar_man.png")
                    self.characters.append("Sprites//c_man.png")
                elif i == 2:
                    self.characters.remove("Sprites//bar_man2.png")
                    self.characters.append("Sprites//c_man2.png")
                elif i == 3:
                    self.characters.remove("Sprites//bar_woman.png")
                    self.characters.append("Sprites//c_woman.png")
                elif i == 4:
                    self.characters.remove("Sprites//bar_woman2.png")
                    self.characters.append("Sprites//c_woman2.png")
            if "Sprites//mantis.png" not in self.characters:
                i = random.randint(0,3)
                self.characters.remove(self.characters[i])
                self.characters.append("Sprites//mantis.png")

        elif Controller.insanity == 4 or Controller.insanity == 5:
            i = random.randint(0,5)
            self.characters.remove("Sprites//bar_man.png")
            self.characters.append("Sprites//c_man.png")
            self.characters.remove("Sprites//bar_man2.png")
            self.characters.append("Sprites//c_man2.png")
            self.characters.remove("Sprites//bar_woman.png")
            self.characters.append("Sprites//c_woman.png")
            self.characters.remove("Sprites//bar_woman2.png")
            self.characters.append("Sprites/c_woman2.png")
            if "Sprites//mantis.png" not in self.characters:
                i = random.randint(0,3)
                self.characters.remove(self.characters[i])
                self.characters.append("Sprites//mantis.png")

        self.chosen_characters = []
        for i in range(len(self.positions)):
            if self.positions[i] == (550,200):
                if Controller.insanity >= 3:
                    top = 10
                    if Controller.insanity == 4:
                        top = 8
                    if Controller.insanity == 5:
                        top = random.randint(5, 6)
                    i = random.randint(0, top)
                    if i < 5:
                        self.chosen_characters.append("Sprites//c_server.png")
                    else:
                        self.chosen_characters.append("Sprites//bar_server.png")
                else:
                    self.chosen_characters.append("Sprites//bar_server.png")
            else:
                self.choice = random.choice(self.characters)
                self.chosen_characters.append(self.choice)
                self.characters.remove(self.choice)

        return self.chosen_characters

# Club Models
class Character(pygame.sprite.Sprite):
    def __init__(self, file, position):
        self.file = file
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (250, 500))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = position
        self.mood = "normal"
# Setting 2 Exclusive
class Dialogue:
    def __init__(self, position, mood):
        myfont = pygame.font.Font("Sprites//times.ttf", 45)

class Arrow(pygame.sprite.Sprite):
    position = 0
    speed = 1
    def __init__(self, type, direction, speed):
        pygame.sprite.Sprite.__init__(self)
        Arrow.speed = speed
        #Where type 1 are flying arrows and 2 are the landing arrows
        if type == 1:
            self.image = pygame.image.load("Sprites//arrow.png").convert_alpha()
            ar_direc = {'left': self.image, 'right': pygame.transform.rotate(self.image, 180), 'up': pygame.transform.rotate(self.image, 270), 'down': pygame.transform.rotate(self.image, 90)}
            self.image = ar_direc[direction]
            self.rect = self.image.get_rect()
            ar_start = {'left': (5, 600), 'up': (105, 600), 'down': (205, 600), 'right': (305, 600)}
            self.position = ar_start[direction]
            Arrow.position = self.position
            self.rect.topleft = Arrow.position
        elif type == 2:
            if Controller.insanity != 5:
                self.image = pygame.image.load("Sprites//arrow_orange.png").convert()
            else:
                insane_arrow = "Sprites//insane_arrow" + str(random.randint(1,3)) + ".png"
                self.image = pygame.image.load(insane_arrow).convert_alpha()
            ar_direc = {'left': self.image, 'right': pygame.transform.rotate(self.image, 180), 'up': pygame.transform.rotate(self.image, 270), 'down': pygame.transform.rotate(self.image, 90)}
            self.rect = self.image.get_rect()
            ar_end = {'left': (5, 64), 'up': (105, 64), 'down': (205, 64), 'right': (305, 64)}
            self.image = ar_direc[direction]
            self.end_position = ar_end[direction]
            self.rect.topleft = self.end_position

    def update(self, position):
        self.x = self.position[0]
        new_pos = float(Arrow.position[1]) - float(Arrow.speed)
        Arrow.position = (self.x, new_pos)
        self.rect.topleft = Arrow.position
