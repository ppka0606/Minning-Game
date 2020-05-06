def Maze():
    """
    生成迷宫(仅限(0,1)数组)并返回对象
    迷宫的图形界面绘制将在其他类中完成
    """
    def __init__(self, level):
        """
        生成指定等级的迷宫
        """
        self.level = level
        self.map = []
        self.create_map()

    def get_map(self):
        return self.map
    
    def create_map(self):
        """
        按一定算法生成一个迷宫并存储在map中
        """
        # 现在具体要求还没有出来,还不知道迷宫是导入还是直接填写一个二维数组
        pass
        

