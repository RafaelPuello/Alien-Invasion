"""Module used for holding unit tests"""

import pygame
from objects import Ship, Settings

class TestShipMethods():
    """Class used to test the various methods of the user controlled ship"""

    def setup_class(self):
        """Method is used to setup the ship class and settings"""
        pygame.init() # pylint: disable=no-member
        settings = Settings()
        self.test_ship = Ship(settings.screen)

    def test_ship_doesnt_leave_screen(self):
        """Method to test that ship doesn't leave the screen"""
        self.test_ship.rect.move_ip(1000, 0)
        self.test_ship.rect.clamp_ip(self.test_ship.screen_rect)
        assert self.test_ship.screen_rect.contains(self.test_ship.rect)

    def teardown_class(self):
        """Method used to clean up after tests"""
        del self.test_ship
        pygame.quit() # pylint: disable=no-member
