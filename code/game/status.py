from button import Button
from const import Const
from player import Player

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
    INTERFACE_RESULT = 5                # 结算界面，显示总分以及历史最高分

    LEVELBEGIN = 0
    LEVEL1 = 1
    LEVEL2 = 2
    LEVEL3 = 3

    PLAYER1 = 1
    PLAYER2 = 2
    PLAYER3 = 3


    def __init__(self, screen):
        """
        初始化游戏状态
        """
        self.screen = screen

        self.interface = self.INTERFACE_LOGIN
        self.level = self.LEVELBEGIN
        self.user = r"Input player name:"

        # 方向键状态，表明是否有一直按下某个键
        self.key_right = False
        self.key_left = False
        self.key_up = False
        self.key_down = False

        self.map = None
        self.distribution = None
        self.add_buttons()

        self.player_kind = 1

        self.player = None

    def add_buttons(self):
        self.buttons = {}

        self.buttons["score"] = Button(self.screen, "Score: 00000", posx = 0, posy = 0, fontsize = 24) # 添加左上角分数按钮

        self.buttons["time"] = Button(self.screen, "Time: 000s",posx = Const.SCREEN_WIDTH - 130, posy = 0, width = 130,fontsize = 24) # 右上角剩余时间
        
        self.buttons["start"] = Button(self.screen, "开始游戏", posy = 250, fonsize = 40)
        self.buttons["help"] = Button(self.screen, "帮助菜单" , posy = 350, fontsize = 40)

        self.buttons["pause"] = Button(self.screen, "暂 停", width = 120, height = 40, posx = Const.SCREEN_WIDTH - 120, posy = Const.SCREEN_HEIGHT -40, fontsize = 30)

        self.buttons["exit_yes"] = Button(self.screen, "确认退出", width = 120,height = 40, posx = 200)
        self.buttons["exit_no"] = Button(self.screen, "返回菜单" , width = 120, height = 40, posx =480)
