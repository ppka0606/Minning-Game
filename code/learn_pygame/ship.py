import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        """
        初始化飞船并设定初始位置
        """

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load(r"resource\alienInvasion\ship.bmp")

        self.image.set_colorkey((255,255,255))
            # 这个设置可以使图片的白色背景编程透明的
        
        self.rect = self.image.get_rect()
        self.scree_rect = screen.get_rect()

        # 置于底部中央
        self.rect.centerx = self.scree_rect.centerx
        self.rect.bottom = self.scree_rect.bottom

        self.center = float(self.rect.centerx)
            # 存储非整数值(因为rect的centerx等属性只能存储int,所以需要特殊处理)

        # 设置初始的移动状态
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """
        图像绘制再指定位置
        """
        
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right == True:
            self.center += self.ai_settings.ship_speed_factor
        
        if self.moving_left == True:
            self.center -= self.ai_settings.ship_speed_factor

        # 使用存储了float类型的center属性来更新rect对象
        self.rect.centerx = self.center
            # 可以试想一下,每次center存储的是准确值,而赋给rect.centerx后只会保留整数部分
            # 相当于用"3像素/2帧"的效果实现了"1.5像素/帧"的预期速度
            # 由于1像素很小,每次移动距离很大,所以在移动时可能产生的0.5像素的偏差就无关紧要了