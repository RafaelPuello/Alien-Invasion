""" Module used to hold the game objects. """

try:
    import pygame

except ImportError as error:
    sys.exit("Couldn't load module.  {}".format(error))


class UserShip(pygame.sprite.Sprite):
    """ Class used for player spaceship. """

    def __init__(self):
        """ Initialize user spaceship. """

        pygame.sprite.Sprite.__init__(self)
