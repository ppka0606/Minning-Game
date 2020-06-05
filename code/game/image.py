import pygame

class Image():
    """
    以此为父类创建图像的管理
    """
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        
        self.image.set_colorkey((255,255,255))
        # self._rect = self.image.get_rect()

    def blit_image(self, screen, posx, posy):
        screen.blit(self.image, (posx,posy))
    
class ImageWall(Image):
    """
    迷宫的墙的图片
    """
    def __init__(self):
        super(ImageWall, self).__init__(r"resource\mingingGame\game\stonewall.bmp")

class ImageSoil(Image):
    """
    迷宫的地面图片
    """
    def __init__(self):
        super(ImageSoil, self).__init__(r"resource\mingingGame\game\soil.bmp")