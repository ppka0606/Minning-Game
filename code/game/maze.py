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

        self._map = [[Const.MAZE_WALL] * Const.MAZE_WIDTH_SQUARE for _ in range(Const.MAZE_HEIGHT_SQUARE)]
        self.create_map()
    
    def create_map(self):
        """
        按一定算法生成一个迷宫并存储在map中
        """
        # 随机生成迷宫
        # 考虑到这个是挖矿游戏,好像宽度1的迷宫不是很合适
        # 参考了 https://zhuanlan.zhihu.com/p/27381213 的算法3并做了一定修改,更像# 是一个矿井
        
        maze_region_max_size = Const.MAZE_REGION_MAX_SIZE_DICT[self.level]
        maze_region_number = Const.MAZE_REGION_NUMBER_DICT[self.level]
        
        height = Const.MAZE_HEIGHT_SQUARE
        width = Const.MAZE_WIDTH_SQUARE
        
        # 制造间隔
        for i in range(1, height, 2):
            for j in range(1, width, 2):
                self._map[i][j] = Const.MAZE_ROAD

        visited_width = (Const.MAZE_WIDTH_SQUARE - 1) // 2
        visited_height = (Const.MAZE_HEIGHT_SQUARE - 1) // 2
        visited = [[False] * visited_width for _ in range(visited_height)]

        direction_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visit_stack = [(0,0)]
        x,y = (0,0)
        visited[x][y] = True
        breaking_walls = visited_width * visited_height - 1
        def can_dig(posx, posy):
            if  posx < 0 or posy < 0 or posx >= visited_height or posy >= visited_width or visited[posx][posy]:
                return False
            else:
                return True
        
        while breaking_walls != 0:
            can = [True] * 4
            for index in range(4):
                temp_x = x + direction_list[index][0]
                temp_y = y + direction_list[index][1]
                can[index] = can_dig(temp_x, temp_y)

            if not(can[0] or can[1] or can[2] or can[3]):
                visit_stack.pop()
                x,y = visit_stack[-1]
            else:
                direction = randint(0, 3)
                while not can[direction]:
                    direction = randint(0, 3)

                dx,dy = direction_list[direction]

                self._map[x * 2 + 1 + dx][y * 2 + 1 + dy] = Const.MAZE_ROAD
                breaking_walls -= 1

                x += dx
                y += dy
                visited[x][y] = True
                visit_stack.append((x,y))
                
            # self.print_map()

        # # 调试中使用展示完成效果
        # self.print_map()

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

# # test
if __name__ == '__main__':
    maze = Maze(1)
