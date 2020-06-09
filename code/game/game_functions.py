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
                status.timer.start()
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
                status.timer.reset()
                status.timer.start()
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
                status.level = Status.LEVELBEGIN
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
                status.level = Status.LEVELBEGIN
                return
            if status.buttons["retry"].selected(mouse_x, mouse_y):
                status.interface = Status.INTERFACE_GAME
                status.replay()
            
def check_game(screen, status):
    status.time_left = status.time - status.timer.getactivetime() / 1000

    if status.time_left + status.time_add < 0:
        status.interface = Status.INTERFACE_RESTART
        status.interruptgame()

    if status.progress_pause:
        progress_time = pygame.time.get_ticks() - status.progresstimer.lastbegin
        if progress_time > Const.PROGRESSBAR_SPEED[status.player_kind - 1]:
            status.progress_pause = False
            status.fillwidth = 0
            status.progresstimer.pause()
            return
        else:
            status.fillwidth = progress_time / Const.PROGRESSBAR_SPEED[status.player_kind - 1] * Const.PROGRESSBAR_WIDTH


    if not status.progress_pause:
        pos = status.player.takeup[0]
        if pos == (Const.MAZE_HEIGHT_SQUARE - 2, Const.MAZE_WIDTH_SQUARE - 2):
            status.calculatescore()
            status.levelup()
            status.interface = Status.INTERFACE_RESULT
            return
        elif status.maze[pos[0]][pos[1]] == Const.MAZE_TIMEDIAMOND:
            status.timediamond += 1
            status.maze[pos[0]][pos[1]] = Const.MAZE_ROAD
            status.progress_pause = True
            status.progresstimer.start()

        elif status.maze[pos[0]][pos[1]] == Const.MAZE_SCOREDIAMOND:
            status.scorediamond += 1
            status.maze[pos[0]][pos[1]] = Const.MAZE_ROAD
            status.progress_pause = True
            status.progresstimer.start()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status.close = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    status.key_left = True
                elif event.key == pygame.K_RIGHT:
                    status.key_right = True
                elif event.key == pygame.K_UP:
                    status.key_up = True
                elif event.key == pygame.K_DOWN:
                    status.key_down = True
                elif event.key == pygame.K_m:
                    status.checkmap = not status.checkmap

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    status.key_left = False
                elif event.key == pygame.K_RIGHT:
                    status.key_right = False
                elif event.key == pygame.K_UP:
                    status.key_up = False
                elif event.key == pygame.K_DOWN:
                    status.key_down = False

            elif event.type == pygame.MOUSEMOTION:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                status.buttons["gamepause"].selected(mouse_x, mouse_y)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                if status.buttons["gamepause"].selected(mouse_x, mouse_y):
                    status.interface = Status.INTERFACE_PAUSE
                    status.timer.pause()

        if status.key_left == True and status.key_right == False and status.key_up == False and status.key_down == False:
            status.player.go_left()
        elif status.key_left == False and status.key_right == True and status.key_up == False and status.key_down == False:
            status.player.go_right()
        elif status.key_left == False and status.key_right == False and status.key_up == True and status.key_down == False:
            status.player.go_up()
        elif status.key_left == False and status.key_right == False and status.key_up == False and status.key_down == True:
            status.player.go_down()

    status.changetime()
    status.changediamond()
    status.changescore()


def check_pause(screen, status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status.close = True
        if event.type == pygame.MOUSEMOTION:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            status.buttons["retry"].selected(mouse_x, mouse_y)
            status.buttons["returnmain"].selected(mouse_x, mouse_y)
            status.buttons["continue"].selected(mouse_x, mouse_y)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if status.buttons["returnmain"].selected(mouse_x, mouse_y):
                status.interface = Status.INTERFACE_LOGIN
                status.level = Status.LEVELBEGIN
                status.interruptgame()
                return
            if status.buttons["continue"].selected(mouse_x, mouse_y):
                status.interface = Status.INTERFACE_GAME
                status.timer.start()
            if status.buttons["retry"].selected(mouse_x, mouse_y):
                status.interface = Status.INTERFACE_GAME
                status.interruptgame()
                status.replay()
                return

def check_result(screen, status):
    if status.level == Status.LEVELBEGIN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status.close = True
            if event.type == pygame.MOUSEMOTION:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                status.buttons["next"].selected(mouse_x, mouse_y)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if status.buttons["next"].selected(mouse_x, mouse_y):
                    status.interface = Status.INTERFACE_LOGIN
                    status.level = Status.LEVELBEGIN

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status.close = True
            if event.type == pygame.MOUSEMOTION:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                status.buttons["next"].selected(mouse_x, mouse_y)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if status.buttons["next"].selected(mouse_x, mouse_y):
                    status.interface = Status.INTERFACE_GAME
                    status.timer.reset()
                    status.timer.start()

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
    if status.interface == Status.INTERFACE_PAUSE:
        check_pause(screen, status)
    if status.interface == Status.INTERFACE_RESULT:
        check_result(screen, status)

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
    status.buttons["introduction7"].blit_button()

def draw_restart(screen, status):
    screen.fill(Const.COLOR_LIGHTGRAY)
    status.buttons["gameover"].blit_button()
    status.buttons["retry"].blit_button()
    status.buttons["returnmain"].blit_button()

def draw_game(screen, status):

    screen.fill(Const.COLOR_LIGHTGRAY)

    dis = status.distribution
    if status.checkmap: # 显示分布图
        for i in range(Const.MAZE_HEIGHT_SQUARE):
            for j in range(Const.MAZE_WIDTH_SQUARE):
                length = Const.DISTRIBUTION_PIXEL
                posx = Const.DISTRIBUTION_POSX + j * length
                posy = Const.DISTRIBUTION_POSY + i * length
                if dis[i][j] == 0:
                    pygame.draw.rect(screen, Const.COLOR_WHITE, (posx, posy, length, length))
                elif dis[i][j] == 0.2:
                    pygame.draw.rect(screen, Const.COLOR_YELLOW1, (posx, posy, length, length))
                elif dis[i][j] == 0.4:
                    pygame.draw.rect(screen, Const.COLOR_YELLOW2, (posx, posy, length, length))
                elif dis[i][j] == 0.6:
                    pygame.draw.rect(screen, Const.COLOR_YELLOW3, (posx, posy, length, length))
                elif dis[i][j] == 0.8:
                    pygame.draw.rect(screen, Const.COLOR_YELLOW4, (posx, posy, length, length))
                else:
                    pygame.draw.rect(screen, Const.COLOR_YELLOW5, (posx, posy, length, length))
        status.buttons["introduction8"].blit_button()
        status.buttons["introduction9"].blit_button()
        return


    # 绘制迷宫
    # 尽量使人物处于中间位置，因此就需要计算需要呈现于图中的区域
    player_posx = status.player.actual_posx
    player_posy = status.player.actual_posy

    center_posx = player_posx
    center_posy = player_posy

    half_surface_width = Const.GAME_SURFACE_WIDTH / 2
    half_surface_height = Const.GAME_SURFACE_HEIGHT / 2
    map_width = Const.MAZE_SQUARE_PIXEL * Const.MAZE_WIDTH_SQUARE
    map_height = Const.MAZE_SQUARE_PIXEL * Const.MAZE_HEIGHT_SQUARE

    # 先确定中心
    if center_posx <= half_surface_width:
        center_posx = half_surface_width
    elif center_posx >=map_width - half_surface_width:
        center_posx = map_width - half_surface_width
    
    if center_posy <= half_surface_height:
        center_posy = half_surface_height
    elif center_posy >=map_height - half_surface_height:
        center_posy = map_height - half_surface_height

    # 围绕中心画图
    center_posx = int(center_posx)
    center_posy = int(center_posy)
    center_square_x = center_posx // Const.MAZE_SQUARE_PIXEL
    center_square_y = center_posy // Const.MAZE_SQUARE_PIXEL

    for i in range(max(0, center_square_y - (Const.MAZE_DISPLAY_HEIGHT_SQUARE + 1) // 2), min(Const.MAZE_HEIGHT_SQUARE - 1, center_square_y + (Const.MAZE_DISPLAY_HEIGHT_SQUARE + 1) // 2) + 1):
        for j in range(max(0, center_square_x - (Const.MAZE_DISPLAY_WIDTH_SQUARE + 1) // 2), min(Const.MAZE_WIDTH_SQUARE - 1, center_square_x + (Const.MAZE_DISPLAY_WIDTH_SQUARE + 1) // 2) + 1):
            image_posx = j * Const.MAZE_SQUARE_PIXEL - (center_posx - half_surface_width)
            image_posy = i * Const.MAZE_SQUARE_PIXEL - (center_posy - half_surface_height)
            image_posx += Const.GAME_INTERFACE_MAINAREA_POSX
            image_posy += Const.GAME_INTERFACE_MAINAREA_POSY

            if status.maze[i][j] == Const.MAZE_WALL:
                status.images["wall"].blit_image(status.screen, image_posx, image_posy)
            elif status.maze[i][j] == Const.MAZE_ROAD:
                status.images["road"].blit_image(status.screen, image_posx, image_posy)
            elif status.maze[i][j] == Const.MAZE_FLAG:
                status.images["flag"].blit_image(status.screen, image_posx, image_posy)
            elif status.maze[i][j] == Const.MAZE_SCOREDIAMOND:
                status.images["road_scorediamond"].blit_image(status.screen, image_posx, image_posy)
            elif status.maze[i][j] == Const.MAZE_TIMEDIAMOND:
                status.images["road_timediamond"].blit_image(status.screen, image_posx, image_posy)
                
    
    player_image = status.player.images[status.player.direction - 1]
    dx = int(center_posx - player_posx)
    dy = int(center_posy - player_posy)
    player_image_posx = half_surface_width - dx
    player_image_posy = half_surface_height - dy
    player_image_posx += Const.GAME_INTERFACE_MAINAREA_POSX
    player_image_posy += Const.GAME_INTERFACE_MAINAREA_POSY
    player_image_posy -= player_image.height
    player_image.blit_image(status.screen, player_image_posx, player_image_posy)

    # 用和背景色相同的框遮住多余部分
    pygame.draw.rect(status.screen, Const.COLOR_LIGHTGRAY, (Const.GAME_INTERFACE_MAINAREA_POSX - Const.MAZE_SQUARE_PIXEL * 2, Const.GAME_INTERFACE_MAINAREA_POSY - Const.MAZE_SQUARE_PIXEL * 2, Const.MAZE_SQUARE_PIXEL * 2, Const.GAME_SURFACE_HEIGHT + 4 * Const.MAZE_SQUARE_PIXEL))
    pygame.draw.rect(status.screen, Const.COLOR_LIGHTGRAY, (Const.GAME_INTERFACE_MAINAREA_POSX, Const.GAME_INTERFACE_MAINAREA_POSY - Const.MAZE_SQUARE_PIXEL * 2, Const.GAME_SURFACE_WIDTH, Const.MAZE_SQUARE_PIXEL * 2))
    pygame.draw.rect(status.screen, Const.COLOR_LIGHTGRAY, (Const.GAME_INTERFACE_MAINAREA_POSX, Const.GAME_INTERFACE_MAINAREA_POSY + Const.GAME_SURFACE_HEIGHT, Const.GAME_SURFACE_WIDTH, Const.MAZE_SQUARE_PIXEL * 2))
    pygame.draw.rect(status.screen, Const.COLOR_LIGHTGRAY, (Const.GAME_INTERFACE_MAINAREA_POSX + Const.GAME_SURFACE_WIDTH, Const.GAME_INTERFACE_MAINAREA_POSY - Const.MAZE_SQUARE_PIXEL * 2, Const.MAZE_SQUARE_PIXEL * 2, Const.GAME_SURFACE_HEIGHT + 4 * Const.MAZE_SQUARE_PIXEL))

    # 显示时间得分
    status.buttons["time"].blit_button()
    status.buttons["score"].blit_button()

    # 显示玩家收集的宝石数量
    status.images["scorediamond"].blit_image(status.screen, 0, Const.SCREEN_HEIGHT - 83)
    status.images["timediamond"].blit_image(status.screen, 170, Const.SCREEN_HEIGHT - 80)
    status.buttons["num_scorediamond"].blit_button()
    status.buttons["num_timediamond"].blit_button()
    status.buttons["gamepause"].blit_button()

    # 显示进度条
    status.buttons["progressbar"].blit_button()
    pygame.draw.rect(status.screen, Const.COLOR_BLUE, (Const.SCREEN_WIDTH - 320, Const.SCREEN_HEIGHT - 68, Const.PROGRESSBAR_WIDTH, 20), 2)
    pygame.draw.rect(status.screen, Const.COLOR_BLUE, (Const.SCREEN_WIDTH - 320, Const.SCREEN_HEIGHT - 68, int(status.fillwidth), 20)) # 填充进度条



def draw_pause(screen, status):
    screen.fill(Const.COLOR_LIGHTGRAY)
    status.buttons["pause"].blit_button()
    status.buttons["retry"].blit_button()
    status.buttons["returnmain"].blit_button()
    status.buttons["continue"].blit_button()

def draw_result(screen, status):
    if status.level == Status.LEVELBEGIN:
        status.buttons["next"].update_text("回到主界面")
    else:
        status.buttons["next"].update_text("下一关") 
    screen.fill(Const.COLOR_LIGHTGRAY)
    status.buttons["next"].blit_button()
    status.buttons["pass"].blit_button()
    status.buttons["resultscore"].blit_button()
    status.buttons["getscore"].update_text(str(int(status.score)))
    status.buttons["calculatescore"].blit_button()
    status.buttons["getscore"].blit_button()

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
    if status.interface == Status.INTERFACE_PAUSE:
        draw_pause(screen, status)
    if status.interface == Status.INTERFACE_RESULT:
        draw_result(screen, status)


