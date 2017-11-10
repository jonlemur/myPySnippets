# using python 3x

import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

size = width, height = 400, 250
screen = pygame.display.set_mode(size)
screen.fill((200,200,200))
myfont = pygame.font.SysFont('Comic Sans MS', 30)

textsurface = myfont.render('Hello Pygame World', False, (250, 250, 250))
screen.blit(textsurface, (50, 90))

# Game loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.display.flip() # updates the screen




    