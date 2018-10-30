import pygame
import random
pygame.font.init()

class Typing:
    def __init__(self):
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

        running = True
        while running:

            self.window = pygame.display.set_mode((800,600))
            self.window.fill((255,255,255))

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
                        print("enter")
                    else:
                        our_key = chr(event.key)
                        print(our_key)
            pygame.display.flip()

Typing()
