import pygame
import os

from image import ImageWall, ImageSoil

from const import Const

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
    draw_map(screen, status.maze)


def draw_login(screen):


def draw_map(screen, maze):
    """
    根据传入的level绘制map
    """
    image_wall = ImageWall()
    image_soil = ImageSoil()

    for i in range(Const.MAZE_HEIGHT_SQUARE):
        for j in range(Const.MAZE_WIDTH_SQUARE):
            if maze[i][j] == 0:
                image_wall.blit_image(screen, j * Const.MAZE_SQUARE_PIXEL + Const.GAME_INTERFACE_MAINAREA_POSX, i * Const.MAZE_SQUARE_PIXEL + Const.GAME_INTERFACE_MAINAREA_POSY)
            else:
                image_soil.blit_image(screen, j * Const.MAZE_SQUARE_PIXEL + Const.GAME_INTERFACE_MAINAREA_POSX, i * Const.MAZE_SQUARE_PIXEL + Const.GAME_INTERFACE_MAINAREA_POSY)
