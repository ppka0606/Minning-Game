class GameStats():
    """
    追踪游戏内的得分等信息
    """

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
            # 游戏按下开始以后再激活

    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit