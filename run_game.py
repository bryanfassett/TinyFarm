import pygame
from pygame.constants import FULLSCREEN, RESIZABLE
from pygame.locals import *
from Game.Common import SpriteState
from Game.Components.SpriteSheet import *

# Initialize PyGAme
pygame.init()
SCREEN_W, SCREEN_H = 800, 600
canvas = pygame.Surface((SCREEN_W, SCREEN_H))
window = pygame.display.set_mode((SCREEN_W,SCREEN_H))
###################

# Test Code Here
actor = SpriteSheet("Character1")
animslist = actor.getAnimationList("Idle", SpriteState.DOWN)
animindex = 0
################

# PyGame Game Loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    canvas.fill((0,100,100))

    window.blit(canvas,(0,0))
    pygame.display.update()

##################