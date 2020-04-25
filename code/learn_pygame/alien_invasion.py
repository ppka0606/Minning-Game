import pygame
from pygame.sprite import Group

import game_function as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
# from alien import Alien
    # 转移到特定的函数中去处理

def run_game():

    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    play_button = Button(ai_settings, screen, "Play now!")
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group() 

    # alien = Alien(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()