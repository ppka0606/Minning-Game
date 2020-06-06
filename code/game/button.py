import os
import pygame
import pygame.color

from const import Const


class Button():
    """
    pygame中没有提供Button类，之后需要多次引用该功能，
    所以在这里自己封装一个
    其实这里的功能更加类似于label，因为鼠标按钮的事件与它是分开进行的
    """

    def __init__(self, screen, text, **kwargs):
        self.screen = screen
        self.text = text

        self.width = kwargs.get("width", 200)
        self.height = kwargs.get("height", 50)
        self.color = kwargs.get("button_color", Const.COLOR_BLUE)
        self.text_color = kwargs.get("text_color", Const.COLOR_WHITE)
        self.posx = kwargs.get("posx", (Const.SCREEN_WIDTH - self.width) // 2)
        self.posy = kwargs.get("posy", (Const.SCREEN_HEIGHT - self.height) // 2)
        fontsize= kwargs.get("fontsize", 48)

        self.font = pygame.font.Font(r"resource\mingingGame\font\simsun.ttc", fontsize)

        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)

        self.prep_text()
    
    def prep_text(self):
        """
        先将text渲染为图像，然后插入到按钮上
        """
        self.message_image = self.font.render(self.text, True, self.text_color, self.color)
        self.message_rect = self.message_image.get_rect()
        self.message_rect.center = self.rect.center
    
    def blit_button(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.message_image, self.message_rect)

    def update_text(text):
        self.text = text
        self.prep_text()

    def in_area(self, posx, posy):
        """
        判断是否再按钮区域内
        """
        return (self.posx <= posx and self.posx + self.width >= posx and self.posy <= posy and self.posy + self.height >= posy)

    def change_text_color(self, text_color):
        """
        改变颜色，在选中某些选项时可能会使用
        """
        self.text_color = text_color
        self.prep_text()