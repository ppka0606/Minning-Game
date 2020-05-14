import pygame
import os

from maze import Maze
from const import Const
import user
import game_functions as gf


if __name__ =="__main__":
    # user.User.get_user_list()
    pygame.init()
    
    screen = pygame.display.set_mode((Const.screen_width, Const.screen_height))
    pygame.display.set_caption("Minging Game")

    while True:
        gf.check_events(screen)
        
        screen.fill(Const.color_default_background)  # 背景色
        pygame.display.flip()
