import pygame
import os

from const import Const

def check_events(screen):
    """
    事件监听
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os._exit(0)
