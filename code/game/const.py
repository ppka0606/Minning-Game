class Const():
    """
    定义供全局使用的常数
    """
    MAZE_WIDTH_SQUARE = 37
    MAZE_HEIGHT_SQUARE = 29 # 迷宫的长宽方格数
    MAZE_SQUARE_PIXEL = 16
    MAZE_ROAD = 1
    MAZE_WALL = 0 

    MAZE_REGION_SIZE_DICT = {1 : 7, 2 : 5, 3 : 3}
        # KEY为迷宫的难度等级,VALUE为对应等级的迷宫一块区域最大的长宽跨度(单位:格数)
    MAZE_REGION_NUMBER_DICT = {1 : 8, 2 : 15, 3 : 30}
        # KEY为难度等级,VALUE为对应等级下的区域数目

    GAME_SURFACE_WIDTH = MAZE_SQUARE_PIXEL * MAZE_WIDTH_SQUARE
    GAME_SURFACE_HEIGHT = MAZE_SQUARE_PIXEL * MAZE_HEIGHT_SQUARE

    SCREEN_HEIGHT = 640
    SCREEN_WIDTH = 800

    # 游戏运行时的主要区域的起始坐标
    GAME_INTERFACE_MAINAREA_POSX = (SCREEN_WIDTH - MAZE_SQUARE_PIXEL * MAZE_WIDTH_SQUARE) / 2 
    GAME_INTERFACE_MAINAREA_POSY = (SCREEN_HEIGHT - MAZE_SQUARE_PIXEL * MAZE_HEIGHT_SQUARE) / 2 

    COLOR_DEFAULT_BACKGROUND = (0, 0, 0)
    COLOR_WHITE = (255, 255, 255)
    COLOR_BLACK = (0,   0,   0  )
    COLOR_BLUE  = (0,   0,   255)
    COLOR_RED   = (255, 0,   0  )

    CLOCK_FPS = 30
    def __init__(self):
        pass