import os
import pygame
import pygame.color

class Button():
    """
    pygame中没有提供Button类，之后需要多次引用该功能，
    所以在这里自己封装一个
    """

    def __init__(self, screen, text, **kwargs):
        self.screen = screen
        self.text = text
        
        self.width = kwargs.get("width", 200)
        self.height = kwargs.get("height", 50)
        self.color = kwargs.get("button_color", pygame.color.BLUE)
        self.text_color = kwargs.get("text_color", pygame.color.WHITE)

        fontsize= kwargs.get("fontsize", 48)
        self.font = pygame. font.SysFont(None, fonstize)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
    
    def prep_text(self):
        """
        先将text渲染为图像，然后插入到按钮上
        """
        self.message_image = self.font.render(self.text, True, self.text_color, self.color)
        self.message_rect = self.message_image.get_rect()
        self.message_rect.center = self.rect.center
    
    def blit_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_rect, )