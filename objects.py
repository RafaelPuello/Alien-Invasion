"""Module used to hold the game objects"""

import os
import pygame

def load_image(name):
    """Function to get image from working directory and return something"""
    fullname = os.path.join('images', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    return image


class Ship(pygame.sprite.Sprite):
    """Class used for player spaceship"""

    def __init__(self, screen):
        """Initialize user spaceship"""
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = load_image("spaceship.bmp")
        self.rect = self.image.get_rect(midbottom=(512, 750))
 
    def update(self):
        """Move the ship depending user input"""

    def move_left(self):
        """Move the user ship left if the player presses the left arrow key"""
        self.rect.move_ip(-55, 0)

    def move_right(self):
        """Move the user ship right if the player presses the right arrow key"""
        self.rect.move_ip(55, 0)
