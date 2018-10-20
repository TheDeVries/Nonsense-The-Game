import pygame
pygame.init()

class Club:
    def __init__(self):
        self.running = True
        self.window = pygame.display.set_mode((800, 600))
        self.club_background = pygame.image.load("Sprites//club.png").convert()
        self.bar2 = pygame.image.load("Sprites//empty_bar.png").convert()
        self.bar_woman = pygame.image.load("Sprites//bar_woman.png").convert()
        self.bar_man = pygame.image.load("Sprites//bar_man.png").convert()
        self.bar_man2 = pygame.image.load("Sprites//bar_man2.png").convert()
        while self.running == True:
            for event in pygame.event.get():
                # Quit button
                if event.type == pygame.QUIT:
                    self.running = False

                # Keybinds
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            self.window.blit(self.club_background, (0,0))

            self.bar_man2.set_colorkey((255,255,255))
            self.bar_man2 = pygame.transform.scale(self.bar_man2, (250, 500))
            self.window.blit(self.bar_man2, (500, 30))

            self.bar_woman.set_colorkey((255,255,255))
            self.bar_woman = pygame.transform.scale(self.bar_woman, (250,500))
            self.window.blit(self.bar_woman, (375, 90))

            self.bar_man.set_colorkey((255,255,255))
            self.bar_man = pygame.transform.scale(self.bar_man, (250, 500))
            self.window.blit(self.bar_man, (250, 150))

            self.bar2.set_colorkey((0,0,64))
            self.window.blit(self.bar2, (200, 300))

            pygame.display.flip()
