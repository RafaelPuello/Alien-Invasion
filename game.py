"""Main module for the Space Invasion game"""

try:
    import sys
    import pygame
    from pygame.locals import *
    from settings import Settings
    from objects import Ship, Barrier

except ImportError as error:
    sys.exit("Couldn't load module.  {}".format(error))
 

def main():
    """Set up main loop for game"""
    pygame.init() # pylint: disable=no-member
    clock= pygame.time.Clock()

    settings = Settings()
    screen = settings.screen
    ship = Ship(screen)
    barrier = pygame.sprite.Group(Barrier(screen, 1), Barrier(screen, 2),
                                  Barrier(screen, 3), Barrier(screen, 4))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.quit() # pylint: disable=no-member
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    ship.moving_right = True
                if event.key == K_LEFT:
                    ship.moving_left = True
                if  event.key == K_SPACE:
                    continue
                    #ship.fire_bullet()
            elif event.type == KEYUP:
                ship.moving_right = False
                ship.moving_left = False

        settings.screen.blit(settings.background, (0, 0))
        ship.draw_ship()
        ship.update()
        barrier.draw(settings.screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
