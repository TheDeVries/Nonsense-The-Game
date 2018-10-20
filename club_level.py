import pygame
pygame.init()

#Must still make into a class, in the meantime it functions on its own.

class Club:
    def __init__(self, sanity):
        pass

def main():

    running = True
    while running:
        window = pygame.display.set_mode((800, 600))
        club_background = pygame.image.load("Sprites//club.png").convert()
        bar2 = pygame.image.load("Sprites//empty_bar.png").convert()
        bar_man = pygame.image.load("Sprites//bar_man.png").convert()
        window.blit(club_background, (0,0))
        bar_man.set_colorkey((255,255,255))
        bar_man = pygame.transform.scale(bar_man, (250, 500))
        window.blit(bar_man, (250, 150))
        bar2.set_colorkey((0,0,64))
        window.blit(bar2, (200, 300))


        for event in pygame.event.get():
            # Quit button
            if event.type == pygame.QUIT:
                running = False

            # Keybinds
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.flip()

main()
