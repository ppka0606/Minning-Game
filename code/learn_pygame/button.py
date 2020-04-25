import pygame.font

class Button():

    def __init__(self, ai_settings, screen, message):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的属性
        # 这个游戏中只设置一个开始按钮，所以就将所有的常数项直接存入类中了
        self.width = 200
        self.height = 50
        self.button_color =  (255, 0, 0)
        self.text_colot = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
            # 设置字体

        # 创建按钮的rect对象并居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_message(message)
    
    def prep_message(self,message):
        """
        需要先将message渲染为图像,然后在按钮的矩形框上居中显示
        """
        self.message_image = self.font.render(message, True, self.text_colot, self.button_color)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)
