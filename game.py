""" Main module for the Space Invasion game. """

try:
    import pygame
    import sys
    from settings import Settings

except ImportError as error:
    sys.exit("Couldn't load module.  {}".format(error))

def main():
    """ Set up main loop for game """

    settings = Settings()

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pylint: disable=no-member
                return
        settings.screen.blit(settings.background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    main()
