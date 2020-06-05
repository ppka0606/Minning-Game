import pygame
import os

from maze import Maze
from const import Const
import user
import game_functions as gf
import map_functions as mf


if __name__ =="__main__":
    # user.User.get_user_list()
    pygame.init()
    
    screen = pygame.display.set_mode((Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT))
    pygame.display.set_caption("挖矿游戏")

    maze = Maze(3).map

    while True:
        gf.check_events(screen)
        
        screen.fill(Const.COLOR_DEFAULT_BACKGROUND)  # 背景色
        mf.draw_map(screen, maze)

        pygame.display.flip()
