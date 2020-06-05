from button import Button
from const import Const

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

    def __init__(self, screen):
        """
        初始化游戏状态
        """
        self.screen = screen

        self.interface = self.INTERFACE_LOGIN
        self.level = self.LEVELBEGIN
        self.player = r"Input player name:"

        self.map = None
        self.distribution = None
        self.add_buttons()

    def add_buttons(self):
        self.buttons = []
        self.buttons.append(Button(self.screen, "Score: 00000", 0, 0, width = 250, fontsize = 36)) # 添加左上角分数按钮
        self.buttons.append(Button(self.screen, "Time: 000s", Const.SCREEN_WIDTH - 128, 0, fontsize = 36)) # 右上角剩余时间

if __name__ == "__main__":
    a = Status()