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
# ֱ�ӵ���sys.exit()ʱ���׳�һ��SystemExit�쳣,����쳣�ǿ��Ա������
# �����������쳣,����ʹ��os._exit(0)

        screen.fill(background_color)# ��ָ����rgbԪ��������ɫ

        pygame.display.flip()

run_game()