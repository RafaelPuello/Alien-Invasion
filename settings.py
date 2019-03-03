""" Module used to hold the settings for the game. """

try:
    import pygame
    import sys

except ImportError as error:
    sys.exit("Couldn't load module.  {}".format(error))

class Settings(): # pylint: disable=too-few-public-methods
    """ Class used to initialize the settings for the game."""

    def __init__(self):
        """ Initialize screen, display, and background. """

        pygame.init()
        self.screen = pygame.display.set_mode((1024, 682))
        pygame.display.set_caption("Space Invaders")

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((40, 40, 40))

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
