import pygame

from maze import Maze
from image import ImageWall
from const import Const

def draw_map(screen, maze):
    """
    根据传入的level绘制map
    """
    image_wall = ImageWall()

    for i in range(Const.MAZE_HEIGHT_SQUARE):
        for j in range(Const.MAZE_WIDTH_SQUARE):
            if maze[i][j] == 0:
                image_wall.blit_image(screen, j * Const.MAZE_SQUARE_PIXEL + Const.GAME_INTERFACE_MAINAREA_POSX, i * Const.MAZE_SQUARE_PIXEL + Const.GAME_INTERFACE_MAINAREA_POSY)


