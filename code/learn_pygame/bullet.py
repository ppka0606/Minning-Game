import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    继承pygam中的Sprite类进行开发
    """

    def __init__(self, ai_settings, screen, ship):
        """
        从飞船所处的位置设定为子弹的初始位置
        ai_settings可视为一个常数包的实例化
        """
        super(Bullet, self).__init__()
            # Python 2.7 的语法格式
        self.screen = screen

        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
            # 和之前的类似,用一个额外变量来存储非整数类型的属性值
        
        self.color = ai_settings.bullet_color
        self.speed_factor =ai_settings.bullet_speed_factor

    def update(self):
        """
        子弹只需要向上移动就可以了
        同样的方法,用额外变量存储非整数数值
        """
        self.y -= self.speed_factor
        self.rect.y = int(self.y)


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        