"""Main module for the Space Invasion game"""

try:
    import sys
    import pygame
    from settings import Settings
    from objects import Ship

except ImportError as error:
    sys.exit("Couldn't load module.  {}".format(error))
 

def main():
    """Set up main loop for game"""

    settings = Settings()
    ship = Ship(settings.screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pylint: disable=no-member
                return
        settings.screen.blit(settings.background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    main()
