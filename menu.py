import pygame
import time
import random
class Menu:
    def __init__(self):
        '''
           inits the menu
        '''
        init = pygame.init()
        self.window = pygame.display.set_mode((800,600))
        self.title = pygame.image.load("Sprites//titlecard.png").convert()
        self.start_button_unpressed = pygame.image.load("Sprites//start1.png").convert()
        self.start_button_pressed = pygame.image.load("Sprites//start2.png").convert()
        self.instruct_button_unpressed = pygame.image.load("Sprites//instruct1.png").convert()
        self.instruct_button_pressed = pygame.image.load("Sprites//instruct2.png").convert()
        # Method Calls
        self.background()
        self.title_pic()
        self.running = True
        # Main Menu Loop
        while self.running:
            for event in pygame.event.get():
                # Quit button
                if event.type == pygame.QUIT:
                    self.running = False

                # Keybinds
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                self.buttons()
                pygame.display.flip()

    def background(self):
        '''
           creates background
        '''
        x1 = random.randint(0, 255)
        x2 = random.randint(0, 255)
        x3 = random.randint(0, 255)
        self.window.fill((x1,x2,x3))
    def title_pic(self):
        '''
           blits title image onto surface
        '''
        self.window.blit(self.title, (200,100))
    def button_method(self, blit1, blit2, x1, x2, y1, y2, unpressed, pressed):
        """
           method for creating buttons
        """
        unpressed = pygame.transform.scale(unpressed, (126, 60))
        pressed = pygame.transform.scale(pressed, (126, 60))
        self.window.blit(unpressed, (blit1, blit2))
        mouse_posx = pygame.mouse.get_pos()[0]
        mouse_posy = pygame.mouse.get_pos()[1]
        if mouse_posx < x1 and mouse_posx > x2 and mouse_posy > y1 and mouse_posy < y2:
            self.window.blit(pressed, (blit1,blit2))
            return True
    def buttons(self):
        # Start button
        y = self.button_method(100,400,226,100,400,460, self.start_button_unpressed, self.start_button_pressed)
        x = pygame.mouse.get_pressed()
        if x[0] == 1 and y == True:
            print("test complete")
        # Instruction button
        y = self.button_method(300,400,426,300,400,460, self.instruct_button_unpressed, self.instruct_button_pressed)
        x = pygame.mouse.get_pressed()
        if x[0] == 1 and y == True:
            print("test complete")
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render('Some Text', False, (0, 0, 0))
            self.window.blit(textsurface,(0,0))


    def quit(self):
        pass
    def setting(self):
        pass
# test
