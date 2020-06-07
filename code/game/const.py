class Const():
    """
    定义供全局使用的常数
    """
    MAX_VALUE = 10000000
    MIN_VALUE = -10000000

    MAZE_WIDTH_SQUARE = 37
    MAZE_HEIGHT_SQUARE = 29 # 迷宫的长宽方格数

    MAZE_DISPLAY_WIDTH_SQUARE = 15
    MAZE_DISPLAY_HEIGHT_SQUARE = 11
    MAZE_SQUARE_PIXEL = 40
    MAZE_ROAD = 1
    MAZE_WALL = 0 

    PLAYER_WIDTH_PIXEL = 30
    PLAYER_HEIGHT_PIXEL = 30

    MAZE_REGION_SIZE_DICT = {1 : 7, 2 : 5, 3 : 3}
        # KEY为迷宫的难度等级,VALUE为对应等级的迷宫一块区域最大的长宽跨度(单位:格数)
    MAZE_REGION_NUMBER_DICT = {1 : 8, 2 : 15, 3 : 30}
        # KEY为难度等级,VALUE为对应等级下的区域数目

    GAME_SURFACE_WIDTH = MAZE_SQUARE_PIXEL * MAZE_WIDTH_SQUARE
    GAME_SURFACE_HEIGHT = MAZE_SQUARE_PIXEL * MAZE_HEIGHT_SQUARE

    SCREEN_HEIGHT = 640
    SCREEN_WIDTH = 800

    # 游戏运行时的主要区域的起始坐标
    GAME_INTERFACE_MAINAREA_POSX = (SCREEN_WIDTH - MAZE_SQUARE_PIXEL * MAZE_DISPLAY_WIDTH_SQUARE) // 2 
    GAME_INTERFACE_MAINAREA_POSY = (SCREEN_HEIGHT - MAZE_SQUARE_PIXEL * MAZE_DISPLAY_HEIGHT_SQUARE) // 2 

    COLOR_WHITE     = (255, 255, 255)
    COLOR_BLACK     = (0,   0,   0  )
    COLOR_BLUE      = (0,   0,   255)
    COLOR_RED       = (255, 0,   0  )
    COLOR_GREEN     = (0,   255, 0  )
    COLOR_LIGHTGRAY = (220, 220, 220)
    COLOR_DARKGRAY  = (210, 210, 210)

    CLOCK_FPS = 25

    PLAYER_SPEED = ( (MAZE_WIDTH_SQUARE - 2) * MAZE_SQUARE_PIXEL / CLOCK_FPS / 15, (MAZE_HEIGHT_SQUARE - 2) * MAZE_SQUARE_PIXEL / CLOCK_FPS / 20, (MAZE_HEIGHT_SQUARE - 2) * MAZE_SQUARE_PIXEL / CLOCK_FPS / 25) # 三种人物，速度为走完横向距离分别用时15s，20s，25s

    IMAGE_PLAYER1_ICON_PATH = r"resource\mingingGame\game\player1_2.png"
    IMAGE_PLAYER2_ICON_PATH = r"resource\mingingGame\game\player2_2.png"
    IMAGE_PLAYER3_ICON_PATH = r"resource\mingingGame\game\player3_2.png"
        # 以上三个为在主界面展示的图标，不是在游戏过程中使用的素材

    IMAGE_TIMEDIAMOND_PATH = r"resource\mingingGame\game\timediamond.bmp"
    IMAGE_SCOREDIAMOND_PATH = r"resource\mingingGame\game\scorediamond.bmp"

    IMAGE_WALL_PATH = r"resource\mingingGame\game\stonewall.bmp"
    IMAGE_ROAD_PATH = r"resource\mingingGame\game\soil.bmp"
    def __init__(self):
        pass