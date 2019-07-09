import pygame

class Ship:


    def __init__(self,screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        # Load the ship
        self.image = pygame.image.load('images/alienblaster.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Movement flag
        self.moving_right = False

        # Places the ship at the center bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)