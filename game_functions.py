"""Module used to hold functions for the game"""

import sys
import pygame
from pygame.locals import *
from objects import Projectile

def check_events(screen, ship, projectiles):
    """Function used to check for user inputs"""
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                ship.moving_right = True
            if event.key == K_LEFT:
                ship.moving_left = True
            if  event.key == K_SPACE:
                projectile = Projectile(screen, ship)
                projectiles.add(projectile)
        elif event.type == KEYUP:
            ship.moving_right = False
            ship.moving_left = False

def update_objects(ship, projectile, barriers):
    """Function used to update the state of the objects"""
    ship.update()
    projectile.update()
    barriers.update()

def update_screen(settings, ship, barriers, projectiles):
    """Function used to update the state of the screen"""
    settings.screen.blit(settings.background, (0, 0))
    ship.draw_ship()
    barriers.draw(settings.screen)
    projectiles.draw(settings.screen)
    pygame.display.flip()
