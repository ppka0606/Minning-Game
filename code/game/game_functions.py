import pygame
import os

from image import ImageWall, ImageSoil
from const import Const
from button import Button

def check_events(screen, status):
    """
    事件监听
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os._exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                os._exit(0)

def update_screen(screen, status):
    draw_map(screen, status.maze, (16, 8))
    for button in status.buttons.values():
        button.blit_button()


def draw_login(screen):
    pass

def draw_map(screen, maze, focus):
    """
    根据传入的level绘制map

    focus表示游戏主界面的中心焦点，因为再界面上显示的游戏不是直接将整个地图绘制出来
    """
    image_wall = ImageWall()
    image_soil = ImageSoil()

    beginx = focus[0] - (Const.MAZE_DISPLAY_WIDTH_SQUARE - 1) // 2
    endx = focus[0] + (Const.MAZE_DISPLAY_WIDTH_SQUARE + 1) // 2
    beginy = focus[1] - (Const.MAZE_DISPLAY_HEIGHT_SQUARE) // 2
    endy = focus[1] + (Const.MAZE_DISPLAY_HEIGHT_SQUARE + 1) // 2
    
    posy = 0
    posx = 0
    for i in range(beginy, endy):
        posx = 0
        for j in range(beginx, endx):
            if maze[i][j] == Const.MAZE_WALL:
                image_wall.blit_image(screen, posx * Const.MAZE_SQUARE_PIXEL + Const.GAME_INTERFACE_MAINAREA_POSX, posy * Const.MAZE_SQUARE_PIXEL + Const.GAME_INTERFACE_MAINAREA_POSY)
            else:
                image_soil.blit_image(screen, posx * Const.MAZE_SQUARE_PIXEL + Const.GAME_INTERFACE_MAINAREA_POSX, posy * Const.MAZE_SQUARE_PIXEL + Const.GAME_INTERFACE_MAINAREA_POSY)
            posx += 1
        posy += 1
    
