import pygame
import os

from maze import Maze
from const import Const
from status import Status

import game_functions as gf

if __name__ =="__main__":
    # user.User.get_user_list()
    pygame.init()
    
    screen = pygame.display.set_mode((Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT))
    pygame.display.set_caption("挖矿游戏")
    status = Status(screen)
    status.maze = Maze(3).map
    fclock = pygame.time.Clock()

    while True:
        screen.fill(Const.COLOR_GREEN) # 背景色

        gf.check_events(screen, status)
        gf.update_screen(screen, status)

        pygame.display.flip()
        fclock.tick(Const.CLOCK_FPS)