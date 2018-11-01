import pygame
import random
pygame.init()

class Typing:
    def __init__(self):
        #Sounds
        self.welcome_jingle = pygame.mixer.Sound("Sounds//Computer Magic.wav")
        self.chime = pygame.mixer.Sound("Sounds//Electronic_Chime.wav")
        self.check = pygame.mixer.Sound("Sounds//Check Mark.wav")

        self.ty_background = pygame.image.load("Sprites//Pro Typing.png")
        #S refers to Sanity and L to level of difficulty
        S1_L1 = ["cat", "tractor", "monkey", "boat", "house", "man", "hat", "run",
        "elephant", "mouse", "computer", "pick", "police", "sports", "fruit",
        "ocean", "money", "game", "snake", "car", "factory", "food", "family"]
        S1_L2_Words = ["receipt", "instructions", "development", "civilization", "etiquette",
        "mispronunciation", "success", "advertisement", "commercial", "residential",
        "education", "industrial", "excellence", "guarantee", "typing", "one-hundred",
        "concealed", "envelope", "kangaroo", "biscuit", "melon", "ghost", "month"]
        S1_L2_Sentences = ["See Spot Run!", "He is tall.", "I love my family.", "God bless America.",
        "All hail Plankton!", "The airport was unforgivably crowded.", "Obama is gone!"
        "I built an igloo in the snow.", "Her shirt was red.", "He's a good doctor. I'm gonna sue him."
        "Can I adjust the thermostat, please?", "You'd better not smoke in here!"]
        S1_L3_Words = ["copyrightable", "supercalifragilisticexpialidocious", "uninitiated",
        "righteous", "engineering", "resolution", "disappear", "emancipation", "establishment"
        "titration", "responsibilities", "environmental", "satisfactory", "hovercraft"]
        S1_L3_Sentences = ["Modern day bananas are actually cousins of original bananas. The 'banana plague' of the 1950s killed off all the real bananas, hence why banana-flavored candy doesn't taste like our bananas."
        "My disappointment is immeasurable and my day is ruined.", "The practice of taking someone else's work or ideas and passing them off as one's own.",
        "I am absolutely stupified right now. You have no idea."]
        words = []

        words += S1_L1
        our_word = "|"
        self.word = random.choice(words)
        self.strike_count = 0

        self.window = pygame.display.set_mode((800,600))
        self.welcome_jingle.play(loops=0)
        self.myfont = pygame.font.SysFont('Times New Roman', 40)
        self.strike = pygame.image.load("Sprites//strike.png").convert()
        self.strike = pygame.transform.scale(self.strike, (40, 40))
        self.strike.set_colorkey((0,0,0))
        left_count = 5

        running = True
        while running:

            self.window.blit(self.ty_background, (0,0))
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
                    elif event.key == pygame.K_RETURN:

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
