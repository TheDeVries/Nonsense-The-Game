import pygame
import random
from controller import *
pygame.init()

class Space:
    def __init__(self, running = True, isJump = False, jumpCount = 10, x = 50, y = 440):
        self.x = x
        self.y = y
        self.running = running
        self.isJump = isJump
        self.jumpCount = jumpCount
        self.win = pygame.display.set_mode((800,600))
        self.image = pygame.image.load("Sprites//THEspaceship.png")
        self.background = pygame.image.load("Sprites//space background.png")
        self.win.blit(self.background, (0,0))
        self.win.blit(self.image, (self.x,self.y))
        self.speed = 5
        pygame.display.update()

        while self.running:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # keys = pygame.key.get_pressed()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

                    if event.key == pygame.K_LEFT: #and x > speed:
                        self.x -= self.speed

                    if event.key == pygame.K_RIGHT: #and x < 500 - width - speed:
                        self.x += self.speed

                    if event.key == pygame.K_UP: #and y > speed:   #y < speed and y < 800 - height - speed limits character to only left and right
                        self.y -= self.speed
                    if not (self.isJump):
                        if event.key == pygame.K_DOWN: #and y < 500 - height - speed:
                            self.y += self.speed

                        if event.key == pygame.K_SPACE:
                            self.isJump = True


                    else:
                        if self.jumpCount >= -10:
                            self.neg = 1
                            if self.jumpCount < 0:
                                self.neg = -1 #used to move downwards after jump
                            self.y -= (self.jumpCount ** 2) * 0.5 * self.neg
                            self.jumpCount -= 1
                            self.y
                        else:
                            self.isJump = False
                            self.jumpCount = 10
