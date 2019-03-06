"""Module used for holding unit tests"""

import pytest
import pygame
from objects import Ship
from settings import Settings

class TestShipMethods():
    """Class used to test the various methods of the user controlled ship"""

    def setup_class(self):
        pygame.init() # pylint: disable=no-member
        settings = Settings()
        self.test_ship = Ship(settings.screen) 
    
    def test_ship_doesnt_leave_screen(self):
        self.test_ship.rect.move_ip(1000, 0)
        self.test_ship.rect.clamp_ip(self.test_ship.screen_rect)
        assert(self.test_ship.screen_rect.contains(self.test_ship.rect))

    def teardown_class(self):
        del self.test_ship
        pygame.quit() # pylint: disable=no-member

