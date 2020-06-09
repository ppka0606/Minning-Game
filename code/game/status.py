from random import randint
from copy import deepcopy

from button import Button
from const import Const
from player import Player
from image import Image
from maze import Maze
from timer import Timer


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
    INTERFACE_RESULT = 5                # 结算界面
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
        self.timer = Timer()
        self.progresstimer = Timer()

        self.progress_pause = False

        self.screen = screen

        self.interface = self.INTERFACE_LOGIN
        self.close = False
        self.checkmap = False
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

        self.time_left = 0.0
        self.time = 0.0

        self.timediamond = 0
        self.scorediamond = 0

        self.fillwidth = 0

    def levelup(self):
        """
        升级， 0-1-2-3循环
        """

        if self.level <= 2:
            self.level += 1
            self.maze,self.distribution = Maze(self.level).map
            self.place_diamond()
            self.maze_copy = deepcopy(self.maze)
            self.player = Player(self.player_kind, self.maze)
            # self.player.initpos()

            self.time = Const.TIME[self.level]
            self.timediamond = 0
            self.scorediamond = 0

            self.key_down = False
            self.key_up = False
            self.key_left = False
            self.key_right = False
            self.buttons["time"].change_text_color(Const.COLOR_BLACK)

            self.time_add = 0
        else:
            self.level = self.LEVELBEGIN

    def changetime(self):
        text = "Time:"

        real_timeleft = self.time_left + self.time_add

        if real_timeleft < 10:
            text += "00"
        elif real_timeleft < 100:
            text += "0"
        
        text += str(int(real_timeleft))
        text += "s"

        self.buttons["time"].update_text(text)
        if real_timeleft < 10 and self.timediamond == 0:
            if int(real_timeleft) % 2 == 0:
                self.buttons["time"].change_text_color(Const.COLOR_RED)
            else:
                self.buttons["time"].change_text_color(Const.COLOR_WHITE)
    
    def changediamond(self):
        text = "X"
        if self.scorediamond < 10:
            text += "00"
        elif self.scorediamond < 100:
            text += "0"

        text += str(self.scorediamond)
        self.buttons["num_scorediamond"].update_text(text)

        if self.time_left + self.time_add <= 5 and self.timediamond > 0:
            self.time_add += 5
            self.timediamond -= 1

        text = "X"
        if self.timediamond < 10:
            text += "00"
        elif self.timediamond < 100:
            text += "0"

        text += str(self.timediamond)
        self.buttons["num_timediamond"].update_text(text)

    def changescore(self):
        text =r"Score:"
        score = 100 * self.scorediamond + 50 * self.timediamond

        if self.player_kind == self.PLAYER3:
            score += (100 * self.scorediamond + 50 * self.timediamond) // 2 * (self.level - 1) # 第三种精灵的宝石得分会随着关卡的增加而增加


        if score < 10:
            text += "0000"
        elif score < 100:
            text += "000"
        elif score < 1000:
            text += "00"
        elif score < 10000:
            text += "0"

        text += str(score)

        self.buttons["score"].update_text(text)

    def place_diamond(self):
        rate = Const.PLAYER_RATE[self.player_kind - 1]
        for i in range(Const.MAZE_HEIGHT_SQUARE):
            for j in range(Const.MAZE_WIDTH_SQUARE):
                if self.maze[i][j] != Const.MAZE_WALL and self.maze[i][j] != Const.MAZE_FLAG:
                    r = rate * self.distribution[i][j]
                    rate1 = randint(1, 100) / 100
                    if r >= rate1:
                        rate2 = randint(1,5)
                        if rate2 <= 2:
                            self.maze[i][j] = Const.MAZE_TIMEDIAMOND
                        else:
                            self.maze[i][j] = Const.MAZE_SCOREDIAMOND
    
    def interruptgame(self):
        self.key_right = False
        self.key_left = False
        self.key_up = False
        self.key_down = False

    def replay(self):
        self.timediamond = 0
        self.scorediamond = 0
        self.time_add = 0
        self.maze = deepcopy(self.maze_copy)
        self.player.initpos()
        self.timer.reset()
        self.timer.start()
        self.score = 0

    def calculatescore(self):
        self.score = self.time_left * 5 + self.timediamond * 50 + self.scorediamond * 100
        if self.player_kind == self.PLAYER3:
            self.score += (self.timediamond * 50 + self.scorediamond * 100) * ((self.level + 3) % 4) // 2 # f(x) = (x+2)%4 ->f(0)=2,f(3)=1,f(2)=0
            self.score = int(self.score)

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
        self.buttons["introduction3"] = Button(self.screen, "     遇到宝石概率低         遇到宝石概率适中    遇到宝石概率及价值逐渐提升", posy = 350, posx = 110, width = 580, height = 50, button_color = Const.COLOR_LIGHTGRAY, text_color = Const.COLOR_BLUE, fontsize = 20)
        self.buttons["introduction4"] = Button(self.screen, "使用方向键控制角色在迷宫中移动", posy = 410, posx = 110, width = 580, height = 30, button_color = Const.COLOR_DARKGRAY, text_color = Const.COLOR_BLACK, fontsize = 20)
        self.buttons["introduction5"] = Button(self.screen, "在规定时间内尽快走到终点，并挖取尽可能多的宝石来提高分数!", posy = 440, posx = 110, width = 580, height = 30, button_color = Const.COLOR_DARKGRAY, text_color = Const.COLOR_BLACK, fontsize = 20)
        self.buttons["introduction6"] = Button(self.screen, "红色的宝石可以获得额外分数，绿色的宝石可以延长时间!", posy = 470, posx = 110, width = 580, height = 30, button_color = Const.COLOR_DARKGRAY, text_color = Const.COLOR_BLACK, fontsize = 20)
        self.buttons["introduction7"] = Button(self.screen, "在游戏过程中按<M>查看本关的矿石分布概率", posy = 500, posx = 110, width = 580, height = 30, button_color = Const.COLOR_DARKGRAY, text_color = Const.COLOR_BLACK, fontsize = 20)


        # 重开界面
        self.buttons["gameover"] = Button(self.screen, "Game Over!", height = 60, text_color = Const.COLOR_RED, fontsize = 48, button_color = Const.COLOR_LIGHTGRAY, posy = 220)
        self.buttons["retry"] = Button(self.screen, "重玩本关", height = 50, text_color = Const.COLOR_BLACK, button_color = Const.COLOR_LIGHTGRAY, posy = 400, posx = 150, fontsize = 36, selected_color = Const.COLOR_BLUE)
        self.buttons["returnmain"] = Button(self.screen, "返回主界面", height = 50, text_color = Const.COLOR_BLACK, button_color = Const.COLOR_LIGHTGRAY, posy = 400, posx = 450, fontsize = 36, selected_color = Const.COLOR_BLUE)

        # 游戏界面
        self.buttons["score"] = Button(self.screen, "Score:00000", text_color = Const.COLOR_BLACK, button_color = Const.COLOR_LIGHTGRAY, fontsize = 32,posx = 0, posy = 0)
        self.buttons["time"] = Button(self.screen, "Time:000s", text_color =Const.COLOR_BLACK, button_color = Const.COLOR_LIGHTGRAY, width = 200, fontsize = 32, posy = 0, posx = Const.SCREEN_WIDTH - 200)
        self.buttons["num_scorediamond"] = Button(self.screen, "X000", text_color = Const.COLOR_BLACK, button_color = Const.COLOR_LIGHTGRAY,width = 60, fontsize = 32, posx = 60, posy = Const.SCREEN_HEIGHT - 76)
        self.buttons["num_timediamond"] = Button(self.screen, "X000", text_color = Const.COLOR_BLACK, button_color = Const.COLOR_LIGHTGRAY, width = 60, fontsize = 32, posx = 230, posy = Const.SCREEN_HEIGHT - 76)
        self.buttons["gamepause"] = Button(self.screen, "暂 停", posx = Const.SCREEN_WIDTH - 100, posy = Const.SCREEN_HEIGHT - 40, width = 100, height = 40, button_color = Const.COLOR_DARKGRAY, text_color = Const.COLOR_BLUE, selected_color = Const.COLOR_RED, fontsize = 36)
        self.buttons["progressbar"] = Button(self.screen, "挖宝进度", posx = Const.SCREEN_WIDTH - 450, posy = Const.SCREEN_HEIGHT - 80, width = 100, fontsize = 32, button_color = Const.COLOR_LIGHTGRAY, text_color = Const.COLOR_BLACK)

        self.buttons["introduction8"] = Button(self.screen, "颜色越深的地方藏有宝石的概率越高", posy = 570, posx = 110, width = 580, height = 30, button_color = Const.COLOR_DARKGRAY, text_color = Const.COLOR_BLACK, fontsize = 20)
        self.buttons["introduction9"] = Button(self.screen, "再次按下<M>以返回游戏界面", posy = 600, posx = 110, width = 580, height = 30, button_color = Const.COLOR_DARKGRAY, text_color = Const.COLOR_BLACK, fontsize = 20)


        # 暂停界面,借用上面的重开和返回主界面
        self.buttons["pause"] = Button(self.screen, "暂 停", height = 60, text_color = Const.COLOR_BLACK, fontsize = 48, button_color = Const.COLOR_LIGHTGRAY, posy = 150)
        self.buttons["continue"] = Button(self.screen, "返回关卡", height = 60, text_color = Const.COLOR_BLACK, button_color = Const.COLOR_LIGHTGRAY, posy = 520, fonsize = 36, selected_color = Const.COLOR_BLUE)

        # 结算界面
        self.buttons["pass"] = Button(self.screen, "过   关", height = 60, text_color = Const.COLOR_RED, fontsize = 48, button_color = Const.COLOR_LIGHTGRAY, posy = 120)
        self.buttons["next"] = Button(self.screen, "下一关", height = 60, text_color = Const.COLOR_BLACK, button_color = Const.COLOR_LIGHTGRAY, posy = 520, WIDTH = 200, selected_color = Const.COLOR_BLUE, fontsize = 36)
        self.buttons["resultscore"] = Button(self.screen, "得 分=",height = 60, posy = 220, text_color = Const.COLOR_BLUE, button_color = Const.COLOR_LIGHTGRAY, fontsize = 40, width = 300)
        self.buttons["calculatescore"] = Button(self.screen, "剩余时间加分 + 时间宝石加分 + 得分宝石加分=",height = 60, posy = 320, text_color = Const.COLOR_BLUE, button_color = Const.COLOR_LIGHTGRAY, fontsize = 32, width = 300)
        self.buttons["getscore"] = Button(self.screen, "10000",height = 60, posy = 420, text_color = Const.COLOR_RED, button_color = Const.COLOR_LIGHTGRAY, fontsize = 40, width = 300)

    def add_images(self):
        self.images["icon1"] = Image(Const.IMAGE_PLAYER1_ICON_PATH)
        self.images["icon2"] = Image(Const.IMAGE_PLAYER2_ICON_PATH)
        self.images["icon3"] = Image(Const.IMAGE_PLAYER3_ICON_PATH)
        self.images["scorediamond"] = Image(Const.IMAGE_SCOREDIAMOND_PATH)
        self.images["timediamond"] = Image(Const.IMAGE_TIMEDIAMOND_PATH)
        self.images["road"] = Image(Const.IMAGE_ROAD_PATH)
        self.images["wall"] = Image(Const.IMAGE_WALL_PATH)
        self.images["flag"] = Image(Const.IMAGE_FLAG_PATH)
        self.images["road_scorediamond"] = Image(Const.IMAGE_ROAD_SCOREDIAMOND_PATH)
        self.images["road_timediamond"] = Image(Const.IMAGE_ROAD_TIMEDIAMOND_PATH)
