"""Main module for the Space Invasion game"""

try:
    import sys
    import pygame
    from pygame.locals import *
    from settings import Settings
    from objects import Ship

except ImportError as error:
    sys.exit("Couldn't load module.  {}".format(error))
 

def main():
    """Set up main loop for game"""
    pygame.init() # pylint: disable=no-member
    clock= pygame.time.Clock()

    settings = Settings()
    ship = Ship(settings.screen)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    ship.move_right()
                if event.key == K_LEFT:
                    ship.move_left()
                if  event.key == K_SPACE:
                    continue
                    #ship.fire_bullet()

        settings.screen.blit(settings.background, (0, 0))
        settings.screen.blit(ship.image, ship.rect)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
