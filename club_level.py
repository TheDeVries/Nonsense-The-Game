import pygame
pygame.init()

class Club:
    def __init__(self):
        self.running = True
        self.window = pygame.display.set_mode((800, 600))
        self.club_background = pygame.image.load("Sprites//club.png").convert()
        self.bar = pygame.image.load("Sprites//empty_bar.png").convert()
        self.bar_woman = pygame.image.load("Sprites//bar_woman.png").convert()
        self.bar_woman2 = pygame.image.load("Sprites//bar_woman2.png").convert()
        self.bar_man = pygame.image.load("Sprites//bar_man.png").convert()
        self.bar_man2 = pygame.image.load("Sprites//bar_man2.png").convert()
        while self.running == True:
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
            self.window.blit(self.club_background, (0,0))

            self.bar_woman2.set_colorkey((255,255,255))
            self.bar_woman2 = pygame.transform.scale(self.bar_woman2, (250, 500))
            self.window.blit(self.bar_woman2, (575, 30))

            self.bar_man2.set_colorkey((255,255,255))
            self.bar_man2 = pygame.transform.scale(self.bar_man2, (250, 500))
            self.window.blit(self.bar_man2, (450, 90))

            self.bar_woman.set_colorkey((255,255,255))
            self.bar_woman = pygame.transform.scale(self.bar_woman, (250,500))
            self.window.blit(self.bar_woman, (325, 150))

            self.bar_man.set_colorkey((255,255,255))
            self.bar_man = pygame.transform.scale(self.bar_man, (250, 500))
            self.window.blit(self.bar_man, (200, 210))

            self.bar.set_colorkey((0,0,64))
            self.window.blit(self.bar, (200, 300))
            pygame.display.flip()
