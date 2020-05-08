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

        self.map = [[0] * Const.maze_width_square for _ in range(Const.maze_height_square)]
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

        for i in range(1, height, 2):
            for j in range(1, width, 2):
                self.map[i][j] = 1

        counter = 0 
        region = []
            # 装入一个4元组,记录左上和右下的坐标,确保不会生成重复的空白
        while counter < maze_region_number:
            # 先选起始坐标
            x = randint(0, (height - 3) / 2)
            y = randint(0, (width - 3) / 2)
            x = x * 2 + 1
            y = y * 2 + 1
                # 确保从奇数格("1"格)开始
            size_x = randint(1, (maze_region_max_size - 1) / 2)
            size_y = randint(1, (maze_region_max_size - 1) / 2)
            size_x = size_x * 2 + 1 
            size_y = size_y * 2 + 1

            for rect in region:
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
                    if i >= height - 2:
                        break
                    for j in range(y, y+size_y):
                        if j >= width - 2:
                            break
                        self.map[i][j] = 1

                region.append((x, y, x + size_x, y + size_y))
                counter += 1
        # pass

# test
if __name__ == '__main__':
    maze = Maze(3)
    for i in range(len(maze.map)):
        for j in range(len(maze.map[0])):
            print("▆" if maze.map[i][j] == 0 else " ",end = "")
        print()


