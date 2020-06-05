

class Status():
    """
    用于详细记录游戏中各种状态信息
    以此决定各种行为
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

    def __init__(self):
        """
        初始化游戏状态
        """
        self.interface = self.INTERFACE_LOGIN
        self.level = self.LEVELBEGIN
        self.player = r"Input player name:"
        self.map = None
        self.distribution = None


if __name__ == "__main__":
    a = Status()