import pygame

class Maze:
    def __init__(self):
        self.running = True
        self.wn = pygame.display.set_mode((800,600))
        while self.running:
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
