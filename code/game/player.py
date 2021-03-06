import pygame
from maze import Maze
from const import Const
from image import Image

class Player():
    """
    Player
    管理玩家的各种资源
    包括图片，位置，速度等信息
    """

    DIRECTION_UP    = 1
    DIRECTION_DOWN  = 2
    DIRECTION_LEFT  = 3
    DIRECTION_RIGHT = 4

    def __init__(self, player_kind, maze):
        """
        实现init函数的可复用，如失败/通关后退回到主界面
        """
        # player图像的实际高度可能和判定高度不完全相同，主要是为了体现可能的立体效果
        # player的判定高度和宽度(用于判定撞墙)为（30，30），见Cosnt
        # 以左下角的坐标为基准进行计算,绘制时再转换为左上角
        self.player_kind = player_kind
        self.maze = maze
        self.speed = Const.PLAYER_SPEED[self.player_kind - 1]
        self.initpos()

        self.images = []
        self.getimage()

    def initpos(self):
        self.actual_posx = float(Const.MAZE_SQUARE_PIXEL)
        self.actual_posy = float(Const.MAZE_SQUARE_PIXEL + Const.PLAYER_HEIGHT_PIXEL)
        # 起始位置为左上角， 用float存储位置便于计算
        self.takeup = [None , None, None, None] # 标记占据的格子，玩家最多可以同时占据四个格子，需进行判定
        # 四个位置的顺序分别是 0 1
        #                    2 3
        self.check_takeup()
        
        if self.maze != None:
            if self.maze[1][2] != Const.MAZE_WALL:
                self.direction = self.DIRECTION_RIGHT
            else:
                self.direction = self.DIRECTION_DOWN
                    # 避免初始的时候脸对着墙

    def getimage(self):
        for i in range(1, 5):
            path = r"resource\mingingGame\game\player"
            path += str(self.player_kind)
            path += "_"
            path += str(i)
            path += ".bmp"
            self.images.append(Image(path))
    
    def go_up(self):
        self.check_takeup()

        if self.direction != self.DIRECTION_UP:
            self.direction = self.DIRECTION_UP
            return # 单次按键只转向不移动
        limit = 0
        if self.takeup[1] == None:  # 横向占1格
            if self.maze[self.takeup[0][0] - 1][self.takeup[0][1]] != Const.MAZE_WALL:
                limit = Const.MIN_VALUE
            else:
                limit = self.takeup[0][0] * Const.MAZE_SQUARE_PIXEL + Const.PLAYER_HEIGHT_PIXEL
        else:
            if self.maze[self.takeup[0][0] - 1][self.takeup[0][1]] != Const.MAZE_WALL and self.maze[self.takeup[1][0] - 1][self.takeup[1][1]] != Const.MAZE_WALL :
                limit = Const.MIN_VALUE
            else:
                limit = self.takeup[0][0] * Const.MAZE_SQUARE_PIXEL + Const.PLAYER_HEIGHT_PIXEL
        self.actual_posy = max(limit, self.actual_posy - self.speed)

    def go_down(self):
        self.check_takeup()

        if self.direction != self.DIRECTION_DOWN:
            self.direction = self.DIRECTION_DOWN
            return 

        limit = 0
        if self.takeup[1] == None:
            if self.takeup[2] == None:
                if self.maze[self.takeup[0][0] + 1][self.takeup[0][1]] != Const.MAZE_WALL:
                    limit = Const.MAX_VALUE
                else:
                    limit = (self.takeup[0][0] + 1) * Const.MAZE_SQUARE_PIXEL
            else:
                if self.maze[self.takeup[0][0] + 2][self.takeup[0][1]] != Const.MAZE_WALL:
                    limit = Const.MAX_VALUE
                else:
                    limit = (self.takeup[0][0] + 2) * Const.MAZE_SQUARE_PIXEL
        else:
            if self.takeup[2] == None:
                if self.maze[self.takeup[0][0] + 1][self.takeup[0][1]] != Const.MAZE_WALL and self.maze[self.takeup[1][0] + 1][self.takeup[1][1]] != Const.MAZE_WALL:
                    limit = Const.MAX_VALUE
                else:
                    limit = (self.takeup[0][0] + 1) * Const.MAZE_SQUARE_PIXEL
            else:
                if self.maze[self.takeup[0][0] + 2][self.takeup[0][1]] != Const.MAZE_WALL and self.maze[self.takeup[1][0] + 2][self.takeup[1][1]] != Const.MAZE_WALL:
                    limit = Const.MAX_VALUE
                else:
                    limit = (self.takeup[0][0] + 2) * Const.MAZE_SQUARE_PIXEL

        self.actual_posy = min(limit, self.actual_posy + self.speed)

    def go_left(self):
        self.check_takeup()

        if self.direction != self.DIRECTION_LEFT:
            self.direction = self.DIRECTION_LEFT
            return

        limit = 0
        if self.takeup[2] == None:  # 纵向占1格
            if self.maze[self.takeup[0][0]][self.takeup[0][1] - 1] != Const.MAZE_WALL:
                limit = Const.MIN_VALUE
            else:
                limit = self.takeup[0][1] * Const.MAZE_SQUARE_PIXEL
        else:
            if self.maze[self.takeup[0][0]][self.takeup[0][1] - 1] != Const.MAZE_WALL and self.maze[self.takeup[2][0]][self.takeup[2][1] - 1] != Const.MAZE_WALL :
                limit = Const.MIN_VALUE
            else:
                limit = self.takeup[0][1] * Const.MAZE_SQUARE_PIXEL
        self.actual_posx = max(limit, self.actual_posx - self.speed)

    def go_right(self):
        self.check_takeup()

        if self.direction != self.DIRECTION_RIGHT:
            self.direction = self.DIRECTION_RIGHT
            return

        limit = 0
        if self.takeup[2] == None:
            if self.takeup[1] == None: 
                if self.maze[self.takeup[0][0]][self.takeup[0][1] + 1] != Const.MAZE_WALL:
                    limit = Const.MAX_VALUE
                else:
                    limit = (self.takeup[0][1] + 1) * Const.MAZE_SQUARE_PIXEL - Const.PLAYER_WIDTH_PIXEL
            else:
                if self.maze[self.takeup[0][0]][self.takeup[0][1] + 2] != Const.MAZE_WALL:
                    limit = Const.MAX_VALUE
                else:
                    limit = (self.takeup[0][1] + 2) * Const.MAZE_SQUARE_PIXEL - Const.PLAYER_WIDTH_PIXEL
        else:
            if self.takeup[1] == None:
                if self.maze[self.takeup[0][0]][self.takeup[0][1] + 1] != Const.MAZE_WALL and self.maze[self.takeup[2][0]][self.takeup[2][1] + 1] != Const.MAZE_WALL:
                    limit = Const.MAX_VALUE
                else:
                    limit = (self.takeup[0][1] + 1) * Const.MAZE_SQUARE_PIXEL - Const.PLAYER_WIDTH_PIXEL
            else:
                if self.maze[self.takeup[0][0]][self.takeup[0][1] + 2] != Const.MAZE_WALL and self.maze[self.takeup[2][0]][self.takeup[2][1] + 2] != Const.MAZE_WALL:
                    limit = Const.MAX_VALUE
                else:
                    limit = (self.takeup[0][1] + 2) * Const.MAZE_SQUARE_PIXEL - Const.PLAYER_WIDTH_PIXEL
        
        self.actual_posx = min(limit, self.actual_posx + self.speed)

    def check_takeup(self):
        col1 = int(self.actual_posx / Const.MAZE_SQUARE_PIXEL)
        col2 = int((self.actual_posx + Const.PLAYER_WIDTH_PIXEL - 0.01)/ Const.MAZE_SQUARE_PIXEL) # 给定0.1的误差防止压线的情况影响判断

        row1 = int((self.actual_posy - Const.PLAYER_HEIGHT_PIXEL) / Const.MAZE_SQUARE_PIXEL)
        row2 = int((self.actual_posy - 0.01) / Const.MAZE_SQUARE_PIXEL)

        self.takeup[0] = (row1, col1)
        self.takeup[1] = (row1, col2)
        self.takeup[2] = (row2, col1)
        self.takeup[3] = (row2, col2)
        
        if col1 == col2:
            self.takeup[1] = None
            self.takeup[3] = None
        
        if row1 == row2:
            self.takeup[2] = None
            self.takeup[3] = None

    def getmaze(self, maze):
        self.maze = maze

if __name__ == "__main__":
    maze = Maze(3).map
    player = Player(1, maze)
    while True:
        print(player.actual_posx, player.actual_posy)
        s = input()
        if s == 'w':
            player.go_up()
        elif s == 's':
            player.go_down()
        elif s == 'a':
            player.go_left()
        else:
            player.go_right()