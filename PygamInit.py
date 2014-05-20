'''
Purpose of gfx is to initialize the gfx
'''
import pygame, sys # imports the pygame module and the sys module
from pygame.locals import * # locals is a dictionary with a lot of stuff

#initializes the graphics
def gfx_init():
    pygame.init() # initializes all imported pygame modules
    DISPLAYSURF = pygame.display.set_mode((1280, 1024)) # sets a 1280x1024 window
    pygame.display.set_caption('Dinomuncher USA') # sets the caption in the top left
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()