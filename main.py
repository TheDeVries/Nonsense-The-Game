import pygame
from menu import *
from maze_level import *
pygame.init()

def main():
    running = True
    # Main Game Loop
    while running:
        for event in pygame.event.get():
            # Quit button
            if event.type == pygame.QUIT:
                running = False

            # Keybinds
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            menu = Menu()

            # Updates Display Constantly
            pygame.display.flip()

main()
