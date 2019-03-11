"""Module used to hold the game objects"""

import os
import pygame

def load_image(name):
    """Function to get image from working directory and return something"""
    fullname = os.path.join('images', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    return image

class Settings(): # pylint: disable=too-few-public-methods
    """Class used to initialize the settings for the game"""

    def __init__(self):
        """Initialize screen, display, and background"""
        self.screen = pygame.display.set_mode((550, 750))
        pygame.display.set_caption("Alien Invasion")
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((0, 0, 0))
        self.font = pygame.font.SysFont("futura", 36, bold=True)
        self.text = self.font.render("Alien Invasion!", 1, (7, 183, 83))
        self.text_position = self.text.get_rect(centerx=self.background.get_width()/2)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def set_menu(self):
        """Display menu until user presses enter or spacebar"""
        font = pygame.font.SysFont("futura", 36, bold=True)
        text = font.render("Alien Invasion!", 1, (7, 183, 83))
        textpos = text.get_rect(centerx=self.background.get_width()/2)
        self.background.blit(text, textpos)

    def set_game(self):
        """Display game"""
        return

class Ship(pygame.sprite.Sprite):
    """Class used for player spaceship"""

    def __init__(self, screen):
        """Initialize the user spaceship"""
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = load_image("ship.bmp")
        self.rect = self.image.get_rect(midbottom=(275, 700))
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ship based on user input"""
        if self.moving_left:
            self.rect.move_ip(-10, 0)

        if self.moving_right:
            self.rect.move_ip(10, 0)
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

    speed = 20
    def __init__(self, ship):
        """Intialize instances of bullet"""
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("projectile.bmp")
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top
        self.vertical_pos = float(self.rect.y)

    def update(self):
        """Update position of projectile"""

        self.vertical_pos -= Projectile.speed
        self.rect.y = self.vertical_pos


class Alien(pygame.sprite.Sprite):
    """Class used to for enemies"""

    direction = -1
    speed = 1
    def __init__(self, screen):
        """Initialize instances of Aliens"""
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = load_image("alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = (20, 0)

    def screen_check(self):
        """Check if any alien has made it to the edge of the screen"""
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien whenever called"""
        self.rect.x += Alien.speed * Alien.direction

class Score():
    """Class used for score tallying"""

    ammo_used = 0
    def __init__(self):
        """Initialize the score"""
        self.aliens_destroyed = []
        self.font = pygame.font.SysFont("futura", 24, True)
        self.text = self.font.render("Score: ", 1, (7, 183, 83))
        self.score_text = self.font.render("{}".format(Score.ammo_used), 1, (100, 100, 100))
        self.text_position = self.text.get_rect(bottomleft=(10,740))
        self.score_position = self.score_text.get_rect(bottomleft=(100, 740))

    def update(self, projectiles, aliens):
        """Update the user's score"""
        for projectile in projectiles.copy():
            self.aliens_destroyed.append(pygame.sprite.spritecollide(projectile, aliens, False))
            Score.ammo_used += 1

    def draw(self, settings):
        """Draw the score on the screen"""
        settings.background.blit(self.text, self.text_position)
        settings.background.blit(self.score_text, self.score_position)