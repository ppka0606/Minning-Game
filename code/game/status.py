from button import Button
from const import Const
from player import Player
from image import Image
from maze import Maze

class Status():
    """
    用于详细记录游戏中各种状态信息
    以此决定各种行为
    同时管理各个组件，因此会在此创建所有可能使用的对象的引用
    """
    INTERFACE_LOGIN = 0                 # 登录界面
    INTERFACE_GAME = 1                  # 游戏中
    INTERFACE_PAUSE = 2                 # 暂停界面
    INTERFACE_HELP = 3                  # 帮助菜单
    INTERFACE_CONFIRM_EXIT = 4          # 确认退出
    INTERFACE_RESULT = 5                # 结算界面分
    INTERFACE_RESTART = 6               # 某一关gameover后重开

    LEVELBEGIN = 0
    LEVEL1 = 1
    LEVEL2 = 2
    LEVEL3 = 3

    PLAYERBEGIN = 0
    PLAYER1 = 1
    PLAYER2 = 2
    PLAYER3 = 3


    def __init__(self, screen):
        """
        初始化游戏状态
        """
        self.screen = screen

        self.interface = self.INTERFACE_LOGIN
        self.close = False
        self.level = self.LEVELBEGIN
        self.user = r"Input player name:"

        # 方向键状态，表明是否有一直按下某个键
        self.key_right = False
        self.key_left = False
        self.key_up = False
        self.key_down = False

        self.maze = None
        self.distribution = None
        self.add_buttons()

        self.player_kind = self.PLAYERBEGIN

        self.player = None
        self.images = {}
        self.add_images()

    def levelup(self):
        self.level += 1
        self.maze = Maze(self.level).map
        self.player = Player(self.player_kind, self.maze)

    def add_buttons(self):
        self.buttons = {}
        # 退出界面
        self.buttons["ask_exit"] = Button(self.screen, "确认退出?", height = 60, text_color = Const.COLOR_RED, fontsize = 48, button_color = Const.COLOR_DARKGRAY, posy = 220)
        self.buttons["confirm_exit"] = Button(self.screen, "确认", height = 50, text_color = Const.COLOR_BLACK, button_color = Const.COLOR_DARKGRAY, posy = 400, posx = 150, fontsize = 36)
        self.buttons["cancel_exit"] = Button(self.screen, "取消", height = 50, text_color = Const.COLOR_BLACK, button_color = Const.COLOR_DARKGRAY, posy = 400, posx = 450, fontsize = 36, selected_color = Const.COLOR_BLUE)

        # 开始界面
        self.buttons["start"] = Button(self.screen, "开始游戏", posy = 450, fontsize = 48, button_color = Const.COLOR_LIGHTGRAY, text_color = Const.COLOR_BLACK)
        self.buttons["help"] = Button(self.screen, "帮助菜单" , posy = 520, fontsize = 42, button_color = Const.COLOR_LIGHTGRAY, text_color = Const.COLOR_BLACK)
        self.buttons["player1"] = Button(self.screen, "饭团" , width =120, height = 40, posx = 110, posy = 270, button_color = Const.COLOR_LIGHTGRAY, text_color = Const.COLOR_GREEN, fontsize = 28, selected_color = Const.COLOR_BLUE)
        self.buttons["player2"] = Button(self.screen, "蛋黄" , width =120, height = 40, posx = 340, posy = 270, button_color = Const.COLOR_LIGHTGRAY, text_color = Const.COLOR_GREEN, fontsize = 28, selected_color = Const.COLOR_BLUE)
        self.buttons["player3"] = Button(self.screen, "栗子" , width =120, height = 40, posx = 570, posy = 270, button_color = Const.COLOR_LIGHTGRAY, text_color = Const.COLOR_GREEN, fontsize = 28, selected_color = Const.COLOR_BLUE)
        self.buttons["confirm_player"] = Button(self.screen, "选择角色后开始游戏", fonstize = 36, button_color = Const.COLOR_DARKGRAY, text_color = Const.COLOR_BLUE, posy = 350, fontsize = 28, width = 260)

        # 帮助界面
        self.buttons["help_title"] = Button(self.screen, "帮 助", posy = 50, fontsize = 48, button_color = Const.COLOR_LIGHTGRAY, text_color = Const.COLOR_BLACK)
        self.buttons["return"] = Button(self.screen, "返回主界面", posy = 550, fontsize = 40, button_color = Const.COLOR_LIGHTGRAY, text_color = Const.COLOR_BLACK)
        self.buttons["introduction1"] = Button(self.screen, "移动速度快        移动速度慢      移动速度适中", posy = 250, posx = 110, width = 580, height = 50, button_color = Const.COLOR_LIGHTGRAY, text_color = Const.COLOR_BLACK, fontsize = 28)
        self.buttons["introduction2"] = Button(self.screen, "挖宝速度慢        挖宝速度快      挖宝速度适中", posy = 300, posx = 110, width = 580, height = 50, button_color = Const.COLOR_LIGHTGRAY, text_color = Const.COLOR_BLACK, fontsize = 28)
        self.buttons["introduction3"] = Button(self.screen, "   遇到宝石概率低        遇到宝石概率适中     遇到宝石概率逐渐提升", posy = 350, posx = 110, width = 580, height = 50, button_color = Const.COLOR_LIGHTGRAY, text_color = Const.COLOR_RED, fontsize = 22)
        self.buttons["introduction4"] = Button(self.screen, "使用键盘的方向键在迷宫中移动", posy = 420, posx = 110, width = 580, height = 40, button_color = Const.COLOR_DARKGRAY, text_color = Const.COLOR_BLACK, fontsize = 22)
        self.buttons["introduction5"] = Button(self.screen, "在规定时间内走到终点，并挖取尽可能多的宝石来提高分数!", posy = 460, posx = 110, width = 580, height = 40, button_color = Const.COLOR_DARKGRAY, text_color = Const.COLOR_BLACK, fontsize = 22)
        self.buttons["introduction6"] = Button(self.screen, "红色的宝石可以获得额外分数，绿色的宝石可以延长时间!", posy = 500, posx = 110, width = 580, height = 40, button_color = Const.COLOR_DARKGRAY, text_color = Const.COLOR_BLACK, fontsize = 22)

        # 重开界面
        self.buttons["gameover"] = Button(self.screen, "Game Over!", height = 60, text_color = Const.COLOR_RED, fontsize = 48, button_color = Const.COLOR_LIGHTGRAY, posy = 220)
        self.buttons["retry"] = Button(self.screen, "重玩本关", height = 50, text_color = Const.COLOR_BLACK, button_color = Const.COLOR_LIGHTGRAY, posy = 400, posx = 150, fontsize = 36, selected_color = Const.COLOR_BLUE)
        self.buttons["returnmain"] = Button(self.screen, "返回主界面", height = 50, text_color = Const.COLOR_BLACK, button_color = Const.COLOR_LIGHTGRAY, posy = 400, posx = 450, fontsize = 36, selected_color = Const.COLOR_BLUE)

        # 游戏界面
        self.buttons["score"] = Button(self.screen, "Score:00000", text_color = Const.COLOR_BLACK, button_color = Const.COLOR_LIGHTGRAY, fontsize = 32,posx = 0, posy = 0)
        self.buttons["time"] = Button(self.screen, "Time:000s", text_color =Const.COLOR_BLACK, button_color = Const.COLOR_LIGHTGRAY, width = 200, fontsize = 32, posy = 0, posx = Const.SCREEN_WIDTH - 200)
        self.buttons["num_scorediamond"] = Button(self.screen, "X000", text_color = Const.COLOR_BLACK, button_color = Const.COLOR_LIGHTGRAY,width = 60, fontsize = 32, posx = 60, posy = Const.SCREEN_HEIGHT - 76)
        self.buttons["num_timediamond"] = Button(self.screen, "X000", text_color = Const.COLOR_BLACK, button_color = Const.COLOR_LIGHTGRAY, width = 60, fontsize = 32, posx = 230, posy = Const.SCREEN_HEIGHT - 76)

    def add_images(self):
        self.images["icon1"] = Image(Const.IMAGE_PLAYER1_ICON_PATH)
        self.images["icon2"] = Image(Const.IMAGE_PLAYER2_ICON_PATH)
        self.images["icon3"] = Image(Const.IMAGE_PLAYER3_ICON_PATH)
        self.images["scorediamond"] = Image(Const.IMAGE_SCOREDIAMOND_PATH)
        self.images["timediamond"] = Image(Const.IMAGE_TIMEDIAMOND_PATH)
        self.images["road"] = Image(Const.IMAGE_ROAD_PATH)
        self.images["wall"] = Image(Const.IMAGE_WALL_PATH)
