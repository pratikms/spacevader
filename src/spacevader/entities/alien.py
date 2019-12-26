import os
from itertools import count

import pygame

from entities.constant import Constant

class Alien:

    _ids = count(0)

    def __init__(self, x=None, y=None, x_change=None, y_change=None):
        self.id = next(self._ids)
        self._icon = pygame.image.load(Constant.ALIEN_ICON)
        self._x = x
        self._y = y
        self._x_change = x_change
        self._y_change = y_change
        self.invaded = False

    @property
    def x(self):
        return self._x

    # @x.setter
    # def x(self, x):
    #     if x <= Constant.LEFT_BOUNDARY:
            

    def render(self, screen):
        screen.blit(self._icon, (self._x, self._y))
