"""Module used to hold the settings for the game"""

import sys
import pygame

class Settings(): # pylint: disable=too-few-public-methods
    """Class used to initialize the settings for the game"""

    def __init__(self):
        """Initialize screen, display, and background"""
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 682))
        pygame.display.set_caption("Space Invaders")
        
        # Create and blit background to screen
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((40, 40, 40))
        self.screen.blit(self.background, (0, 0))

        # Create title and blit to screen
        self.font = pygame.font.SysFont("futura", 36, bold=True)
        self.text = self.font.render("Space Invasion!", 1, (7, 183, 83))
        self.textpos = self.text.get_rect(centerx=self.background.get_width()/2)
        self.background.blit(self.text, self.textpos)
        pygame.display.flip()
