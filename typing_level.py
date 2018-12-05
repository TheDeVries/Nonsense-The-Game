import pygame
import random
from controller import *
pygame.init()

class Typing:
    total_words = 5
    time_limit = 35
    I1_L1 = ["cat", "tractor", "monkey", "boat", "house", "man", "hat", "run",
    "elephant", "mouse", "computer", "pick", "deep", "sports", "fruit",
    "ocean", "money", "game", "snake", "car", "factory", "food", "family", "the",
    "host", "pantry", "tag", "flag", "plant", "noun", "bank", "joke"]
    I1_L2 = ["receipt", "instructions", "development", "civilization", "etiquette",
    "mispronunciation", "success", "advertisement", "commercial", "residential",
    "education", "industrial", "excellence", "guarantee", "typing", "one-hundred",
    "concealed", "envelope", "kangaroo", "biscuit", "melon", "ghost", "month"]
    I1_L3 = ["copyrightable", "supercalifragilisticexpialidocious", "uninitiated",
    "righteous", "engineering", "resolution", "disappear", "emancipation", "establishment"
    "titration", "responsibilities", "environmental", "satisfactory", "hovercraft"]
    I2_L1 = ["bogus", "heart", "head", "shoulder", "knees", "toes", "and", "wall",
    "dark", "light", "floor", "roof", "ceiling", "gnat", "bug", "fly", "dot", "excuses",
    "koala", "gong", "tower", "wires", "wad", "lake", "shallow", "moon", "bash", "fist", "pop",
    "zone", "kite", "bite", "flimsy", "son", "rig", "mitten", "lisp", "shower", "mutter"]
    I2_L2 = ["condemnation", "vibrato", "candy", "image", "malfunction", "idol", "stupid",
    "greed", "power", "ghost", "leer", "singed", "quirky", "hunter", "backslash", "backlash",
    "snapshot", "jungle", "racing", "demolition", "flowers", "giant", "garden"]
    I2_L3 = ["infatuation", "revelation", "revolution", "buoyancy", "contamination", "corruption",
    "entitlement", "reparation", "irregularity", "exceptions", "uncopyrightable", "propulsion",
    "instigation", "filibustering", "lamentation", "compounding", "rebounding", "relapsing"]
    I3_L1 = ["ring", "panic", "police", "rifle", "bills", "nail", "push", "you", "are", "awful",
    "single", "alone", "hard", "wonky", "coma", "funky", "leave", "youlldie", "runaway", "off",
    "gnome", "boxer", "deliver", "box", "weld", "well", "hire", "high", "trance", "fugue", "siren", "beef",
    "grind", "loop", "cheese", "breach", "popcorn", "rough", "coin", "coil", "choir", "shine"]
    I3_L2 = ["unload", "anxiety", "depression", "irrational", "yourealone", "insanity", "voices", "hardened",
    "reputation", "president", "slavery", "practice", "grammatically", "incorrect", "soluable", "shivering",
    "tendency", "onslaught", "constipation", "glee", "naive", "criminal", "debtor", "gentle", "polish"]
    I3_L3 = ["dictionary", "interdependency", "sacrifice", "utilitarianism", "independent", "monstrosity",
    "helllloooooooooooo", "embarrassed", "supercritical", "yourlovedones", "hescomingsoon", "marketplace",
    "apocalypse", "supernovas", "industrialization", "greenhouses", "latitudinal", "deception", "equilibrium", "protection"]
    I4_L1 = ["die", "crust", "blip", "hike", "lost", "pod", "crop", "suck", "wasp", "zombie", "down", "drown",
    "heel", "combustion", "kale", "love", "dealer", "needle", "cradle", "beetle", "leech", "tentacle", "yeast",
    "saint", "lob", "bridge", "craft", "sack", "aged", "wreck", "wrench", "spoon", "bulge", "corrode", "void", "god",
    "soap", "mud", "bubble", "vista", "jade", "patch", "bolt", "sun", "twist", "sign", "cleave", "suds"]
    I4_L2 = ["ass", "frightening", "betrayal", "inconsistency", "derivative", "spine", "collar", "mortal",
    "divine", "enlighten", "pastel", "blood", "labor", "firefly", "nuclear", "dehydrated", "smallpox", "plague",
    "normality", "creep", "expectation", "common", "habitat", "misophonia", "citation", "disorderly"]
    I4_L3 = ["antidisestablishmentarianism", "robust", "decadence", "grandparents", "loathesome", "similarities",
    "conductivity", "poisonous", "obnoxious", "overlord", "hescomingrunwhileyoustillcan", "injustices", "getoutofhere",
    "considerations", "accomodations", "citadel", "demonic", "destruction", "invasion", "taxation", "palace"]
    I5_L1 = ["hush", "little", "baby", "dont", "say", "a", "word", "mommas", "gonna", "buy", "you", "rocking", "bird",
    "sleep", "goat", "devil", "twinkle", "star", "wonder", "what", "are", "frugality", "python", "hell", "devil", "liability",
    "bribery", "token", "salvage", "surrender", "this", "instant", "kill", "murder", "broke", "ruination", "prod", "alcohol",
    "fool", "divorce", "dim", "drip", "pulp", "luck", "ape", "pig", "maul"]
    I5_L2 = ["ivory", "malfunction", "assassination", "improvisation", "tiles", "arsonist", "psychological", "surrealism",
    "hahahahahahahahahahahahahahahahahahhahahahah", "gray", "pale", "lifeless", "flesh", "sin", "loneliness", "homeless", "oppressed",
    "forever", "deprived", "of", "necessities", "intolerance", "thousands", "wanderers", "hopelessness", "fate", "unhinged", "backwards", "divorce"]
    I5_L3 = ["decapitation", "dehumanization", "willpower", "allhopeislost", "youcantwinthisgameyouknow", "ddagweggaeg", "plmidffeddargh", "scissors",
    "potency", "wweeiirrdd", "gamethisis", "whyareyoustillplaying", "puppet", "werewolf", "vampire", "professorstevenallenmoore", "eeegfgfgfgfggfgfgfgf",
    "locket", "verilyisaytoyou", "m", "a", "d", "n", "e", "s", "copingmechanism", "plaque", "wound", "atlantiansarestupid", "suckitourprojectisthebest"]
    def __init__(self):
        self.start_tick = pygame.time.get_ticks()
        self.completions = Controller.done_counter[5]
        #Sounds
        self.window = pygame.display.set_mode((800,600))
        if Controller.insanity < 3:
            if Controller.insanity == 1:
                self.welcome_jingle = pygame.mixer.Sound("Sounds//computer_magic.wav")
            if Controller.insanity == 2:
                jin_chance = random.randint(0,4)
                if jin_chance < 2:
                    self.welcome_jingle = pygame.mixer.Sound("Sounds//computer_magic.wav")
                else:
                    self.welcome_jingle = pygame.mixer.Sound("Sounds//computer_magic2.wav")
        elif Controller.insanity >= 3:
            if Controller.insanity == 3:
                jin_chance = random.randint(0,4)
                if jin_chance < 2:
                    self.welcome_jingle = pygame.mixer.Sound("Sounds//computer_magic2.wav")
                else:
                    self.welcome_jingle = pygame.mixer.Sound("Sounds//distortion1.wav")
            else:
                self.welcome_jingle = pygame.mixer.Sound("Sounds//distortion1.wav")
        self.check = pygame.mixer.Sound("Sounds//check.wav")
        self.check2 = pygame.mixer.Sound("Sounds//check2.wav")
        self.striked = pygame.mixer.Sound("Sounds//Buzzer.wav")

        #Sprites
        self.background = pygame.image.load("Sprites//Pro Typing.png").convert()
        self.walmart = pygame.image.load("Sprites//walmart.png").convert()

        #Initialize display and controller variables
        self.words = []
        self.difficultify(self.words)
        #Below, the first int in the string is the number of words and the second is the time in seconds
        #difficulty = {0: '005 030', 1: '010 035', 2: '015 060', 3: '020 060', 4: '025 060', 5: '010 30', 6: '015 35', 7: '010 025', 8: '020 050', 9: '025 050', 10: '030 050'}
        #self.handler = 0

        our_word = "|"
        self.word = random.choice(self.words)
        self.strike_count = 0

        self.welcome_jingle.play(loops=0)
        self.myfont = pygame.font.Font("Sprites//times.ttf", 40)
        self.strike = pygame.image.load("Sprites//strike.png").convert_alpha()
        self.strike = pygame.transform.scale(self.strike, (40, 40))

        self.left_count = Typing.total_words
        self.time_limit = Typing.time_limit

        running = True
        while running:
            self.window.blit(self.walmart, (0,0))
            self.window.blit(self.background, (0,0))
            if Controller.insanity == 5:
                self.background.set_colorkey((19, 108, 78))
            Controller.score(self, self.window, (255,255,255))
            Controller.insanity_meter(self, self.window, (255,255,255))
            Controller.clock(self, self.window, (240, 93, 93), self.time_limit, self.start_tick)
            display_word = self.myfont.render(self.word, True, (0, 0, 0))
            display_line = self.myfont.render(">", True, (0,0,0))
            display_cursor = self.myfont.render("|", True, (0,0,0))
            self.window.blit(display_word, (270, 405))
            self.window.blit(display_line, (10, 475))
            display_count = self.myfont.render(str(self.left_count), True, (0,0,0))
            self.window.blit(display_count, (574, 210))
            if self.strike_count == 1:
                self.window.blit(self.strike, (574, 335))
            elif self.strike_count == 2:
                self.window.blit(self.strike, (574, 335))
                self.window.blit(self.strike, (624, 335))
            elif self.strike_count >= 3:
                Controller.transition(self, 5, False)
            l = len(our_word)

            if self.left_count == 0:
                Controller.transition(self, 5, True)

            for event in pygame.event.get():
                Controller.basic_command(self, event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if our_word[0:l-1] == self.word:
                            self.left_count -= 1
                            if self.left_count % 10 == 0 and self.left_count != 0:
                                self.check2.play(loops=0)
                            elif self.left_count != 0:
                                self.check.play(loops=0)
                        else:
                            self.strike_count += 1
                            if self.strike_count != 3:
                                self.striked.play(loops = 0)
                        self.word = random.choice(self.words)
                        our_word = "|"
                    elif event.key == pygame.K_BACKSPACE:
                        our_word = our_word[0:(l-2)]
                        our_word += "|"
                    else:
                        our_key = self.myfont.render(chr(event.key), True, (0,0,0))
                        our_word = our_word[0:(l-1)]
                        our_word += chr(event.key)
                        our_word += "|"
            display_ours = self.myfont.render(our_word, True, (0,0,0))
            self.window.blit(display_ours, (40, 475))

            pygame.display.flip()
    def difficultify(self, words):
        self.words = words
        self.handler = 0
        if self.completions % 2 == 0 and self.completions != 0:
            Typing.total_words += 5
            Typing.time_limit += 10
        else:
            Typing.time_limit -= 5
        if (self.completions % 10) + 1 == 1:
            if self.completions >= 11:
                self.handler = 10
                if self.completions >= 21:
                    self.handler = 20
        if Controller.insanity == 1:
            self.words += Typing.I1_L1
            if self.handler >= 10:
                self.words += Typing.I1_L2
                if self.handler == 20:
                    self.words += Typing.I1_L3
        elif Controller.insanity == 2:
            self.words += Typing.I2_L1
            if self.handler >= 10:
                self.words += Typing.I2_L2
                if self.handler == 20:
                    self.words += Typing.I2_L3
        elif Controller.insanity == 3:
            self.words += Typing.I3_L1
            if self.handler >= 10:
                self.words += Typing.I3_L2
                if self.handler == 20:
                    self.words += Typing.I3_L3
        elif Controller.insanity == 4:
            self.words += Typing.I4_L1
            if self.handler >= 10:
                self.words += Typing.I4_L2
                if self.handler == 20:
                    self.words += Typing.I4_L3
        elif Controller.insanity == 5:
            self.words += Typing.I5_L1
            if self.handler >= 10:
                self.words += Typing.I5_L2
                if self.handler == 20:
                    self.words += Typing.I5_L3
        return self.words