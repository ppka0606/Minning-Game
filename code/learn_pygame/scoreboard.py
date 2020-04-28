import pygame.font

class ScoreBoard(object):
    """
    计分板类,用于显示分数
    """

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        """
        将文字渲染为图像
        """
        rounded_score = int(round(self.stats.score, -1))
            # 将得分按3位一段显示出来
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.background_color)

        # 置于右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        