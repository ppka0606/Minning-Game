import pygame

class Image():
    """
    以此为父类创建图像的管理
    """
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        
        self.image.set_colorkey((255,255,255))
        self._rect = self.image.get_rect()
        
        self._posx = 0
        self._posy = 0

    def blit_image(self):
        self.screen.blit(self.image, self._rect)
    
