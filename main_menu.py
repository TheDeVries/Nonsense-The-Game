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
        self.quit_button_unpressed = pygame.image.load("Sprites//quit1.png").convert()
        self.quit_button_pressed = pygame.image.load("Sprites//quit2.png").convert()
        self.setting_button_unpressed = pygame.image.load("Sprites//settings1.png").convert()
        self.setting_button_pressed = pygame.image.load("Sprites//settings2.png").convert()
        # Method Calls
        our_color = self.background()
        x = 0
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

            x -= 1
            rel_x = x % 800
            self.window.fill(our_color)
            self.window.blit(self.menu_background, (rel_x - 800, 0))
            if rel_x < 800:
                self.window.blit(self.menu_background, (rel_x, 0))
            self.title_pic()
            self.buttons()
            pygame.display.flip()

    def background(self):
        '''
           creates background
        '''
        x1 = random.randint(0, 255)
        x2 = random.randint(0, 255)
        x3 = random.randint(0, 255)
        rand_color = (x1,x2,x3)
        self.window.fill((x1,x2,x3))
        self.menu_background = pygame.image.load("Sprites//movingbackground.png").convert()
        self.menu_background.set_colorkey((255,255,255))
        self.window.blit(self.menu_background, (0, 0))
        return rand_color

    def title_pic(self):
        '''
           blits title image onto surface
        '''
        self.title.set_colorkey((255,255,255))
        self.window.blit(self.title, (200,100))
    def text(self, x, y, z, a):
        myfont = pygame.font.SysFont('Times New Roman', z)
        textsurface = myfont.render(a, True, (0, 0, 0))
        self.window.blit(textsurface,(x,y))
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
        y = self.button_method(37,400,163,37,400,460, self.start_button_unpressed, self.start_button_pressed)
        x = pygame.mouse.get_pressed()
        self.text(47,410,60,"Start")
        if x[0] == 1 and y == True:
            print("test complete")
        # Instruction button
        y = self.button_method(237,400,363,237,400,460, self.instruct_button_unpressed, self.instruct_button_pressed)
        x = pygame.mouse.get_pressed()
        self.text(262,410,60,"Info")
        if x[0] == 1 and y == True:
            instruct = Instructions()
            self.running = False
        # Quit button
        y = self.button_method(437,400,563,437,400,460, self.setting_button_unpressed, self.setting_button_pressed)
        x = pygame.mouse.get_pressed()
        self.text(462,420,30,"Settings")
        if x[0] == 1 and y == True:
            set = Settings()
            self.running = False

        #Settings button
        y = self.button_method(637,400,763,637,400,460, self.quit_button_unpressed, self.quit_button_pressed)
        x = pygame.mouse.get_pressed()
        self.text(652,410,60,"Quit")
        if x[0] == 1 and y == True:
            self.running = False


    def quit(self):
        pass
    def setting(self):
        pass
class Instructions:
    def __init__(self):
        self.window = pygame.display.set_mode((800,600))
        self.running = True
        Menu.background(self)

        # Main Menu Loop
        while self.running:
            for event in pygame.event.get():
                # Quit button
                if event.type == pygame.QUIT:
                    foo = Menu()
                    self.running = False

                # Keybinds
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        bar = Menu()
                        self.running = False

                self.instruct()

                pygame.display.flip()
    def instruct(self):
        myfont = pygame.font.SysFont('Times New Roman', 30)
        textsurface = myfont.render('Instructions: Example instructions...', True, (0, 0, 0))
        self.window.blit(textsurface,(0,0))
class Settings:
    res = (800, 600)
    def __init__(self):
        self.window = pygame.display.set_mode(Settings.res)
        self.running = True
        Menu.background(self)
        self.res_button_unpressed = pygame.image.load("Sprites//res1.png").convert()
        self.res_button_pressed = pygame.image.load("Sprites//res2.png").convert()

        # Main Menu Loop
        while self.running:
            for event in pygame.event.get():
                # Quit button
                if event.type == pygame.QUIT:
                    foo = Menu()
                    self.running = False

                # Keybinds
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        bar = Menu()
                        self.running = False
                self.res_buttons()


                pygame.display.flip()
    def res_buttons(self):
        y = Menu.button_method(self, 37,400,163,37,400,460, self.res_button_unpressed, self.res_button_pressed)
        x = pygame.mouse.get_pressed()
        Menu.text(self, 47,410,60,"1000 by 750")
        if x[0] == 1 and y == True:
            Settings.res = (1000, 750)
