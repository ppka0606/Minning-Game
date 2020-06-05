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

    def __init__(self, screen, text, posx, posy, **kwargs):
        self.screen = screen
        self.text = text
        self.posx = posx
        self.posy = posy

        self.width = kwargs.get("width", 200)
        self.height = kwargs.get("height", 50)
        self.color = kwargs.get("button_color", Const.COLOR_BLUE)
        self.text_color = kwargs.get("text_color", Const.COLOR_WHITE)

        fontsize= kwargs.get("fontsize", 48)
        self.font = pygame. font.SysFont(None, fontsize)

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.prep_text()
    
    def prep_text(self):
        """
        先将text渲染为图像，然后插入到按钮上
        """
        self.message_image = self.font.render(self.text, True, self.text_color, self.color)
        self.message_rect = self.message_image.get_rect()
        self.message_rect.center = self.rect.center
    
    def blit_button(self):
        # self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.message_image, (self.posx, self.posy))

    def update_text(text):
        self.text = text
        self.prep_text()