import pygame
import random
from controller import *
pygame.init()

class Typing:
    def __init__(self):
        self.start_tick = pygame.time.get_ticks()
        #Sounds
        self.window = pygame.display.set_mode((800,600))
        self.welcome_jingle = pygame.mixer.Sound("Sounds//Computer Magic.wav")
        self.chime = pygame.mixer.Sound("Sounds//Electronic_Chime.wav")
        self.check = pygame.mixer.Sound("Sounds//Check Mark.wav")

        #Sprites
        self.ty_background = pygame.image.load("Sprites//Pro Typing.png").convert()
        self.walmart = pygame.image.load("Sprites//walmart.png").convert()

        I1_L1 = ["cat", "tractor", "monkey", "boat", "house", "man", "hat", "run",
        "elephant", "mouse", "computer", "pick", "deep", "sports", "fruit",
        "ocean", "money", "game", "snake", "car", "factory", "food", "family"]
        I1_L2 = ["receipt", "instructions", "development", "civilization", "etiquette",
        "mispronunciation", "success", "advertisement", "commercial", "residential",
        "education", "industrial", "excellence", "guarantee", "typing", "one-hundred",
        "concealed", "envelope", "kangaroo", "biscuit", "melon", "ghost", "month"]
        I1_L3 = ["copyrightable", "supercalifragilisticexpialidocious", "uninitiated",
        "righteous", "engineering", "resolution", "disappear", "emancipation", "establishment"
        "titration", "responsibilities", "environmental", "satisfactory", "hovercraft"]
        I2_L1 = ["bogus", "heart", "head", "shoulder", "knees", "toes", "and", "wall",
        "dark", "light", "floor", "roof", "ceiling", "gnat", "bug", "fly", "dot", "excuses",
        "koala", "gong", "tower", "wires", "wad", "lake", "shallow", "moon", "bash"]
        words = []

        words += I1_L1
        our_word = "|"
        self.word = random.choice(words)
        self.strike_count = 0

        self.welcome_jingle.play(loops=0)
        self.myfont = pygame.font.Font("Sprites//times.ttf", 40)
        self.strike = pygame.image.load("Sprites//strike.png").convert()
        self.strike = pygame.transform.scale(self.strike, (40, 40))
        self.strike.set_colorkey((0,0,0))
        left_count = 5

        running = True
        while running:
            self.window.blit(self.ty_background, (0,0))
            Controller.score(self, self.window, (255,255,255))
            Controller.insanity_meter(self, self.window, (255,255,255))
            Controller.clock(self, self.window, (240, 93, 93), 30, self.start_tick)
            display_word = self.myfont.render(self.word, True, (0, 0, 0))
            display_line = self.myfont.render(">", True, (0,0,0))
            display_cursor = self.myfont.render("|", True, (0,0,0))
            self.window.blit(display_word, (270, 405))
            self.window.blit(display_line, (10, 475))
            display_count = self.myfont.render(str(left_count), True, (0,0,0))
            self.window.blit(display_count, (574, 210))
            if self.strike_count == 1:
                self.window.blit(self.strike, (574, 335))
            elif self.strike_count == 2:
                self.window.blit(self.strike, (574, 335))
                self.window.blit(self.strike, (624, 335))
            elif self.strike_count >= 3:
                self.window.blit(self.strike, (574, 335))
                self.window.blit(self.strike, (624, 335))
                self.window.blit(self.strike, (674, 335))
            l = len(our_word)

            if left_count == 0:
                Controller.transition(self, 5, True)
                c = Controller()

            for event in pygame.event.get():
                # Quit button
                Controller.basic_command(self, event)
                # Keybinds
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:

                        if our_word[0:l-1] == self.word:
                            left_count -= 1
                            self.check.play(loops=0)
                        else:
                            self.strike_count += 1
                        self.word = random.choice(words)
                        our_word = "|"
                    elif event.key == pygame.K_BACKSPACE:
                        our_word = our_word[0:(l-2)]
                        our_word += "|"
                    elif event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                        pass
                    else:
                        our_key = self.myfont.render(chr(event.key), True, (0,0,0))
                        our_word = our_word[0:(l-1)]
                        our_word += chr(event.key)
                        our_word += "|"
            display_ours = self.myfont.render(our_word, True, (0,0,0))
            self.window.blit(display_ours, (40, 475))

            pygame.display.flip()
