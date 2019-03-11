"""Module used to hold functions for the game"""

import sys
import pygame
from pygame.locals import *
from objects import Projectile, Alien

def create_aliens(screen):
    """Function used to create a 5 X 10 alien set"""
    aliens = pygame.sprite.Group()
    for row_location in range(0, 150, 30):
        for column_location in range(0, 500, 50):
            alien = Alien(screen)
            alien.rect.x += column_location
            alien.rect.y += row_location
            aliens.add(alien)
    return aliens

def start_menu():
    """Function used to start menu"""
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_RETURN:
                return False
        return True

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
                if len(projectiles) < 4: # Limit user projectiles
                    projectile = Projectile(ship)
                    projectiles.add(projectile)
        elif event.type == KEYUP:
            ship.moving_right = False
            ship.moving_left = False

def update_objects(ship, projectiles, barriers, aliens, score):
    """Function used to update the state of the objects"""
    for projectile in projectiles.sprites():
        if projectile.rect.bottom <= 0:
            projectiles.remove(projectile)
    for alien in aliens.sprites():
        if alien.screen_check():
            Alien.direction *= -1
            for alien in aliens.sprites():
                alien.rect.y += 5
    if len(aliens) <= 35 and len(aliens) > 20:
        Alien.speed = 2
    elif len(aliens) <= 20:
        Alien.speed = 3
    pygame.sprite.groupcollide(projectiles, aliens, True, True)
    ship.update()
    projectiles.update()
    barriers.update()
    aliens.update()
    score.update(projectiles, aliens)

def update_screen(settings, ship, barriers, projectiles, aliens, score):
    """Function used to update the screen"""
    settings.screen.blit(settings.background, (0, 0))
    ship.draw_ship()
    barriers.draw(settings.screen)
    aliens.draw(settings.screen)
    projectiles.draw(settings.screen)
    score.draw(settings)
    pygame.display.flip()
