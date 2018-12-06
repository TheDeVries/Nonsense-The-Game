import pygame
import random
import json
from controller import *

class End:
    def __init__(self):
        pygame.init()
        self.start_tick = pygame.time.get_ticks()
        self.window = pygame.display.set_mode((800,600))
        self.c_title = pygame.image.load("Sprites//c_titlecard.png").convert()
        self.c_title.set_colorkey((255,255,255))
        self.font = pygame.font.Font("Sprites//times.ttf", 45)
        a_string = "You have gone insane."
        self.position = (190, 225)
        self.mode = 1
        self.plural = "s"
        self.running = True
        while self.running == True:
            self.window.fill((0,0,0))
            self.sec = int((pygame.time.get_ticks()-self.start_tick)/1000)
            #Mode one is our display sequence of events
            if self.mode == 1:
                self.display_message = self.font.render(a_string, True, (240, 93, 93))
                if self.sec > 3 and self.sec < 5:
                    a_string = ""
                elif self.sec > 5 and self.sec < 13:
                    if Controller.score_current < 2 and Controller.score_current != 0:
                        self.pural = ""
                    a_string = "You cleared " + str(Controller.score_current) + " scene" + self.plural + "."
                elif self.sec > 12:
                    a_string = ""
                    if self.sec > 14:
                        #Add to a local highscore json file before displaying final screen
                        
                        fptr = open("highscore.json")
                        data = fptr.read()
                        print(data)
                        fptr.close()
                        '''
                        pdata = json.loads(data)
                        pdata.append(Controller.score_current)
                        pdata = json.dumps(pdata)
                        fptr = open("people.json", "w")
                        data = fptr.write(pdata)
                        fptr.close()
                        '''
                        
                        infile = open("highscore.json", "r")
                        our_list = []
                        for line in infile:
                            our_list.append(line[:-1])
                        our_list.sort()
                        print(our_list)
                        
                        self.mode = 2
                self.window.blit(self.display_message, self.position)
            elif self.mode == 2:
                pygame.draw.ellipse(self.window, (255,255,255), (150, 50, 500, 250))
                self.window.blit(self.c_title, (200,100))
                self.display_message

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

            pygame.display.flip()
