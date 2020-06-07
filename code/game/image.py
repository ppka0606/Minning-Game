import pygame

class Image():
    """
    图像的管理
    """
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        
        self.image.set_colorkey((255,255,255))

        self.height = self.image.get_rect().height
        # self._rect = self.image.get_rect()

    def blit_image(self, screen, posx, posy):
        screen.blit(self.image, (posx,posy))
    