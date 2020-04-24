import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load(r"resource\alienInvasion\alien.bmp")
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
