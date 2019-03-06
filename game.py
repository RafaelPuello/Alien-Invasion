"""Main module for the Space Invasion game"""

try:
    import sys
    import pygame
    from settings import Settings
    from objects import Ship, Barrier
    from game_functions import (check_events, update_screen,
                                update_objects)

except ImportError as error:
    sys.exit("Couldn't load module.  {}".format(error))

def main():
    """Set up main loop for game"""
    pygame.init()
    clock = pygame.time.Clock()

    settings = Settings()
    screen = settings.screen
    ship = Ship(screen)
    bullets = pygame.sprite.Group()
    barrier = pygame.sprite.Group(Barrier(screen, 1), Barrier(screen, 2),
                                  Barrier(screen, 3), Barrier(screen, 4))

    while True:
        check_events(ship, bullets)
        update_objects(ship, bullets, barrier)
        update_screen(settings, ship, barrier, bullets)
        clock.tick(60)

if __name__ == '__main__':
    main()
