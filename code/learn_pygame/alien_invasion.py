import sys
import os
import pygame
from settings import Settings

def run_game():

    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                # os._exit(0)
# 直接调用sys.exit()时会抛出一个SystemExit异常,这个异常是可以被捕获的
# 如果不想出现异常,可以使用os._exit(0)

        screen.fill(ai_settings.background_color)# 用指定的rgb元组来填充底色

        pygame.display.flip()

run_game()