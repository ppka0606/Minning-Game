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
        maze_region_max_size = Const.MAZE_REGION_SIZE_DICT[self.level]
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
        # 接下来制造地图中的空白地形

        rect_list = [(1000, 1000)] # 给定一个填充值，方便循环进行
        area = Const.MAZE_REGION_SIZE_DICT[self.level]
        num = Const.MAZE_REGION_NUMBER_DICT[self.level]
        wall_width = (Const.MAZE_WIDTH_SQUARE - 1) // 2
        wall_height = (Const.MAZE_HEIGHT_SQUARE - 1) // 2

        while len(rect_list) <= num:
            posx = randint(1, wall_height - 1)
            posy = randint(1, wall_width - 1)
            posx *= 2
            posy *= 2

            can_blank = True
            for rect in rect_list:
                if abs(posx - rect[0]) <= area and abs(posy - rect[1]) <= area:
                    can_blank = False
                    break
            
            if can_blank:
                rect_list.append((posx, posy))
                down_edge = min(posx + area, Const.MAZE_HEIGHT_SQUARE - 2)
                right_edge = min(posy + area, Const.MAZE_WIDTH_SQUARE - 2)
                for i in range(posx, down_edge):
                    for j in range(posy, right_edge):
                        self._map[i][j] = Const.MAZE_ROAD

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
    maze = Maze(3)
