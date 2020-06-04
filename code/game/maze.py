import os
from random import randint

from const import Const


class Maze():
    """
    生成迷宫(仅限(0,1)数组)并返回对象
    迷宫的图形界面绘制将在其他类中完成
    """
    def __init__(self, level):
        """
        生成指定等级的迷宫
        """
        self.level = level

        self._map = [[0] * Const.maze_width_square for _ in range(Const.maze_height_square)]
        self.create_map()
    
    def create_map(self):
        """
        按一定算法生成一个迷宫并存储在map中
        """
        # 随机生成迷宫
        # 考虑到这个是挖矿游戏,好像宽度1的迷宫不是很合适
        # 参考了 https://zhuanlan.zhihu.com/p/27381213 的算法3并做了一定修改,更像# 是一个矿井
        
        maze_region_max_size = Const.maze_region_max_size_dict[self.level]
        maze_region_number = Const.maze_region_number_dict[self.level]
        
        height = Const.maze_height_square
        width = Const.maze_width_square
        
        # 制造间隔
        for i in range(1, height, 2):
            for j in range(1, width, 2):
                self._map[i][j] = 1
        # self.print_map()

        # 生成一条通路,全部是左下角开始到右上角(向下一格)结束
        self._map[height - 2][0] = 1
        self._map[1][width - 1] = 1
            # 挖到右上角通了为止
        temp_x = height - 2
        temp_y = 1

        stack = []
        stack.append((temp_x, temp_y))
            # 为防止挖到死角,需要一个栈来回退
        while self._map[1][width - 3] != 1 and self._map[2][width - 2] != 1:
        # while (1, width - 3) not in stack and (2, width - 2) not in stack:
            # 循环的结束条件是挖到出口的通路为止
            can_dig = [True] * 4
            if temp_x - 2 < 0 or self._map[temp_x - 1][temp_y] != 0:
                can_dig[0] = False
            if temp_x + 2 > height - 2 or self._map[temp_x + 1][temp_y] != 0:
                can_dig[1] = False
            if temp_y - 2 < 0 or self._map[temp_x][temp_y - 1] != 0:
                can_dig[2] = False
            if temp_y + 2 > width - 2 or self._map[temp_x][temp_y + 1] != 0:
                can_dig[3] = False

            if not (can_dig[0] or can_dig[1] or can_dig[2] or can_dig[3]):
                # 如果上下左右都挖不了(出地图或者邻近一个已经挖过了)
                # self.print_map()
                stack.pop()
                temp_x = stack[len(stack) - 1][0]
                temp_y = stack[len(stack) - 1][1]
                continue
            
            direction = randint(1, 6)
            # 为了尽量往出口接近,提高向上和向右的概率
            if direction == 5:
                direction = 1
            elif direction == 6:
                direction = 3
            if can_dig[direction - 1]:
                if direction == 1:
                    self._map[temp_x - 1][temp_y] = 1
                    temp_x -= 2
                elif direction == 2:
                    self._map[temp_x + 1][temp_y] = 1
                    temp_x += 2
                elif direction == 3:
                    self._map[temp_x][temp_y - 1] = 1
                    temp_y -= 2
                else:
                    self._map[temp_x][temp_y + 1] = 1
                    temp_y += 2

            stack.append((temp_x, temp_y))


        # 制造空白
        counter = 0 
        regions = []
            # 装入一个4元组,记录左上和右下的坐标,确保不会生成重复的空白

        while counter < maze_region_number:
            # 先选起始坐标
            x = randint(0, (height - 3) // 2)
            y = randint(0, (width - 3) // 2)
            x = x * 2 + 1
            y = y * 2 + 1
                # 确保从奇数格("1"格)开始
            size_x = randint(1, (maze_region_max_size - 1) // 2)
            size_y = randint(1, (maze_region_max_size - 1) // 2)
            size_x = size_x * 2 + 1 
            size_y = size_y * 2 + 1

            for rect in regions:
                if x >= rect[0] and x <= rect[2] and y >= rect[1] and y <= rect[3]:
                    break
                    # 左上角
                if x + size_x >= rect[0] and x + size_x <= rect[2] and y >= rect[1] and y <= rect[3]:
                    break
                    # 左下角
                if x >= rect[0] and x <= rect[2] and y + size_y >= rect[1] and y + size_y <= rect[3]:
                    break
                    # 右上角
                if x + size_x >= rect[0] and x + size_x <= rect[2] and y + size_y >= rect[1] and y + size_y <= rect[3]:
                    break
                    # 右下角
            else:
                for i in range(x, x+size_x):
                    if i > height - 2:
                        break
                    for j in range(y, y+size_y):
                        if j > width - 2:
                            break
                        self._map[i][j] = 1

                regions.append((x, y, x + size_x, y + size_y))
                counter += 1

        # 封堵住单一口的空白
        for i in range(1, Const.maze_height_square - 1):
            for j in range(1, Const.maze_width_square - 1):
                if self._map[i][j] == 1 and self._map[i][j - 1] == 0 and self._map[i][j + 1] == 0 and self._map[i - 1][j] == 0 and self._map[i + 1][j] == 0:
                    self._map[i][j] = 0

        # 调试中使用展示完成效果
        self.print_map()

    def print_map(self):
        os.system("cls")
        print("开始画图")
        for i in range(len(self._map)):
            for j in range(len(self._map[0])):
                print("O" if self._map[i][j] == 0 else " ",end = "")
            print()
        print("完成")

    @property
    def map(self):
        return self._map

# test
if __name__ == '__main__':
    maze = Maze(1)
    # print(maze.map)
