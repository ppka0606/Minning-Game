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
# ֱ�ӵ���sys.exit()ʱ���׳�һ��SystemExit�쳣,����쳣�ǿ��Ա������
# �����������쳣,����ʹ��os._exit(0)

        screen.fill(ai_settings.background_color)# ��ָ����rgbԪ��������ɫ

        pygame.display.flip()

run_game()