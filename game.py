"""Main module for the Space Invasion game"""

try:
    import sys
    import pygame
    from objects import Ship, Barrier, Projectile, Alien, Settings
    from game_functions import (check_events, update_screen,
                                update_objects, create_aliens)

except ImportError as error:
    sys.exit("Couldn't load module.  {}".format(error))

def main():
    """Set up main loop for game"""
    pygame.init()
    clock = pygame.time.Clock()

    settings = Settings()
    screen = settings.screen
    ship = Ship(screen)
    aliens = create_aliens(screen)
    projectiles = pygame.sprite.Group()
    barriers = pygame.sprite.Group(Barrier(screen, 1), Barrier(screen, 2),
                                  Barrier(screen, 3), Barrier(screen, 4))

    while True:
        check_events(screen, ship, projectiles)
        update_objects(ship, projectiles, barriers)
        update_screen(settings, ship, barriers, projectiles, aliens)
        clock.tick(60)

if __name__ == '__main__':
    main()
