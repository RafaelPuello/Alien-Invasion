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
                if len(projectiles) < 10: # Limit user projectiles
                    projectile = Projectile(ship)
                    projectiles.add(projectile)
        elif event.type == KEYUP:
            ship.moving_right = False
            ship.moving_left = False

def update_objects(ship, projectile, barriers):
    """Function used to update the state of the objects"""
    ship.update()
    projectile.update()
    barriers.update()

def update_screen(settings, ship, barriers, projectiles, aliens):
    """Function used to update the state of the screen"""
    for projectile in projectiles.copy():
            if projectile.rect.bottom <= 0:
                 projectiles.remove(projectile)
    settings.screen.blit(settings.background, (0, 0))
    ship.draw_ship()
    barriers.draw(settings.screen)
    projectiles.draw(settings.screen)
    aliens.draw(settings.screen)
    pygame.display.flip()
