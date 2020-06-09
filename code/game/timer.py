import os
import pygame

class Timer:
    """
    定制一个游戏中的计时器
    """
    def __init__(self):
        self.reset()

    def reset(self):
        self.lastbegin = 0
        self.pausebegin = 0
        
        self.totalpause = 0
        self.totalactive = 0

    def start(self):
        self.totalpause += (pygame.time.get_ticks() - self.pausebegin)
        self.lastbegin = pygame.time.get_ticks()

    def getactivetime(self):
        return (self.totalactive + pygame.time.get_ticks() - self.lastbegin)

    def pause(self):
        self.totalactive += (pygame.time.get_ticks() - self.lastbegin)
        self.pausebegin = pygame.time.get_ticks()
