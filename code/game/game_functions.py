import pygame
import os

from image import Image
from const import Const
from button import Button
from status import Status

def check_exit(screen, status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status.close = True
        if event.type == pygame.MOUSEMOTION:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            status.buttons["confirm_exit"].selected(mouse_x, mouse_y)
            status.buttons["cancel_exit"].selected(mouse_x, mouse_y)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if status.buttons["cancel_exit"].selected(mouse_x, mouse_y):
                status.close = False
            if status.buttons["confirm_exit"].selected(mouse_x, mouse_y):
                os._exit(0)

def check_login(screen, status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status.close = True
        if event.type == pygame.MOUSEMOTION:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            status.buttons["start"].selected(mouse_x, mouse_y)
            status.buttons["help"].selected(mouse_x, mouse_y)
            status.buttons["player1"].selected(mouse_x, mouse_y)
            status.buttons["player2"].selected(mouse_x, mouse_y)
            status.buttons["player3"].selected(mouse_x, mouse_y)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if status.buttons["player1"].selected(mouse_x, mouse_y):
                status.buttons["confirm_player"].update_text("已选择 饭团")

                status.buttons["player1"].lock()
                status.buttons["player2"].unlock()
                status.buttons["player3"].unlock()

                status.player_kind = Status.PLAYER1

            if status.buttons["player2"].selected(mouse_x, mouse_y):
                status.buttons["confirm_player"].update_text("已选择 蛋黄")

                status.buttons["player1"].unlock()
                status.buttons["player2"].lock()
                status.buttons["player3"].unlock()

                status.player_kind = Status.PLAYER2
            if status.buttons["player3"].selected(mouse_x, mouse_y):
                status.buttons["confirm_player"].update_text("已选择 栗子")

                status.buttons["player1"].unlock()
                status.buttons["player2"].unlock()
                status.buttons["player3"].lock()

                status.player_kind = Status.PLAYER3
            if status.buttons["help"].selected(mouse_x, mouse_y):
                status.interface = Status.INTERFACE_HELP

            if status.buttons["start"].selected(mouse_x, mouse_y)and status.player_kind != Status.PLAYERBEGIN:
                status.interface = Status.INTERFACE_GAME
                status.levelup()
                return

def check_help(screen, status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status.close = True
        if event.type == pygame.MOUSEMOTION:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            status.buttons["return"].selected(mouse_x, mouse_y)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if status.buttons["return"].selected(mouse_x, mouse_y):
                status.interface = Status.INTERFACE_LOGIN
                return

def check_restart(screen, status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status.close = True
        if event.type == pygame.MOUSEMOTION:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            status.buttons["retry"].selected(mouse_x, mouse_y)
            status.buttons["returnmain"].selected(mouse_x, mouse_y)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if status.buttons["returnmain"].selected(mouse_x, mouse_y):
                status.interface = Status.INTERFACE_LOGIN
                return
            
def check_game(screen, status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status.close = True

def check_events(screen, status):
    """
    事件监听
    """
    if status.close:
        check_exit(screen, status)
        return
    if status.interface == Status.INTERFACE_LOGIN:
        check_login(screen, status)
    if status.interface == Status.INTERFACE_HELP:
        check_help(screen, status)
    if status.interface == Status.INTERFACE_RESTART:
        check_restart(screen, status)
    if status.interface == Status.INTERFACE_GAME:
        check_game(screen, status)

def draw_exit(screen, status):
    screen.fill(Const.COLOR_DARKGRAY)
    status.buttons["ask_exit"].blit_button()
    status.buttons["confirm_exit"].blit_button()
    status.buttons["cancel_exit"].blit_button()

def draw_login(screen, status):
    screen.fill(Const.COLOR_LIGHTGRAY)
    status.buttons["start"].blit_button()
    status.buttons["help"].blit_button()
    status.buttons["player1"].blit_button()
    status.buttons["player2"].blit_button()
    status.buttons["player3"].blit_button()
    status.buttons["confirm_player"].blit_button()

    status.images["icon1"].blit_image(status.screen, 130, 130)
    status.images["icon2"].blit_image(status.screen, 360, 130)
    status.images["icon3"].blit_image(status.screen, 590, 130)

def draw_help(screen, status):
    screen.fill(Const.COLOR_LIGHTGRAY)
    status.buttons["return"].blit_button()
    status.buttons["help_title"].blit_button()

    status.images["icon1"].blit_image(status.screen, 130, 130)
    status.images["icon2"].blit_image(status.screen, 360, 130)
    status.images["icon3"].blit_image(status.screen, 590, 130)

    status.buttons["introduction1"].blit_button()
    status.buttons["introduction2"].blit_button()
    status.buttons["introduction3"].blit_button()
    status.buttons["introduction4"].blit_button()
    status.buttons["introduction5"].blit_button()
    status.buttons["introduction6"].blit_button()

def draw_restart(screen, status):
    screen.fill(Const.COLOR_LIGHTGRAY)
    status.buttons["gameover"].blit_button()
    status.buttons["retry"].blit_button()
    status.buttons["returnmain"].blit_button()

def draw_game(screen, status):
    screen.fill(Const.COLOR_LIGHTGRAY)
    status.buttons["time"].blit_button()
    status.buttons["score"].blit_button()
    status.images["scorediamond"].blit_image(status.screen, 0, Const.SCREEN_HEIGHT - 83)
    status.images["timediamond"].blit_image(status.screen, 170, Const.SCREEN_HEIGHT - 80)
    status.buttons["num_scorediamond"].blit_button()
    status.buttons["num_timediamond"].blit_button()

    # 绘制迷宫
    # 尽量使人物处于中间位置，因此就需要计算需要呈现于图中的区域
    if status.player.actual_posx <= Const.MAZE_SQUARE_PIXEL * Const.MAZE_DISPLAY_WIDTH_SQUARE / 2 and status.player.actual_posy <= Const.MAZE_SQUARE_PIXEL * Const.MAZE_DISPLAY_HEIGHT_SQUARE / 2: # 在左上角区域
        for i in range(Const.MAZE_DISPLAY_HEIGHT_SQUARE):
            for j in range(Const.MAZE_DISPLAY_WIDTH_SQUARE):
                posx = Const.GAME_INTERFACE_MAINAREA_POSX + j * Const.MAZE_SQUARE_PIXEL
                posy = Const.GAME_INTERFACE_MAINAREA_POSY + i * Const.MAZE_SQUARE_PIXEL
                if status.maze[i][j] == Const.MAZE_WALL:
                    status.images["wall"].blit_image(status.screen, posx, posy)
                else:
                    status.images["road"].blit_image(status.screen, posx, posy)
        
        sprite_image = status.player.images[status.player.direction - 1]
        sprite_posx = int(status.player.actual_posx) + Const.GAME_INTERFACE_MAINAREA_POSX
        sprite_posy = int(status.player.actual_posy) + Const.GAME_INTERFACE_MAINAREA_POSY - sprite_image.height
        sprite_image.blit_image(status.screen, sprite_posx, sprite_posy) # 此时没有相对移位，所以就把精灵放在绝对位置就好

def draw(screen, status):
    if status.close:
        draw_exit(screen, status)
        return
    if status.interface == Status.INTERFACE_LOGIN:
        draw_login(screen, status)
    if status.interface == Status.INTERFACE_HELP:
        draw_help(screen, status)
    if status.interface == Status.INTERFACE_RESTART:
        draw_restart(screen, status)
    if status.interface == Status.INTERFACE_GAME:
        draw_game(screen, status)


