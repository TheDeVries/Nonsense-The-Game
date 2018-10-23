import pygame
pygame.init()
class Maze:
    tile_size = 96
    map_height = 2
    map_width = 3
    def __init__(self):
        self.running = True
        self.wn = pygame.display.set_mode((800,600))
        self.player = pygame.image.load("Sprites//character_walk.png")
        self.mountain = pygame.image.load("Sprites//grass_mount1.png")
        self.grass = pygame.image.load("Sprites//grass.png")
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
            self.map_build()
            pygame.display.flip()
    def map_build(self):
        textures = {"1":self.mountain, "2":self.grass}
        map_list = [["1", "1", "1"],
              ["2", "2", "2"]]
        for rows in range(Maze.map_height):
            for colums in range(Maze.map_width):
                self.wn.blit(textures[map_list[rows][colums]], (colums*Maze.tile_size, rows*Maze.tile_size))
