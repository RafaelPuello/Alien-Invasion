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
        """Initialize the user spaceship"""
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = load_image("spaceship.bmp")
        self.rect = self.image.get_rect(midbottom=(512, 750))
        self.speed = 1.5
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ship based on user input"""
        if self.moving_left:
            self.rect.move_ip(-15*self.speed, 0)

        if self.moving_right:
            self.rect.move_ip(15*self.speed, 0)
        self.rect.clamp_ip(self.screen_rect)

    def draw_ship(self):
        """Blit ship to screen"""
        self.screen.blit(self.image, self.rect)


class Barrier(pygame.sprite.Sprite): # pylint: disable=too-few-public-methods
    """Class used for green barriers"""

    def __init__(self, screen, number=1):
        """Intialize instances of barriers"""
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = load_image("barrier.bmp")
        self.rect = self.image.get_rect()
        if number == 1:
            self.rect.center = (75, 575)
        elif number == 2:
            self.rect.center = (200, 575)
        elif number == 3:
            self.rect.center = (325, 575)
        else:
            self.rect.center = (450, 575)


class Projectile(pygame.sprite.Sprite):
    """Class used for projectiles"""

    def __init__(self, ship):
        """Intialize instances of bullet"""
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("projectile.bmp")
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top
        self.vertical_pos = float(self.rect.y)
        self.speed = 20

    def update(self):
        """Update position of projectile"""

        self.vertical_pos -= self.speed
        self.rect.y = self.vertical_pos


class Alien(pygame.sprite.Sprite):
    """Class used to for enemies"""

    def __init__(self, screen):
        """Initialize instances of Aliens"""
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = load_image("alien.bmp")
        self.rect = self.image.get_rect()
        self.speed = 1.5
        self.rect.center = (10, 100)