"""Module used to hold functions for the game"""

import sys
import pygame

def check_events(ship, bullets):
    """Function used to check for user inputs"""
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.locals.K_LEFT:
                ship.moving_left = True
            if  event.key == pygame.locals.K_SPACE:
                bullets.update()
        elif event.type == pygame.locals.KEYUP:
            ship.moving_right = False
            ship.moving_left = False

def update_objects(ship, bullets, barrier):
    """Function used to update the state of the objects"""
    ship.update()
    bullets.update()
    barrier.update()

def update_screen(settings, ship, barrier, bullets):
    """Function used to update the state of the screen"""
    settings.screen.blit(settings.background, (0, 0))
    ship.draw_ship()
    barrier.draw(settings.screen)
    pygame.display.flip()
