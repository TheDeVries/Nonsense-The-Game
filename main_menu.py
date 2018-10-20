import pygame
import time
import random
class Menu:
    res = (800,600)
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
        self.res_button_unpressed = pygame.image.load("Sprites//res1.png").convert()
        self.res_button_pressed = pygame.image.load("Sprites//res2.png").convert()
        self.song = pygame.mixer.music.load("Sounds//MenuMusic.mp3")
        # Method Calls
        our_color = self.background()
        pygame.mixer.music.play()
        i = 0
        self.running = True
        self.music = True
        self.menu_act = 0

        # Main Menu Loop
        while self.running:
            for event in pygame.event.get():
                # Quit button
                if event.type == pygame.QUIT:
                    if self.menu_act == 0:
                        self.running = False
                    elif self.menu_act == 1:
                        self.menu_act = 0
                    elif self.menu_act == 2:
                        self.menu_act = 0

                # Keybinds
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.menu_act == 0:
                            self.running = False
                        elif self.menu_act == 1:
                            self.menu_act = 0
                        elif self.menu_act == 2:
                            self.menu_act = 0

            #Scrolling Background Image
            i -= 1
            rel_x = i % 800
            self.window.fill(our_color)
            self.window.blit(self.menu_background, (rel_x - 800, 0))
            if rel_x < 800:
                self.window.blit(self.menu_background, (rel_x, 0))
            #Title and Buttons
            if self.menu_act == 0:
                self.title_pic()
                self.buttons()
            elif self.menu_act == 1:
                self.instruct()
            elif self.menu_act == 2:
                self.music_buttons()
            elif self.music == False:
                pygame.mixer.music.stop()



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
        pygame.draw.ellipse(self.window, (255,255,255), (150, 50, 500, 250))
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
            self.menu_act = 1
        # Quit button
        y = self.button_method(437,400,563,437,400,460, self.setting_button_unpressed, self.setting_button_pressed)
        x = pygame.mouse.get_pressed()
        self.text(462,420,30,"Settings")
        if x[0] == 1 and y == True:
            self.menu_act = 2
        #Settings button
        y = self.button_method(637,400,763,637,400,460, self.quit_button_unpressed, self.quit_button_pressed)
        x = pygame.mouse.get_pressed()
        self.text(652,410,60,"Quit")
        if x[0] == 1 and y == True:
            self.running = False
        #Credits button
        #I want to make it so that when the title card is clicked (or the oval behind it),
        #it 'flips over' and on the back it says our names and can be clicked to flip back again.
        #y = self.button_method(150, 50, 150, 50, )
    def instruct(self):
        myfont = pygame.font.SysFont('Times New Roman', 30)
        textsurface = myfont.render('Instructions: Example instructions...', True, (0, 0, 0))
        self.window.blit(textsurface,(0,0))
    def music_buttons(self):
        # Music on button
        y = self.button_method(237,400,363,237,400,460, self.res_button_unpressed, self.res_button_pressed)
        x = pygame.mouse.get_pressed()
        self.text(255,420,30,"Music On")
        if x[0] == 1 and y == True:
            self.music = True
        # Music off
        y = self.button_method(437,400,563,437,400,460, self.res_button_unpressed, self.res_button_pressed)
        x = pygame.mouse.get_pressed()
        self.text(455,420,30,"Music Off")
        if x[0] == 1 and y == True:
            self.music = False
