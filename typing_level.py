import pygame
import random
from controller import *
pygame.init()

class Typing:
    def __init__(self):
        self.start_tick = pygame.time.get_ticks()
        #Sounds
        self.window = pygame.display.set_mode((800,600))
        if Controller.insanity < 3:
            self.welcome_jingle = pygame.mixer.Sound("Sounds//Computer Magic.wav")
        else:
            self.welcome_jingle = pygame.mixer.Sound("Sounds//distortion1.wav")
        self.chime = pygame.mixer.Sound("Sounds//Electronic_Chime.wav")
        self.check = pygame.mixer.Sound("Sounds//Check Mark.wav")

        #Sprites
        self.background = pygame.image.load("Sprites//Pro Typing.png").convert()
        self.walmart = pygame.image.load("Sprites//walmart.png").convert()

        I1_L1 = ["cat", "tractor", "monkey", "boat", "house", "man", "hat", "run",
        "elephant", "mouse", "computer", "pick", "deep", "sports", "fruit",
        "ocean", "money", "game", "snake", "car", "factory", "food", "family", "the"]
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
        I2_L2 = ["condemnation", "vibrato", "candy", "image", "malfunction", "idol", "stupid",
        "greed", "power", "ghost", "leer", "singed", "quirky", "hunter", "backslash", "backlash",
        "snapshot", "jungle", "racing", "demolition", "flowers", "giant", "garden"]
        I2_L3 = ["infatuation", "revelation", "revolution", "buoyancy", "contamination", "corruption",
        "entitlement", "reparation", "irregularity", "exceptions", "uncopyrightable", "propulsion",
        "instigation", "filibustering"]
        I3_L1 = ["ring", "panic", "police", "rifle", "bills", "nail", "push", "you", "are", "awful",
        "single", "alone", "hard", "wonky", "coma", "funky", "leave", "youlldie", "runaway", "off",
        "gnome", "boxer", "deliver", "box", "weld", "well", "hire", "high", "trance", "fugue", "siren"]
        I3_L2 = ["unload", "anxiety", "depression", "irrational", "yourealone", "insanity", "voices", "hardened",
        "reputation", "president", "slavery", "practice", "grammatically", "incorrect", "soluable", "shivering",
        "tendency", "onslaught", "constipation", "glee", "naive", "criminal", "debtor", "gentle", "polish"]
        I3_L3 = ["dictionary", "interdependency", "sacrifice", "utilitarianism", "independent", "monstrosity",
        "helllloooooooooooo", "embarrassed", "supercritical", "yourlovedones", "hescomingsoon", "marketplace",
        "apocalypse", "supernova", "industrialization", "greenhouse", "latitudinal", "deception", "equilibrium"]
        words = []

        words += I1_L1
        our_word = "|"
        self.word = random.choice(words)
        self.strike_count = 0

        self.welcome_jingle.play(loops=0)
        self.myfont = pygame.font.Font("Sprites//times.ttf", 40)
        self.strike = pygame.image.load("Sprites//strike.png").convert_alpha()
        self.strike = pygame.transform.scale(self.strike, (40, 40))

        difficulty = {0: '005 030', 1: '010 035', 2: '015 060', 3: '020 060', 4: '025 060', 5: '010 30', 6: '015 35', 7: '010 025', 8: '020 050', 9: '025 050', 10: '030 050'}
        diff_str = difficulty[Controller.done_counter[5]]
        print(diff_str)
        left_count = int(diff_str[0:3])
        time_limit = int(diff_str[4:])

        running = True
        while running:
            self.window.blit(self.background, (0,0))
            Controller.score(self, self.window, (255,255,255))
            Controller.insanity_meter(self, self.window, (255,255,255))
            Controller.clock(self, self.window, (240, 93, 93), time_limit, self.start_tick)
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
