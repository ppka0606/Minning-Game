# import sys
import pygame
import os

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire(ai_settings, screen, ship, bullets)

def fire(ai_settings, screen, ship, bullets):
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
            # 按住空格键添加一颗新的子弹进去

def check_keyup_events(event, ship):
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

def update_screen(ai_settings, screen, ship, alien, bullets):

    screen.fill(ai_settings.background_color)# 用指定的rgb元组来填充底色

    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()
    alien.draw(screen)

    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()

    # 删除已经飞出屏幕的子弹,否则他们将持续消耗资源
    for bullet in bullets.copy():
        # 必须使用副本,否则迭代器会出问题
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
        # 很好用的调试技巧,可以发现子弹的数量不会超过某个特定的值(手速固定的情况下),一段时间不操作后自动归零


# 绘制alien

def get_number_alines_x(ai_settings, alien_width):
    """
    每行能装下多少个alien
    """
    available_space_x = ai_settings.screen_width - 2 * alien_width
        # 设置间隔为两个alien的宽度
    number_aliens_x = int(available_space_x / (2 * alien_width))

    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien) 

# 创建多行alien
def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_fleet(ai_settings, screen, ship, aliens):
    """
    创建一群alien
    """
    alien_example = Alien(ai_settings, screen)
        # 重命名为alien_example,以便于和下文区分.这个Alien实例的作用仅是为了获得长宽数据以进行计算
    number_aliens_x = get_number_alines_x(ai_settings, alien_example.rect.width)    
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien_example.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def update_aliens(ai_settings, aliens):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

def check_fleet_edges(ai_settings, aliens):
    """
    处理alien到达边缘时候的情况
    """
    for alien in aliens:
        if alien.check_edges() == True:
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """
    将alien整体下移,并切换左右方向
    """
    for alien in aliens:
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

