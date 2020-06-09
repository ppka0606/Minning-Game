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
    MAZE_FLAG = 2
    MAZE_TIMEDIAMOND = 3
    MAZE_SCOREDIAMOND = 4

    PLAYER_WIDTH_PIXEL = 30
    PLAYER_HEIGHT_PIXEL = 30

    MAZE_REGION_SIZE_DICT = {1 : 7, 2 : 5, 3 : 3}
        # KEY为迷宫的难度等级,VALUE为对应等级的迷宫一块区域最大的长宽跨度(单位:格数)
    MAZE_REGION_NUMBER_DICT = {1 : 8, 2 : 15, 3 : 30}
        # KEY为难度等级,VALUE为对应等级下的区域数目

    TIME = {1 : 999, 2 : 150, 3 : 180}

    GAME_SURFACE_WIDTH = MAZE_SQUARE_PIXEL * MAZE_DISPLAY_WIDTH_SQUARE
    GAME_SURFACE_HEIGHT = MAZE_SQUARE_PIXEL * MAZE_DISPLAY_HEIGHT_SQUARE




    SCREEN_HEIGHT = 640
    SCREEN_WIDTH = 800

    # 显示概率分布图的常数
    DISTRIBUTION_PIXEL = 15
    DISTRIBUTION_WIDTH = DISTRIBUTION_PIXEL * MAZE_WIDTH_SQUARE
    DISTRIBUTION_HEIGHT = DISTRIBUTION_PIXEL * MAZE_HEIGHT_SQUARE
    DISTRIBUTION_POSX = (SCREEN_WIDTH - DISTRIBUTION_WIDTH) // 2
    DISTRIBUTION_POSY = (SCREEN_HEIGHT - DISTRIBUTION_HEIGHT) // 2


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
    COLOR_YELLOW1   = (255, 255, 224)
    COLOR_YELLOW2   = (238, 238, 209)
    COLOR_YELLOW3   = (205, 205, 180)
    COLOR_YELLOW4   = (139, 139, 122)
    COLOR_YELLOW5   = (255, 255, 0  )

    CLOCK_FPS = 25

    PLAYER_SPEED = ( (MAZE_WIDTH_SQUARE - 2) * MAZE_SQUARE_PIXEL / CLOCK_FPS / 7, (MAZE_HEIGHT_SQUARE - 2) * MAZE_SQUARE_PIXEL / CLOCK_FPS / 12, (MAZE_HEIGHT_SQUARE - 2) * MAZE_SQUARE_PIXEL / CLOCK_FPS / 10) # 三种人物，速度为走完横向距离分别用时7s，12s，10s

    PLAYER_RATE = (0.05, 0.07, 0.08)
    SCORE_RATE = 0.8 # 生成得分宝石的概率越大，时间宝石的概率越小


    IMAGE_PLAYER1_ICON_PATH = r"resource\mingingGame\game\player1_2.png"
    IMAGE_PLAYER2_ICON_PATH = r"resource\mingingGame\game\player2_2.png"
    IMAGE_PLAYER3_ICON_PATH = r"resource\mingingGame\game\player3_2.png"
        # 以上三个为在主界面展示的图标，不是在游戏过程中使用的素材

    IMAGE_TIMEDIAMOND_PATH = r"resource\mingingGame\game\timediamond.bmp"
    IMAGE_SCOREDIAMOND_PATH = r"resource\mingingGame\game\scorediamond.bmp"

    IMAGE_WALL_PATH = r"resource\mingingGame\game\stonewall.bmp"
    IMAGE_ROAD_PATH = r"resource\mingingGame\game\soil.bmp"
    IMAGE_FLAG_PATH = r"resource\mingingGame\game\flag.bmp"
    IMAGE_ROAD_SCOREDIAMOND_PATH = r"resource\mingingGame\game\soil_scorediamond.bmp"
    IMAGE_ROAD_TIMEDIAMOND_PATH = r"resource\mingingGame\game\soil_timediamond.bmp"

    PROGRESSBAR_WIDTH = 120
    PROGRESSBAR_SPEED = (2000, 1000, 1500) # 分别挖矿用时为2s，1s，1.5s

    def __init__(self):
        pass