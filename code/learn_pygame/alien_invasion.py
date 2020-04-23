import pygame
from pygame.sprite import Group

import game_function as gf
from settings import Settings
from ship import Ship

def run_game():

    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(ai_settings,screen)
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # 删除已经飞出屏幕的子弹,否则他们将持续消耗资源
        for bullet in bullets.copy():
            # 必须使用副本,否则迭代器会出问题
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        # print(len(bullets))
            # 很好用的调试技巧,可以发现子弹的数量不会超过某个特定的值(手速固定的情况下),一段时间不操作后自动归零
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()