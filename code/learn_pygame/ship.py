-*- coding:utf-8 -*-
import pygame

class Ship():

    def __init__(self,screen):
        """
        初始化飞船并设定初始位置
        """

        self.screen = screen
        self.image = pygame.image.load("resource\alienInvasion\ship.bmp")
        self.rect = self.image.get_rect()
        self.scree_rect = screen.get_rect()
        
        # 置于底部中央
        self.rect.centerx = self.scree_rect.centerx
        self.rect.bottomleft = self.scree_rect.bottomleft

    def blitme(self):
        """
        图像绘制再指定位置
        """
        
        self.screen.blit(self.image,self.rect)
