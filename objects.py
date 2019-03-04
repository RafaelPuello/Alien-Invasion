"""Module used to hold the game objects"""

import os
import pygame

def load_image(name):
    """Function to get image from working directory and return something"""
    fullname = os.path.join('images', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    return image, image.get_rect()


class Ship(pygame.sprite.Sprite): # pylint: disable=too-few-public-methods
    """Class used for player spaceship"""

    def __init__(self, screen):
        """Initialize user spaceship"""
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("spaceship.png")


    def update(self):
        """Move the ship depending user input"""
