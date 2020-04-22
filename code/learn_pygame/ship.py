import pygame

class Ship():

    def __init__(self,screen):
        """
        初始化飞船并设定初始位置
        """

        self.screen = screen
        self.image = pygame.image.load(r"resource\alienInvasion\ship.bmp")

        self.image.set_colorkey((255,255,255))
        # 这个设置可以使图片的白色背景编程透明的
        
        self.rect = self.image.get_rect()
        self.scree_rect = screen.get_rect()

        # 置于底部中央
        self.rect.centerx = self.scree_rect.centerx
        self.rect.bottom = self.scree_rect.bottom

        # 设置初始的移动状态
        self.moving_right = False

    def blitme(self):
        """
        图像绘制再指定位置
        """
        
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right == True:
            self.rect.centerx += 1
