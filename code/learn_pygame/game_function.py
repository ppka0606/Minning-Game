# import sys
import pygame
import os

def check_keydown_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right =False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    for event in pygame.event.get():
        # 退出事件
        if event.type == pygame.QUIT:
            os._exit(0)
# 直接调用sys.exit()时会抛出一个SystemExit异常,这个异常是可以被捕获的
# 如果不想出现异常,可以使用os._exit(0)

        # 键盘事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship):

    screen.fill(ai_settings.background_color)# 用指定的rgb元组来填充底色
    ship.blitme()

    pygame.display.flip()

