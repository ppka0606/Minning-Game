class Settings():
    def __init__(self):
        """
        存储一些常数,便于跨文件引用
        """

        # 背景设置
        self.screen_width = 800
        self.screen_height = 640
        self.background_color = (230,230,230)
        self.ship_speed_factor = 1.5

        # 设置子弹的属性
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 13
            # 允许同时存在于屏幕的子弹数量上限

        # alien
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
            # 1:  --> ; -1:  <--