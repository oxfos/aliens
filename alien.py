import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to model the alien"""

    def __init__(self, ai_game):
        """Initialization of an ALien instance"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
    
    def update(self):
        """Move the alien to the right."""
        self.rect.x += self.settings.alien_speed