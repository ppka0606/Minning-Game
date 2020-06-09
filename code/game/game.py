import pygame
import os

from maze import Maze
from const import Const
from status import Status
from timer import Timer

import game_functions as gf

if __name__ =="__main__":
    # user.User.get_user_list()
    pygame.init()
    
    screen = pygame.display.set_mode((Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT))
    pygame.display.set_caption("寻宝精灵")
    status = Status(screen)
    fclock = pygame.time.Clock()

    while True:

        gf.check_events(screen, status)
        gf.draw(screen, status)

        pygame.display.flip()
        fclock.tick(Const.CLOCK_FPS)
