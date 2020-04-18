import sys
import os
import pygame

def run_game():

    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Alien Invasion")
    background_color = (230,230,230)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                # os._exit(0)
# 直接调用sys.exit()时会抛出一个SystemExit异常,这个异常是可以被捕获的
# 如果不想出现异常,可以使用os._exit(0)

        screen.fill(background_color)# 用指定的rgb元组来填充底色

        pygame.display.flip()

run_game()