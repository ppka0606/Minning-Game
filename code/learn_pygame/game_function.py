# import sys
import pygame
import os

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
            # 按住空格键添加一颗新的子弹进去

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right =False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        # 退出事件
        if event.type == pygame.QUIT:
            os._exit(0)
# 直接调用sys.exit()时会抛出一个SystemExit异常,这个异常是可以被捕获的
# 如果不想出现异常,可以使用os._exit(0)

        # 键盘事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship, bullets):

    screen.fill(ai_settings.background_color)# 用指定的rgb元组来填充底色

    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()

    pygame.display.flip()

