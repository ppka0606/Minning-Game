class Const():
    """
    定义供全局使用的常数
    """
    maze_width_square = 37
    maze_height_square = 29 
        # 迷宫的长宽方格数
    maze_region_max_size_dict = {1 : 9, 2 : 7, 3 : 5}
        # key为迷宫的难度等级,value为对应等级的迷宫一块区域最大的长宽跨度(单位:格数)
    maze_region_number_dict = {1 : 10, 2 : 17, 3 : 30}
        # key为难度等级,value为对应等级下的区域数目

    def __init__(self):
        pass